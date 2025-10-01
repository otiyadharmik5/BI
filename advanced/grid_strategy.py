from src.logger import setup_logger
from src.validation import validate_order_inputs
from src.binance_client import get_client

logger = setup_logger()
client = get_client()

def run_grid(symbol: str, side: str, lower: float, upper: float, steps: int, quantity: float):
    try:
        if upper <= lower:
            raise ValueError("upper must be greater than lower.")
        data = validate_order_inputs(symbol, side, quantity)
        step_size = (upper - lower) / steps
        grid_orders = []
        for i in range(steps + 1):
            price = round(lower + i * step_size, 2)
            buy = client.place_limit_order(data['symbol'], "BUY", data['quantity'], price)
            sell = client.place_limit_order(data['symbol'], "SELL", data['quantity'], price + 0.01)
            grid_orders.append({"level": i, "buy": buy, "sell": sell})
        return {"status": "success", "grid": grid_orders}
    except Exception as e:
        logger.exception("Grid strategy failed")
        return {"status": "error", "message": str(e)}
