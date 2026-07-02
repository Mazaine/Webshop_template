# Webshop Template Teljes Dokumentáció

## 1. Áttekintés

A Webshop Template egy semleges, újrahasznosítható full-stack webshop alap. Célja, hogy új webáruház projektek gyors indításához adjon stabil backend, frontend, admin és infrastruktúra kiindulópontot.

A template nem tartalmaz projekt-specifikus brandet, demo termékeket, jogi PDF-eket, éles API kulcsokat vagy production secreteket. A projekt React + FastAPI + PostgreSQL + Redis + Docker alapokra épül.

## 2. Fő funkciók

- Felhasználói regisztráció és belépés.
- JWT alapú autentikáció.
- Felhasználói fiók oldal.
- Termékek és kategóriák.
- Termékrészletek variáns kezeléssel.
- Kosár.
- Checkout.
- Rendelések.
- Admin dashboard.
- Admin termékkezelés.
- Admin rendeléskezelés.
- Admin felhasználókezelés.
- Szállítási módok.
- Átvételi pont alap.
- Newsletter alap.
- Tranzakciós e-mail alap.
- Cloudflare Turnstile-ready botvédelem.
- Rate limiting.
- Security middleware.
- OpenAPI dokumentáció.
- Backend tesztek.
- Frontend production build.
- Magyar/angol frontend nyelvváltó.

## 3. Technológiai stack

### Backend

- Python
- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Redis
- pytest
- Pydantic settings

### Frontend

- React
- TypeScript
- Vite
- React Router
- Axios
- Saját CSS komponensrendszer
- Saját könnyű i18n helper

### Infrastruktúra

- Docker Compose
- PostgreSQL konténer
- Redis konténer
- Backend konténer
- Frontend konténer

## 4. Projekt struktúra

```text
.
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── crud/
│   │   ├── db/
│   │   ├── dependencies/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── scripts/
│   │   └── services/
│   ├── alembic/
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── context/
│   │   ├── hooks/
│   │   ├── i18n/
│   │   ├── pages/
│   │   ├── styles/
│   │   └── utils/
│   ├── Dockerfile
│   ├── package.json
│   └── vite.config.ts
├── docs/
├── docker-compose.yml
├── README.md
└── TEMPLATE_AUDIT.md
```

## 5. Gyors indítás Dockerrel

1. Hozd létre a lokális `.env` fájlokat a minták alapján.

```bash
copy .env.example .env
copy backend\.env.example backend\.env
copy frontend\.env.example frontend\.env
```

2. Cseréld a placeholder secreteket és projekt adatokat.

3. Indítsd a stack-et.

```bash
docker compose up --build
```

4. Nyisd meg az alkalmazást.

- Frontend: `http://localhost:5173`
- Backend API: `http://localhost:8000`
- API dokumentáció: `http://localhost:8000/docs`

## 6. Környezeti változók

A template csak `.env.example` fájlokat tartalmaz. Éles vagy lokális `.env` fájlokat nem szabad commitolni.

### Fontos backend változók

- `PROJECT_NAME`: backend projekt neve.
- `DATABASE_URL`: PostgreSQL connection string.
- `SECRET_KEY`: JWT és biztonsági műveletek titka.
- `BACKEND_CORS_ORIGINS`: engedélyezett frontend origin lista.
- `SMTP_HOST`: SMTP szerver.
- `SMTP_PORT`: SMTP port.
- `SMTP_USER`: SMTP felhasználó.
- `SMTP_PASSWORD`: SMTP jelszó.
- `SMTP_FROM_EMAIL`: feladó e-mail cím.
- `BREVO_API_KEY`: Brevo API kulcs, ha Brevo integrációt használsz.
- `BANK_TRANSFER_ACCOUNT_NAME`: banki kedvezményezett.
- `BANK_TRANSFER_ACCOUNT_NUMBER`: bankszámlaszám.
- `BANK_TRANSFER_BANK_NAME`: bank neve.
- `ENVIRONMENT`: `development`, `test`, `production`.
- `CAPTCHA_PROVIDER`: például `turnstile`.
- `CAPTCHA_ENABLED`: botvédelem be- vagy kikapcsolása.
- `TURNSTILE_SECRET_KEY`: Cloudflare Turnstile backend secret.
- `RATE_LIMIT_BACKEND`: `memory` vagy Redis alapú beállítás.
- `REDIS_URL`: Redis connection string.

### Fontos frontend változók

- `VITE_API_BASE_URL`: backend API URL, ha a default nem megfelelő.
- `VITE_CAPTCHA_PROVIDER`: captcha provider.
- `VITE_CAPTCHA_ENABLED`: frontend captcha kapcsoló.
- `VITE_TURNSTILE_SITE_KEY`: Cloudflare Turnstile site key.

## 7. Backend dokumentáció

### Backend belépési pont

- `backend/app/main.py`

Itt történik a FastAPI app inicializálása, middleware-ek, routerek és alap konfigurációk bekötése.

### API modulok

- `backend/app/api/auth.py`: regisztráció, belépés, saját profil, jelszókezelés.
- `backend/app/api/products.py`: publikus terméklekérdezések.
- `backend/app/api/categories.py`: publikus kategórialista.
- `backend/app/api/checkout.py`: rendelés létrehozása checkoutból.
- `backend/app/api/orders.py`: saját rendelések.
- `backend/app/api/admin.py`: admin statisztikák, termékek, rendelések, felhasználók.
- `backend/app/api/newsletter.py`: hírlevél feliratkozás és saját státusz.
- `backend/app/api/shipping.py`: szállítási módok.
- `backend/app/api/pickup_points.py`: átvételi pontok.
- `backend/app/api/health.py`: health check.
- `backend/app/api/test_email.py`: fejlesztői e-mail teszt végpont.

### Modellek

- `User`: felhasználók és admin jogosultság.
- `Category`: termékkategóriák.
- `Product`: termék alapadatok.
- `ProductVariant`: termékvariánsok.
- `Order`: rendelés fejléc.
- `OrderItem`: rendelés tételek.
- `NewsletterSubscriber`: hírlevél feliratkozók.
- `NewsletterCampaign`: hírlevél kampány alap.
- `ShippingMethod`: szállítási módok.
- `PickupPoint`: átvételi pontok.
- `SecurityLog`: biztonsági események.
- `StockMovement`: készletmozgások.

### Sémák

A `backend/app/schemas/` mappa tartalmazza a request és response DTO-kat. Új endpoint esetén itt érdemes Pydantic sémát létrehozni.

### Adatbázis migráció

Alembic használatos.

Lokális migráció futtatása:

```bash
docker compose exec -T backend alembic upgrade head
```

Új migráció generálása fejlesztéskor:

```bash
docker compose exec -T backend alembic revision --autogenerate -m "description"
```

## 8. Frontend dokumentáció

### Frontend belépési pontok

- `frontend/src/main.tsx`: React app mount, provider hierarchia.
- `frontend/src/App.tsx`: route konfiguráció és kosár állapot.
- `frontend/src/styles/global.css`: globális design alapok.

### Fő oldalak

- `/`: Home.
- `/products`: terméklista.
- `/products/:slug`: termékrészletek.
- `/categories`: kategória áttekintés.
- `/category/:categorySlug`: kategória termékei.
- `/cart`: kosár.
- `/checkout`: checkout.
- `/checkout/success`: sikeres rendelés.
- `/login`: belépés.
- `/register`: regisztráció.
- `/account`: fiókom.
- `/my-orders`: saját rendelések.
- `/admin`: admin dashboard.
- `/admin/products`: admin termékek.
- `/admin/orders`: admin rendelések.
- `/admin/users`: admin felhasználók.
- `/admin/shipping`: admin szállítás.
- `/admin/newsletters`: admin hírlevelek.
- `*`: 404.

### API kliens

A frontend API rétege itt található:

`frontend/src/api/`

Fő fájlok:

- `client.ts`: Axios kliens és auth token kezelés.
- `auth.ts`: auth requestek.
- `products.ts`: termék requestek.
- `categories.ts`: kategória requestek.
- `checkout.ts`: checkout request.
- `orders.ts`: saját rendelések.
- `admin.ts`: admin requestek.
- `newsletter.ts`: hírlevél requestek.
- `shipping.ts`: szállítási requestek.
- `pickupPoints.ts`: átvételi pont requestek.

### UI komponensek

Közös UI komponensek:

`frontend/src/components/ui/`

- `Button`
- `Card`
- `Badge`
- `Input`
- `EmptyState`
- `LoadingState`
- `ErrorState`
- `PageHeader`
- `ProductGrid`

Layout és domain komponensek:

- `SiteHeader`
- `SiteFooter`
- `AdminLayout`
- `ProductCard`
- `ProtectedRoute`
- `PickupPointSelector`
- `CaptchaWidget`

## 9. Többnyelvűség

A frontend saját, könnyű i18n rendszert használ.

Fájlok:

```text
frontend/src/i18n/index.tsx
frontend/src/i18n/hu.ts
frontend/src/i18n/en.ts
```

Alapértelmezett nyelv: magyar.

A választott nyelv localStorage kulcsa:

```text
webshop-template.language
```

Nyelvváltó helye:

```text
frontend/src/components/SiteHeader.tsx
```

### Új nyelv hozzáadása

1. Hozz létre új fájlt, például `de.ts`.
2. Másold át a meglévő `hu.ts` kulcsstruktúráját.
3. Fordítsd le az értékeket.
4. Bővítsd a `Language` típust `index.tsx` fájlban.
5. Add hozzá az új nyelvet a `dictionaries` objektumhoz.
6. Tegyél új gombot a header nyelvváltóba.

## 10. Admin használat

### Admin login

Nincs külön admin login route. Az admin ugyanazon a login felületen lép be, mint a normál felhasználó.

- Login: `/login` vagy `/auth`
- Admin dashboard: `/admin`

### Dev admin seed

Local/dev környezetben futtatható:

```bash
docker compose exec -T backend python -m app.scripts.seed_dev_admin
```

Dev admin:

- Email: `admin@example.com`
- Password: `Admin12345!`

Production környezetben a script hibával leáll, és nem hoz létre alap admin felhasználót.

## 11. Kosár és checkout

A kosár frontend oldali állapotként működik, localStorage alapú perzisztenciával.

Fő fájlok:

- `frontend/src/App.tsx`
- `frontend/src/utils/cart.ts`
- `frontend/src/pages/CartPage.tsx`
- `frontend/src/pages/CheckoutPage.tsx`

Checkout során a frontend a backend `checkout` endpointot hívja, amely rendelést hoz létre. A template banki átutalási alapot tartalmaz, fizetési szolgáltató integrációt projekt szerint kell hozzáadni.

## 12. E-mail és newsletter

A template tartalmazza az e-mail rendszer alapjait:

- tranzakciós e-mail szolgáltatás,
- e-mail sablon alapok,
- newsletter subscriber kezelés,
- admin newsletter kampány alap.

Konfigurációhoz SMTP vagy Brevo jellegű szolgáltató adatok szükségesek. Production környezetben minden e-mail secretet környezeti változóban kell megadni.

## 13. Botvédelem és rate limiting

A template Cloudflare Turnstile-ready integrációt tartalmaz.

Fő fájlok:

- `backend/app/services/turnstile.py`
- `backend/app/services/captcha_service.py`
- `frontend/src/components/security/CaptchaWidget.tsx`
- `frontend/src/hooks/useCaptcha.ts`

A rate limiting alap a backend core rétegben található:

- `backend/app/core/rate_limit.py`

Redis alapú működéshez állítsd be a `REDIS_URL` és rate limit backend változókat.

## 14. Tesztelés

### Backend tesztek

Dockerrel:

```bash
docker compose exec -T backend pytest
```

Lokálisan:

```bash
cd backend
python -m pip install -r requirements.txt
python -m pytest
```

Aktuális validált eredmény:

- 8 teszt sikeres.
- Core flow tesztek sikeresek.
- E-mail service tesztek sikeresek.
- Rate limit tesztek sikeresek.

### Frontend build

Dockerrel:

```bash
docker compose exec -T frontend npm run build
```

Lokálisan:

```bash
cd frontend
npm install
npm run build
```

Aktuális validált eredmény:

- TypeScript build sikeres.
- Vite production build sikeres.

## 15. Fejlesztési workflow

Ajánlott napi fejlesztési folyamat:

1. Húzd le a legfrissebb kódot.
2. Indítsd a Docker stack-et.
3. Futtasd az Alembic migrációkat.
4. Seedeld a dev admint, ha szükséges.
5. Fejlessz backend vagy frontend oldalon.
6. Futtasd a releváns teszteket.
7. Futtasd a frontend buildet.
8. Commitolj kis, értelmes egységekben.

## 16. Új projekt indítása ebből a template-ből

1. Forkold vagy klónozd a repót.
2. Nevezd át a projektet saját brand szerint.
3. Cseréld a README és dokumentáció projektnevét.
4. Hozd létre a saját `.env` fájlokat.
5. Állítsd be a production secreteket.
6. Adj hozzá saját logót és vizuális asseteket.
7. Tölts fel saját kategóriákat és termékeket.
8. Készíts saját jogi dokumentumokat.
9. Állítsd be az e-mail szolgáltatót.
10. Állítsd be a captcha kulcsokat.
11. Állítsd be a payment vagy banki adatokat.
12. Futtasd a backend teszteket és frontend buildet.
13. Készíts production deployment konfigurációt.

## 17. Saját brand hozzáadása

Cserélendő területek:

- `README.md` projektleírás.
- `frontend/index.html` title/meta.
- `frontend/src/i18n/hu.ts` és `en.ts` brand szövegek.
- Header/footer szövegek.
- Faviconok.
- Logó.
- Színek a `frontend/src/styles/global.css` fájlban.
- OpenGraph/meta képek, ha szükséges.

## 18. Saját termékadatok hozzáadása

A template nem tartalmaz demo adatot. Termékadatokat projekt szerint kell létrehozni.

Lehetséges utak:

- Admin felületen manuális termékfelvitel.
- Saját seed script írása.
- Saját import pipeline készítése.
- Külső PIM/ERP integráció fejlesztése.

Fontos: ne hozz vissza projekt-specifikus import scriptet a template-be, ha az nem általánosan újrahasznosítható.

## 19. Deployment ajánlás

Production deployment előtt ellenőrizd:

- `ENVIRONMENT=production`
- erős `SECRET_KEY`
- production PostgreSQL URL
- production Redis URL
- CORS origin lista
- HTTPS
- reverse proxy beállítások
- SMTP/Brevo production kulcsok
- Cloudflare Turnstile kulcsok
- rate limiting
- backup stratégia
- monitoring
- logkezelés
- admin user provisioning

## 20. Biztonsági checklist

- Nincs `.env` commitolva.
- Nincs production API kulcs commitolva.
- Dev admin seed production környezetben blokkolva van.
- Admin route-ok role alapon védettek.
- Rate limiting megtartva.
- Security middleware megtartva.
- Captcha integráció beköthető.
- Production secret rotáció kötelező.
- GitHub secret scanning ajánlott.

## 21. Ismert korlátok

- A template nem tartalmaz valós brand asseteket.
- A template nem tartalmaz jogi PDF dokumentumokat.
- A template nem tartalmaz demo termékadatokat.
- A payment alap banki átutalás jellegű, payment provider integrációt külön kell hozzáadni.
- A pickup point integráció alapként maradt meg, éles carrier konfigurációt ellenőrizni kell.
- A frontend design template szintű, brandre szabás ajánlott.

## 22. Hibaelhárítás

### A frontend nem éri el a backendet

Ellenőrizd:

- `VITE_API_BASE_URL`
- Docker compose service nevek
- backend konténer fut-e
- CORS beállítások

### A login nem működik

Ellenőrizd:

- backend fut-e
- adatbázis migráció lefutott-e
- dev admin seed lefutott-e
- `SECRET_KEY` stabil-e
- browser localStorage token nem régi-e

### A checkout nem működik

Ellenőrizd:

- van-e termék a kosárban
- szállítási módok elérhetőek-e
- captcha beállítások helyesek-e
- backend logokban van-e validációs hiba

### Az e-mail küldés nem működik

Ellenőrizd:

- SMTP/Brevo környezeti változók
- sender e-mail cím
- szolgáltatói API kulcs
- backend logok

### A backend tesztek hibáznak

Ellenőrizd:

- dependency telepítés
- Python verzió
- teszt adatbázis konfiguráció
- Docker konténerek állapota

## 23. Hasznos parancsok

Stack indítása:

```bash
docker compose up --build
```

Stack leállítása:

```bash
docker compose down
```

Backend tesztek:

```bash
docker compose exec -T backend pytest
```

Frontend build:

```bash
docker compose exec -T frontend npm run build
```

Dev admin seed:

```bash
docker compose exec -T backend python -m app.scripts.seed_dev_admin
```

Alembic upgrade:

```bash
docker compose exec -T backend alembic upgrade head
```

Backend logok:

```bash
docker compose logs backend
```

Frontend logok:

```bash
docker compose logs frontend
```

## 24. Dokumentációs fájlok

- `README.md`: gyors áttekintés és indulás.
- `docs/PROJECT_DOCUMENTATION.md`: teljes használati és fejlesztői dokumentáció.
- `docs/COMPLETE_TEMPLATE_REPORT.md`: template készítési záró riport.
- `docs/frontend_template_redesign_report.md`: frontend redesign riport.
- `TEMPLATE_AUDIT.md`: template audit, eltávolítások és készenléti összegzés.

## 25. Záró megjegyzés

A Webshop Template célja, hogy stabil, biztonságos és semleges alapot adjon webshop projektekhez. Új projekt indításakor a legfontosabb feladatok a brandre szabás, production secretek beállítása, saját termékadatok feltöltése, jogi dokumentumok elkészítése és production deployment finomhangolása.
