"""Order lookup service backed by an in-memory store."""
ORDERS = {1: {"id": 1, "customer": "Demo Customer"}, 2: {"id": 2, "customer": "Contoso"}}


class OrderNotFoundError(LookupError):
    """Raised when an order ID does not exist."""


def get_order(order_id: int) -> dict:
    order = ORDERS.get(order_id)
    if order is None:
        raise OrderNotFoundError(order_id)
    return {"id": order["id"], "customer": order["customer"]}
