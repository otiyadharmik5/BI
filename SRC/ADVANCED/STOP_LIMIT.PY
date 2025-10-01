from src.logger import setup_logger
from src.validation import validate_order_inputs
from src.binance_client import get_client

logger = setup_logger()
client = get_client()

def place_stop_limit(symbol: str, side: str, quantity: float, stop_price: float, limit_price: float):
    try:
        data = validate_order_inputs(symbol, side, quantity, limit_price)
        if stop_price <= 0:
            raise ValueError("stop_price must be positive.")
        logger.info(f"Placing STOP-LIMIT order: {data}, stop={stop_price}")
        resp = client.place_limit_order(data['symbol'], data['side'], data['quantity'], limit_price)
        logger.info(f"Stop-limit placed (simulated): {resp}")
        return {"status": "success", "response": resp}
    except Exception as e:
        logger.exception("Stop-limit failed")
        return {"status": "error", "message": str(e)}
