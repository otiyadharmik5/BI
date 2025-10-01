import time
from src.logger import setup_logger
from src.validation import validate_order_inputs
from src.binance_client import get_client

logger = setup_logger()
client = get_client()

def run_twap(symbol: str, side: str, quantity: float, slices: int = 5, interval: float = 1.0):
    try:
        data = validate_order_inputs(symbol, side, quantity)
        piece = data['quantity'] / slices
        results = []
        for i in range(slices):
            logger.info(f"TWAP slice {i+1}/{slices}: {piece}")
            resp = client.place_market_order(data['symbol'], data['side'], piece)
            results.append(resp)
            time.sleep(interval)
        return {"status": "success", "results": results}
    except Exception as e:
        logger.exception("TWAP failed")
        return {"status": "error", "message": str(e)}
