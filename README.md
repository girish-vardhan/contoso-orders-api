# Contoso Orders API

Small FastAPI service used for Azure SRE Agent + GitHub incident-response testing. Synthetic data only.

## Run locally

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m uvicorn app.main:app --reload
```

Endpoints: `/health`, `/orders/{order_id}`, `/docs`.

## Test

```powershell
python -m pytest -ra
```
