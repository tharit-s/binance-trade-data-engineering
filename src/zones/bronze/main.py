from bronze_module import FullLoadDataIngestion


if __name__ == "__main__":

    symbols = ["AAVEUSDT", "STXUSDT", "ARBUSDT"]

    for symbol in symbols:
        FullLoadDataIngestion(symbol=symbol, limit=10).write_trade_data_to_json()