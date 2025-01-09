import os
from wine_quality import logger
from sklearn.model_selection import train_test_split
import pandas as pd

from wine_quality.entity.config_entity import DataTransformationConfig

class DataTransformation:
    """
    This class shall be used to transform the raw data into test set and training set, assuming that the raw datat is already cleaned.
    NOTE: You can add more data transformation methods in this class if you need to. Such as scaling, encoding, PCA, etc.
          You can also perform all kinds of EDA in Machine Learning cycle here before passing the data to the Model.
    """
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def testTrainSplitting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into test and train
        train, test = train_test_split(data, test_size=0.2, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        logger.info("Data Transformation: Test Train Splitting is done.")
        logger.info(f"Train shape: {train.shape} \nTest shape: {test.shape}")

        print(train.shape)
        print(test.shape)