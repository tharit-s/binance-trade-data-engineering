import pandas as pd
import os


class DataProcessor:
    def __init__(self, source_folder_path, target_folder_path, ma_periods=[50, 100, 200], ma_lower_position=50, ma_upper_position=100):
        self.source_folder_path = source_folder_path
        self.target_folder_path = target_folder_path
        self.ma_periods = ma_periods
        self.ma_lower_position = ma_lower_position
        self.ma_upper_position = ma_upper_position
        pd.set_option("display.max_columns", 100)

    def process_data(self):
        csv_files = os.listdir(self.source_folder_path)

        for csv_file in csv_files:
            df_temp = pd.read_csv(os.path.join(self.source_folder_path, csv_file))
            df_ma = self.calculate_moving_averages(df_temp, self.ma_periods)
            df_ma_positions = self.calculate_positions(df_ma, self.ma_lower_position, self.ma_upper_position)

            target_path = os.path.join(self.target_folder_path, csv_file)
            df_ma_positions.to_csv(target_path, index=False)

    @staticmethod
    def calculate_moving_averages(df, ma_periods):
        df_ma = df.copy()

        for ma_period in ma_periods:
            df_ma[f'ma{ma_period}'] = df_ma['close'].rolling(window=ma_period, min_periods=1).mean()

        return df_ma
    
    @staticmethod
    def calculate_positions(df, ma_lower_position, ma_upper_position):
        df_positions = df.copy()
        df_positions['position'] = "HOLD"

        for i in range(0, len(df_positions)):
            if df_positions.at[i, f'ma{ma_lower_position}'] < df_positions.at[i, f'ma{ma_upper_position}']:
                df_positions.at[i, 'position'] = "BUY"
            elif df_positions.at[i, f'ma{ma_lower_position}'] >= df_positions.at[i, f'ma{ma_upper_position}']:
                df_positions.at[i, 'position'] = "SELL"

        return df_positions
