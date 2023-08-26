import binance
import json
import os


class DataIngestion:

    def __init__(self, symbol, limit, target_folder_path):
        self.symbol = symbol
        self.limit = limit
        self.target_folder_path = target_folder_path
        self.client = binance.Client()

    def get_trade_data(self):
        try:
            return self.client.get_historical_trades(
                symbol=self.symbol,
                limit=self.limit
            )
        except binance.exceptions.BinanceAPIException as e:
            print(f"An error occurred while fetching trade data: {e}")
            return None
        except Exception as e:
            print(f"An unknown error occurred: {e}")
            return None

    def get_target_path(self):
        return os.path.join(
            self.target_folder_path,
            f"{self.symbol}.json"
        )

    def write_trade_data_to_json(self):
        trade_data = self.get_trade_data()
        if trade_data is not None:
            with open(self.get_target_path(), "w") as f:
                json.dump(trade_data, f)