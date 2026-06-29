"""Create a local development admin user.

This script is intentionally blocked in production. It is meant for local Docker
or developer workstations only.
"""

from app.core.config import settings
from app.core.security import hash_password
from app.db.session import SessionLocal
from app.models.user import User
from sqlalchemy import select

DEV_ADMIN_EMAIL = "admin@example.com"
DEV_ADMIN_PASSWORD = "Admin12345!"


def seed_dev_admin() -> None:
    if settings.environment.lower() == "production":
        raise RuntimeError("Refusing to seed a default admin in production.")

    db = SessionLocal()
    try:
        user = db.scalar(select(User).where(User.email == DEV_ADMIN_EMAIL))
        if user is None:
            user = User(
                email=DEV_ADMIN_EMAIL,
                username="dev-admin",
                full_name="Development Admin",
                password_hash=hash_password(DEV_ADMIN_PASSWORD),
                role="admin",
                is_active=True,
                is_email_verified=True,
            )
            db.add(user)
        else:
            user.password_hash = hash_password(DEV_ADMIN_PASSWORD)
            user.role = "admin"
            user.is_active = True
            user.is_email_verified = True
            user.deleted_at = None
            db.add(user)
        db.commit()
        print(f"Development admin ready: {DEV_ADMIN_EMAIL} / {DEV_ADMIN_PASSWORD}")
    finally:
        db.close()


if __name__ == "__main__":
    seed_dev_admin()
