import argparse
from src.market_orders import place_market_order
from src.limit_orders import place_limit_order
from src.advanced.stop_limit import place_stop_limit
from src.advanced.oco import place_oco
from src.advanced.twap import run_twap
from src.advanced.grid_strategy import run_grid

def main():
    parser = argparse.ArgumentParser("Binance Futures CLI Bot")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_market = sub.add_parser("market")
    p_market.add_argument("symbol")
    p_market.add_argument("side", choices=["BUY", "SELL"])
    p_market.add_argument("quantity", type=float)

    p_limit = sub.add_parser("limit")
    p_limit.add_argument("symbol")
    p_limit.add_argument("side", choices=["BUY", "SELL"])
    p_limit.add_argument("quantity", type=float)
    p_limit.add_argument("--price", type=float, required=True)

    p_sl = sub.add_parser("stoplimit")
    p_sl.add_argument("symbol")
    p_sl.add_argument("side", choices=["BUY", "SELL"])
    p_sl.add_argument("quantity", type=float)
    p_sl.add_argument("--stop_price", type=float, required=True)
    p_sl.add_argument("--limit_price", type=float, required=True)

    p_oco = sub.add_parser("oco")
    p_oco.add_argument("symbol")
    p_oco.add_argument("side", choices=["BUY", "SELL"])
    p_oco.add_argument("quantity", type=float)
    p_oco.add_argument("--tp", type=float, required=True)
    p_oco.add_argument("--sl", type=float, required=True)

    p_twap = sub.add_parser("twap")
    p_twap.add_argument("symbol")
    p_twap.add_argument("side", choices=["BUY", "SELL"])
    p_twap.add_argument("quantity", type=float)
    p_twap.add_argument("--slices", type=int, default=5)
    p_twap.add_argument("--interval", type=float, default=1.0)

    p_grid = sub.add_parser("grid")
    p_grid.add_argument("symbol")
    p_grid.add_argument("side", choices=["BUY", "SELL"])
    p_grid.add_argument("--lower", type=float, required=True)
    p_grid.add_argument("--upper", type=float, required=True)
    p_grid.add_argument("--steps", type=int, default=5)
    p_grid.add_argument("--quantity", type=float, required=True)

    args = parser.parse_args()

    if args.cmd == "market":
        print(place_market_order(args.symbol, args.side, args.quantity))
    elif args.cmd == "limit":
        print(place_limit_order(args.symbol, args.side, args.quantity, args.price))
    elif args.cmd == "stoplimit":
        print(place_stop_limit(args.symbol, args.side, args.quantity, args.stop_price, args.limit_price))
    elif args.cmd == "oco":
        print(place_oco(args.symbol, args.side, args.quantity, args.tp, args.sl))
    elif args.cmd == "twap":
        print(run_twap(args.symbol, args.side, args.quantity, args.slices, args.interval))
    elif args.cmd == "grid":
        print(run_grid(args.symbol, args.side, args.lower, args.upper, args.steps, args.quantity))

if __name__ == "__main__":
    main()
