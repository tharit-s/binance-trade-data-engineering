from gold_module import DataProcessor
from pathlib import Path
import os
from minutely_interval_user_input_module import clean_minutely_interval_with_user_input
import visualize_module
import pandas as pd
from pathlib import Path


# Data Lakehouse
MAIN_FOLDER = "datalakehouse"
SOURCE_ZONE_FOLDER = "silver"
INGESTION_FOLDER = "batch"
TARGET_ZONE_FOLDER = "gold"

source_folder_path = os.path.join(
    Path(__file__).parents[3],
    MAIN_FOLDER,
    SOURCE_ZONE_FOLDER,
    INGESTION_FOLDER
)

target_folder_path = os.path.join(
    Path(__file__).parents[3],
    MAIN_FOLDER,
    TARGET_ZONE_FOLDER,
    INGESTION_FOLDER
)

ma_periods = [50, 100, 200]
ma_lower_position = 50
ma_upper_position = 100

data_processor = DataProcessor(
    source_folder_path=source_folder_path, 
    target_folder_path=target_folder_path,
    ma_periods=ma_periods,
    ma_lower_position=ma_lower_position,
    ma_upper_position=ma_upper_position
    )
data_processor.process_data()

# Data Visualization
minutely_interval = clean_minutely_interval_with_user_input()

if minutely_interval != '':
    MAIN_FOLDER = "datalakehouse"
    SOURCE_ZONE_FOLDER = "gold"
    INGESTION_FOLDER = "batch"

    source_folder_path = os.path.join(
        Path(__file__).parents[3],
        MAIN_FOLDER,
        SOURCE_ZONE_FOLDER,
        INGESTION_FOLDER
    )

    # Get a list of all the CSV files in the directory
    csv_files = [f for f in os.listdir(source_folder_path) if f.endswith('.csv')]

    # Create a list of DataFrames
    dfs = []

    # Read each CSV file into a DataFrame
    for csv in csv_files:
        df = pd.read_csv(os.path.join(source_folder_path, csv))
        dfs.append(df)

    # Concatenate the DataFrames into a single DataFrame
    df = pd.concat(dfs)

    # Visualize data
    visualize_module.create_visualization_ohlc_candle_stick(df, minutely_interval)
    visualize_module.create_visualization_ohlc_ma_and_position(df, minutely_interval)