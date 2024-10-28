import os
import sys
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
from src.DiamondPricePrediction.utils.utils import load_object
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import customexception

class ModelEvaluation:
    def __init__(self):
        pass

    def eval_metrics(self, actual, pred, num_features=10):
        mse = mean_squared_error(actual, pred)
        rmse = np.sqrt(mse)
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        n = len(actual) 
        adj_r2 = 1 - (1 - r2) * (n - 1) / (n - num_features - 1)
        
        return mse, rmse, mae, r2, adj_r2

    def initiate_model_evaluation(self, train_array, test_array):
        try:
            X_test, y_test = test_array[:, :-1], test_array[:, -1]

            model_path = os.path.join("artifacts", "model.pkl")
            model = load_object(model_path)

            # Set MLflow tracking URI
            mlflow.set_registry_uri("https://dagshub.com/shelkekunal90/fsdsmendtoend.mlflow")
            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

            print(f"MLflow Tracking URL Scheme: {tracking_url_type_store}")

            with mlflow.start_run():
                predicted_qualities = model.predict(X_test)
                num_features = X_test.shape[1]  # Get number of features (columns) for Adjusted R^2 calculation
                mse, rmse, mae, r2, adj_r2 = self.eval_metrics(y_test, predicted_qualities, num_features)
                mlflow.log_metric("mse", mse)
                mlflow.log_metric("rmse", rmse)
                mlflow.log_metric("mae", mae)
                mlflow.log_metric("r2", r2)
                mlflow.log_metric("adjusted_r2", adj_r2)
                if tracking_url_type_store != "file":
                    mlflow.sklearn.log_model(model, "model", registered_model_name="ml_model")
                else:
                    mlflow.sklearn.log_model(model, "model")

        except Exception as e:
            logging.error(f"Error in model evaluation: {str(e)}")
            raise customexception(e, sys)

