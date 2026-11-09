# Contoso Orders API

Small FastAPI service used for Azure SRE Agent + GitHub incident-response testing. Orders are synthetic in-memory data.

## Run locally

Requires Python 3.13.

Windows PowerShell:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m uvicorn app.main:app --reload
```

Linux/macOS:

```sh
python3.13 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m uvicorn app.main:app --reload
```

Endpoints: `/health`, `/orders/{order_id}`, `/docs` on `http://127.0.0.1:8000`.

## Run the production container

Requires Docker. From the repository root:

```sh
docker build -t contoso-orders-api:local .
docker run --rm --name orders-api --publish 127.0.0.1:8000:8000 contoso-orders-api:local
```

In a second terminal, smoke-test the running container:

```sh
curl --fail http://127.0.0.1:8000/health
curl --fail http://127.0.0.1:8000/orders/1
```

Stop the container with Ctrl+C in the first terminal; `--rm` removes it automatically.

## Test

After installing the development requirements in the virtual environment:

```sh
python -m pytest -ra
```
