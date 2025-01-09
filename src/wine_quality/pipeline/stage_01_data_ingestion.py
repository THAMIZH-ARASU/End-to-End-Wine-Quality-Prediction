from wine_quality.config.configuration import ConfigurationManager
from wine_quality.components.data_ingestion import DataIngestion

STAGE_NAME = "Stage 1: Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.getDataIngestionConfig()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zipfile()
        