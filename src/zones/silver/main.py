from silver_module import DataProcessor
import os


MAIN_FOLDER = "datalakehouse"
SOURCE_ZONE_FOLDER = "bronze"
INGESTION_FOLDER = "batch"

TARGET_ZONE_FOLDER = "silver"

data_processor = DataProcessor(
    source_folder=os.path.join(MAIN_FOLDER, SOURCE_ZONE_FOLDER, INGESTION_FOLDER),
    target_folder=os.path.join(MAIN_FOLDER, TARGET_ZONE_FOLDER, INGESTION_FOLDER)
)
data_processor.process_data()
