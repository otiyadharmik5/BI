from src.logger import setup_logger
from src.validation import validate_order_inputs
from src.binance_client import get_client

logger = setup_logger()
client = get_client()

def place_limit_order(symbol: str, side: str, quantity: float, price: float):
    try:
        data = validate_order_inputs(symbol, side, quantity, price)
        logger.info(f"Placing LIMIT order: {data}")
        resp = client.place_limit_order(data['symbol'], data['side'], data['quantity'], data['price'])
        logger.info(f"Order response: {resp}")
        return {"status": "success", "response": resp}
    except Exception as e:
        logger.exception("Limit order failed")
        return {"status": "error", "message": str(e)}
