import os
from pathlib import Path
import urllib.request as request
import zipfile
from wine_quality import logger
from wine_quality.entity.config_entity import DataIngestionConfig
from wine_quality.utils.common import get_size

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        # Ensure the parent directory exists
        os.makedirs(os.path.dirname(self.config.local_file_name), exist_ok=True)

        if not os.path.exists(self.config.local_file_name):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_file_name
            )
            logger.info(f"File downloaded: {filename} \nWith following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_file_name))}")
            
    def extract_zipfile(self):
        """
        zip_file_path: str
        Extracts the zip file to the specified directory
        Function return None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_file_name, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)