from jesse.strategies import Strategy
import pandas as pd

from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

class ExampleStrategy(Strategy):
    def should_long(self) -> bool:
        return True

    def should_short(self) -> bool:
        return False

    def should_cancel(self) -> bool:
        return False

    def go_long(self):
        current_timestamp = self.current_candle[0]
        print("Longing at "  , pd.to_datetime(current_timestamp, unit='ms'))
        print(   cg.get_price(ids='bitcoin', vs_currencies='usd'))
        self.buy = 1, self.price
        self.take_profit = 1, self.price + 10

    def go_short(self):
        pass
