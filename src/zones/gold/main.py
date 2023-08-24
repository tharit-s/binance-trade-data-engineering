from gold_module import DataProcessor
from pathlib import Path
import os


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

data_processor = DataProcessor(
    source_folder_path=source_folder_path, 
    target_folder_path=target_folder_path
    )
data_processor.process_data()
