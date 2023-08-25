from bronze_module import DataIngestion
from pathlib import Path
import os
from symbol_user_input_module import clean_symbols_with_user_input_and_default


symbols = clean_symbols_with_user_input_and_default()
print("Input: list of symbols:", symbols)
limit = 1000

MAIN_FOLDER = "datalakehouse"
INGESTION_FOLDER = "batch"
TARGET_ZONE_FOLDER = "bronze"

target_folder_path = os.path.join(
    Path(__file__).parents[3],
    MAIN_FOLDER,
    TARGET_ZONE_FOLDER,
    INGESTION_FOLDER
)

for symbol in symbols:
    data_ingestion = DataIngestion(
        symbol=symbol, 
        limit=limit, 
        target_folder_path=target_folder_path
        )
    data_ingestion.write_trade_data_to_json()

