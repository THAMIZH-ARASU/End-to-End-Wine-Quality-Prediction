from wine_quality.components.data_validation import DataValidation
from wine_quality.config.configuration import ConfigurationManager

STAGE_NAME = "Stage 2: Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.getDataValidationConfig()
        data_validation = DataValidation(data_validation_config)
        data_validation.validateAllColumns()
