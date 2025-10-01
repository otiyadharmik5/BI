from src.logger import setup_logger
from src.validation import validate_order_inputs
from src.binance_client import get_client

logger = setup_logger()
client = get_client()

def place_market_order(symbol: str, side: str, quantity: float):
    try:
        data = validate_order_inputs(symbol, side, quantity)
        logger.info(f"Placing MARKET order: {data}")
        resp = client.place_market_order(data['symbol'], data['side'], data['quantity'])
        logger.info(f"Order response: {resp}")
        return {"status": "success", "response": resp}
    except Exception as e:
        logger.exception("Market order failed")
        return {"status": "error", "message": str(e)}
