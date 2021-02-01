# Package Imports
import pickle
import pandas as pd
import numpy as np
from sklearn import preprocessing
import joblib
import os
# from companies import dashboard
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)

class RiskAssessorClassifier:
    def __init__(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path_to_artifacts = os.path.join(BASE_DIR, 'algo_data/files/')
        self.values_fill_missing =  joblib.load(path_to_artifacts + "ra_train_mode.joblib")
        self.encoders = joblib.load(path_to_artifacts + "ra_encoders.joblib")
        self.model = joblib.load(path_to_artifacts + "ra_random_forest.joblib")
        # self.model = pickle.load(open('light_model.sav', 'rb'))

    def preprocessing(self, input_data):
# Read in data
        data_file = path_to_artifacts + 'application_train.csv'
        app_train = pd.read_csv(data_file).sort_values('SK_ID_CURR').reset_index(drop = True).loc[:1000000, :]
# Set an index
        app_train = app_train.set_index('SK_ID_CURR')
# Delete COLUMNS with very many NaNs, more than 40% of the observations in the column missing
        app_data = app_train.dropna(thresh = 45000, axis = 1)
# Subset numerical data
        numerics = ['int16','int32','int64','float16','float32','float64']
        numerical_vars = list(app_data.select_dtypes(include=numerics).columns)
        numerical_data = app_data[numerical_vars]
        
# Fill in missing values
        numerical_data = numerical_data.fillna(numerical_data.mean())
# Subset categorical data
        cates = ['object']
        cate_vars = list(app_data.select_dtypes(include=cates).columns)
        categorical_data = app_data[cate_vars]
# Fill in missing values
        categorical_data = categorical_data.fillna(method = 'ffill')

# Instantiate label encoder
        le = preprocessing.LabelEncoder()
        categorical_data = categorical_data.apply(lambda col: le.fit_transform(col).astype(str))
# Concat the data
        input_data = pd.concat([categorical_data, numerical_data], axis = 1)
        # Prepare test data for individual predictions
        input_data = clean_data.drop(['TARGET'], axis = 1)
        return input_data

    def predict(self, input_data):
        prob = self.model.predict_proba(input_data).tolist()[0]   #predict a client's probability of defaulting
        p = prob[1]
        return  p

    def postprocessing(p):
        label = 'high'
        if value > 0.67:
            label = 'high'
        elif value > 0.33:
            label = 'moderate'
        else:
            label = 'low'        
        return {"probability": value, "label": label, "status": "OK"}

    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            print("dta", input_data)
            prediction = self.predict(input_data)[0]  # only one sample
            prediction = self.postprocessing(prediction)
        except Exception as e:
            return {"status": "Error", "message": str(e)}

        return prediction