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
        return self.client.get_historical_trades(
            symbol=self.symbol,
            limit=self.limit
        )

    def get_target_path(self):
        return os.path.join(
            self.target_folder_path,
            f"{self.symbol}.json"
        )

    def write_trade_data_to_json(self):
        with open(self.get_target_path(), "w") as f:
            json.dump(self.get_trade_data(), f)