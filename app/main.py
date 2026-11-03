import logging
from fastapi import FastAPI
from app.service import get_order

logger = logging.getLogger(__name__)
app = FastAPI(title="Contoso Orders API")


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/orders/{order_id}")
def read_order(order_id: int):
    try:
        return get_order(order_id)
    except Exception:
        logger.exception("Order lookup failed: order_id=%s", order_id)
        raise
