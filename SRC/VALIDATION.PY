from typing import Optional

VALID_SIDES = {"BUY", "SELL"}

def validate_symbol(symbol: str):
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a non-empty string.")
    if not symbol.upper().endswith("USDT"):
        raise ValueError("Symbol must be a USDT pair (e.g., BTCUSDT).")
    return symbol.upper()

def validate_side(side: str):
    if not side or side.upper() not in VALID_SIDES:
        raise ValueError("Side must be BUY or SELL.")
    return side.upper()

def validate_quantity(quantity: float):
    try:
        q = float(quantity)
    except Exception:
        raise ValueError("Quantity must be a number.")
    if q <= 0:
        raise ValueError("Quantity must be positive.")
    return q

def validate_price(price: Optional[float]):
    if price is None:
        return None
    try:
        p = float(price)
    except Exception:
        raise ValueError("Price must be numeric.")
    if p <= 0:
        raise ValueError("Price must be positive.")
    return p

def validate_order_inputs(symbol: str, side: str, quantity: float, price: Optional[float] = None):
    return {
        "symbol": validate_symbol(symbol),
        "side": validate_side(side),
        "quantity": validate_quantity(quantity),
        "price": validate_price(price)
    }
