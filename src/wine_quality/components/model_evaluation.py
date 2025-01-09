import os
from pathlib import Path
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from urllib.parse import urlparse
import numpy as np
import joblib
from wine_quality.entity.config_entity import ModelEvaluationConfig
from wine_quality.utils.common import save_json

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluateMetrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    def saveResults(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        X_test = test_data.drop([self.config.target_column], axis = 1)
        y_test = test_data[self.config.target_column]

        predictions = model.predict(X_test)

        rmse, mae, r2 = self.evaluateMetrics(y_test, predictions)

        scores = {"rmse": rmse, "mae": mae, "r2_score": r2}
        save_json(path = Path(self.config.metric_file_name), data= scores)
