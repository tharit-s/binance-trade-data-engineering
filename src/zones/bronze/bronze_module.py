import binance
import json
from pathlib import Path
import os

class FullLoadDataIngestion:
    MAIN_FOLDER = "datalakehouse"
    ZONE_FOLDER = "bronze"
    INGESTION_FOLDER = "batch"

    def __init__(self, symbol, limit=None):
        self.symbol = symbol
        self.limit = limit
        self.client = binance.Client()

    def get_trade_data(self):
        return self.client.get_historical_trades(
            symbol=self.symbol,
            limit=self.limit
        )

    def get_target_path(self):
        return os.path.join(
            Path(__file__).parents[3],
            self.MAIN_FOLDER,
            self.ZONE_FOLDER,
            self.INGESTION_FOLDER,
            f"{self.symbol}.json"
        )

    def write_trade_data_to_json(self):
        with open(self.get_target_path(), "w") as f:
            json.dump(self.get_trade_data(), f)