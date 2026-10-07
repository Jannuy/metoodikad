# Õppeainete tagasiside

## Docker Compose arenduses

Käivita Docker Desktop ja seejärel projekti juurkaustast:

```powershell
docker compose up --build
```

Rakendused:

- Vue/Vite: <http://localhost:5173>
- Django API: <http://localhost:8000/api/>
- Django admin: <http://localhost:8000/admin/>
- PostgreSQL: konteinerisisene teenus `db`, andmed on volume'is `postgres_data`

Peata teenused:

```powershell
docker compose down
```

Andmebaasi koos andmetega eemaldamiseks kasuta eraldi käsku:

```powershell
docker compose down -v
```

Kopeeri `.env.example` fail `.env` failiks, kui soovid muuta PostgreSQL-i või Django
seadeid.

## Ilma Dockerita

Backend:

```powershell
.\.venv\Scripts\Activate.ps1
python backend\manage.py migrate
python backend\manage.py runserver
```

Frontend teises terminalis:

```powershell
npm run dev
```

Rakenduse kasutajaliides asub kaustas `frontend/src` ja kasutab Vue 3,
Vue Routerit ning Vite'i. Juurkausta `index.html`, `script.js` ja `style.css`
on algne staatiline mockup; arenduses käivitatakse Vue rakendus käsuga
`npm run dev`. Vue saadab tagasiside Django REST API-le aadressidel
`/api/feedback/` ja `/api/summary/`.
