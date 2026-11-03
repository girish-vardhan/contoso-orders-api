"""Order lookup service backed by an in-memory store."""
from fastapi import HTTPException

ORDERS = {1: {"id": 1, "customer": "Demo Customer"}, 2: {"id": 2, "customer": "Contoso"}}


def get_order(order_id: int) -> dict:
    order = ORDERS.get(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"id": order["id"], "customer": order["customer"]}
