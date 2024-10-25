import os
import sys
import pickle
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.DiamondPricePrediction.exception import customexception
from src.DiamondPricePrediction.logger import logging

def evaluate_model(X_train, y_train, X_test, y_test, models, params=None):
    report = {}

    try:
        for model_name, model in models.items():
            if params and model_name in params:
                # Perform hyperparameter tuning with GridSearchCV
                search = GridSearchCV(model, params[model_name], cv=5, n_jobs=-1, verbose=1)
                search.fit(X_train, y_train)
                model = search.best_estimator_
            else:
                # Train model without hyperparameter tuning
                model.fit(X_train, y_train)
            # Predict on test data
            y_pred = model.predict(X_test)
            # Evaluate model using R^2 score
            score = r2_score(y_test, y_pred)
            # Store model score
            report[model_name] = score

        return report

    except Exception as e:
        logging.error("Error during model evaluation")
        raise customexception(e, sys)

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise customexception(e, sys)

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.error("Exception occurred in load_object function")
        raise customexception(e, sys)
