from dataclasses import dataclass
import os
import sys
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from src.DiamondPricePrediction.utils.utils import save_object
from src.DiamondPricePrediction.logger import logging
from src.DiamondPricePrediction.exception import customexception
from src.DiamondPricePrediction.utils.utils import evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_training(self, train_array, test_array):
        try:
            logging.info('Splitting Dependent and Independent variables from train and test data')
            X_train, y_train, X_test, y_test = (train_array[:, :-1],train_array[:, -1],
                                                test_array[:, :-1],test_array[:, -1])

            # List of models to evaluate
            models = {
                'LinearRegression': LinearRegression(),
                'Lasso': Lasso(),
                'Ridge': Ridge(),
                'ElasticNet': ElasticNet(),
                'DecisionTreeRegressor': DecisionTreeRegressor(),
                'RandomForestRegressor': RandomForestRegressor(),
                'XGBRegressor': XGBRegressor()
            }
            # Hyperparameter tuning for RandomForest and XGBoost
            params = {'RandomForestRegressor': {
                        'n_estimators': [100, 200],
                        'max_depth': [10, 20],
                        'min_samples_split': [2, 5]},
                      'XGBRegressor': {
                        'learning_rate': [0.01, 0.1],
                        'n_estimators': [100, 200],
                        'max_depth': [3, 5]}}

            # Evaluate models using the evaluate_model utility
            model_report: dict = evaluate_model(X_train, y_train, X_test, y_test, models, params)

            print(model_report)
            print('\n====================================================================================\n')
            logging.info(f'Model Report : {model_report}')

            # Get the best model based on the highest R2 score
            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]

            print(f'Best Model Found, Model Name: {best_model_name}, R2 Score: {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found, Model Name: {best_model_name}, R2 Score: {best_model_score}')
            best_model.fit(X_train,y_train)
            # Save the best model
            save_object(file_path=self.model_trainer_config.trained_model_file_path,obj=best_model)

        except Exception as e:
            logging.info('Exception occurred during Model Training')
            raise customexception(e, sys)