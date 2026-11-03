"""Order lookup service backed by an in-memory store."""
ORDERS = {1: {"id": 1, "customer": "Demo Customer"}, 2: {"id": 2, "customer": "Contoso"}}


def get_order(order_id: int) -> dict:
    order = ORDERS.get(order_id)
    return {"id": order["id"], "customer": order["customer"]}
