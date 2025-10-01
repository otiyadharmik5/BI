import random
from src.logger import setup_logger
from src.validation import validate_order_inputs
from src.binance_client import get_client

logger = setup_logger()
client = get_client()

def place_oco(symbol: str, side: str, quantity: float, take_profit: float, stop_loss: float):
    try:
        data = validate_order_inputs(symbol, side, quantity)
        logger.info(f"Placing OCO: {data}, TP={take_profit}, SL={stop_loss}")
        tp_order = client.place_limit_order(data['symbol'], "SELL" if data['side']=="BUY" else "BUY", data['quantity'], take_profit)
        sl_order = client.place_limit_order(data['symbol'], "SELL" if data['side']=="BUY" else "BUY", data['quantity'], stop_loss)
        executed = random.choice(["tp", "sl", None])
        return {"status": "success", "tp_order": tp_order, "sl_order": sl_order, "executed": executed}
    except Exception as e:
        logger.exception("OCO failed")
        return {"status": "error", "message": str(e)}
