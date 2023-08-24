import pandas as pd
import os


class DataProcessor:
    def __init__(self, source_folder_path, target_folder_path):
        self.source_folder_path = source_folder_path
        self.target_folder_path = target_folder_path
        pd.set_option("display.max_columns", 100)

    def process_data(self):
        json_files = os.listdir(self.source_folder_path)

        for json_file in json_files:
            json_filename = json_file.split(".json")[0]
            
            df_temp = pd.read_json(f"{self.source_folder_path}/{json_file}")
            df_temp['minute'] = df_temp['time'] // 60000
            df_temp['time'] = pd.to_datetime(df_temp['time'], unit='ms', errors='coerce')
            df_temp['open'] = df_temp.groupby('minute')['price'].transform('first')
            df_temp['high'] = df_temp.groupby('minute')['price'].transform('max')
            df_temp['low'] = df_temp.groupby('minute')['price'].transform('min')
            df_temp['close'] = df_temp.groupby('minute')['price'].transform('last')
            df_temp['volume'] = df_temp.groupby('minute')['qty'].transform('sum')
            df_temp.set_index('time', inplace=True)

            minutely_intervals = [1, 5, 15, 30, 60]
            
            for minutely_interval in minutely_intervals:
                target_path = os.path.join(
                    self.target_folder_path,
                    f"{json_filename}_minutely_{minutely_interval}.csv"
                )
                
                df_ohlcv = self.calculate_ohlcv(df_temp, minutely_interval)
                df_ohlcv["filename"] = json_file
                df_ohlcv["coin"] = json_filename
                df_ohlcv["minutelyInterval"] = minutely_interval

                df_ohlcv.to_csv(target_path)
    
    @staticmethod
    def calculate_ohlcv(df, minutely_interval):
        df_ohlcv = df.resample(f'{minutely_interval}T').agg({
            'open': 'first',
            'high': 'max',
            'low': 'min',
            'close': 'last',
            'volume': 'sum'
        })
        return df_ohlcv
