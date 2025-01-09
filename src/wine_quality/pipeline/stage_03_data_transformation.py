from pathlib import Path
from wine_quality.components.data_tranformation import DataTransformation
from wine_quality.config.configuration import ConfigurationManager

STAGE_NAME = "Stage 3: Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def run(self):
        config = ConfigurationManager()
        data_transformation_config = config.getDataTransformationConfig()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.testTrainSplitting()

    def main(self):
        try:
            with open(Path('artifacts/data_validation/status.txt'), 'r') as f:
                status = f.read().split(' ')[-1]
            if status == 'True':
                self.run()
            else:
                raise Exception("Data Validation stage failed: Your data schema is not valid")
        except Exception as e:
            print(e)