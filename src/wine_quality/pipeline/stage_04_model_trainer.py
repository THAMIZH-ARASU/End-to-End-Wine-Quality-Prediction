from pathlib import Path
from wine_quality.components.model_trainer import ModelTrainer
from wine_quality.config.configuration import ConfigurationManager

STAGE_NAME = "Stage 4: Model Training stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.getModelTrainerConfig()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()