import os
import time
import random
from typing import Dict, Any

MOCK = os.environ.get("BINANCE_MOCK", "1") == "1"
API_KEY = os.environ.get("BINANCE_API_KEY", "")
API_SECRET = os.environ.get("BINANCE_API_SECRET", "")

class BinanceClientWrapper:
    def __init__(self, api_key: str = API_KEY, api_secret: str = API_SECRET, mock: bool = MOCK):
        self.mock = mock
        self.api_key = api_key
        self.api_secret = api_secret

    def place_market_order(self, symbol: str, side: str, quantity: float) -> Dict[str, Any]:
        if self.mock:
            return self._mock_order("MARKET", symbol, side, quantity, None)
        raise NotImplementedError("Real Binance API not implemented.")

    def place_limit_order(self, symbol: str, side: str, quantity: float, price: float) -> Dict[str, Any]:
        if self.mock:
            return self._mock_order("LIMIT", symbol, side, quantity, price)
        raise NotImplementedError("Real Binance API not implemented.")

    def _mock_order(self, order_type, symbol, side, quantity, price):
        time.sleep(0.2)
        return {
            "orderId": int(time.time() * 1000) + random.randint(0, 999),
            "symbol": symbol,
            "status": "FILLED" if order_type == "MARKET" else "NEW",
            "type": order_type,
            "side": side,
            "origQty": quantity,
            "price": price or round(random.uniform(10000, 60000), 2),
            "filledQty": quantity if order_type == "MARKET" else 0,
            "info": {"mock": True}
        }

_client = None
def get_client():
    global _client
    if _client is None:
        _client = BinanceClientWrapper()
    return _client
