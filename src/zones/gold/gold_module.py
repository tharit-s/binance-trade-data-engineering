import pandas as pd
import os

class DataProcessor:
    def __init__(self, source_folder_path, target_folder_path, periods=[50, 100, 200]):
        self.source_folder_path = source_folder_path
        self.target_folder_path = target_folder_path
        self.periods = periods
        pd.set_option("display.max_columns", 100)

    def process_data(self):
        csv_files = os.listdir(self.source_folder_path)

        for csv_file in csv_files:
            csv_filename = csv_file.split(".csv")[0]
            df_temp = pd.read_csv(os.path.join(self.source_folder_path, csv_file))
            df_ma = self.calculate_moving_averages(df_temp, self.periods)

            target_path = os.path.join(self.target_folder_path, csv_file)
            df_ma.to_csv(target_path)

    @staticmethod
    def calculate_moving_averages(df, periods):
        df_ma = df.copy()

        for period in periods:
            df_ma[f'ma{period}'] = df_ma['close'].rolling(window=period, min_periods=1).mean()

        return df_ma
