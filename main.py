from wine_quality import logger
from wine_quality.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from wine_quality.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from wine_quality.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from wine_quality.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from wine_quality.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Stage 01: Data Ingestion stage"
try:
    logger.info(f">>>>> Starting {STAGE_NAME} <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> Finished {STAGE_NAME} <<<<<\n\nx========================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Stage 02: Data Validation stage"
try:
    logger.info(f">>>>> Starting {STAGE_NAME} <<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>> Finished {STAGE_NAME} <<<<<\n\nx========================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Stage 03: Data Transformation stage"
try:
    logger.info(f">>>>> Starting {STAGE_NAME} <<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>> Finished {STAGE_NAME} <<<<<\n\nx========================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Stage 04: Model Training stage"
try:
    logger.info(f">>>>> Starting {STAGE_NAME} <<<<<")
    model_training = ModelTrainerTrainingPipeline()
    model_training.main()
    logger.info(f">>>>> Finished {STAGE_NAME} <<<<<\n\nx========================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Stage 05: Model Evaluation stage"
try:
    logger.info(f">>>>> Starting {STAGE_NAME} <<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.main()
    logger.info(f">>>>> Finished {STAGE_NAME} <<<<<\n\nx========================x")
except Exception as e:
    logger.exception(e)
    raise e