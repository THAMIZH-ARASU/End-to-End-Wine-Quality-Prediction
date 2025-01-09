from pathlib import Path
from wine_quality.components.model_evaluation import ModelEvaluation
from wine_quality.config.configuration import ConfigurationManager

STAGE_NAME = "Stage 5: Model Training stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.getModelEvaluationConfig()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.saveResults()