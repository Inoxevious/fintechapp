from django.test import TestCase
from apps.ml.income_classifier.random_forest import RandomForestClassifier
from apps.ml.risk_assessor.risk_assessor import RiskAssessorClassifier
from apps.ml.income_classifier.extra_trees import ExtraTreesClassifier
import inspect
from apps.ml.registry import MLRegistry
from rest_framework.test import APIClient


class MLTests(TestCase):
    def test_rf_algorithm(self):
        input_data = {
            "age": 37,
            "workclass": "Private",
            "fnlwgt": 34146,
            "education": "HS-grad",
            "education-num": 9,
            "marital-status": "Married-civ-spouse",
            "occupation": "Craft-repair",
            "relationship": "Husband",
            "race": "White",
            "sex": "Male",
            "capital-gain": 0,
            "capital-loss": 0,
            "hours-per-week": 68,
            "native-country": "United-States"
        }
        my_alg = RandomForestClassifier()
        response = my_alg.compute_prediction(input_data)
        self.assertEqual('OK', response['status'])
        self.assertTrue('label' in response)
        self.assertEqual('<=50K', response['label'])


    # add below method to MLTests class:
        def test_registry(self):
            registry = MLRegistry()
            self.assertEqual(len(registry.endpoints), 0)
            endpoint_name = "income_classifier"
            algorithm_object = RandomForestClassifier()
            algorithm_name = "random forest"
            algorithm_status = "production"
            algorithm_version = "0.0.1"
            algorithm_owner = "Piotr"
            algorithm_description = "Random Forest with simple pre- and post-processing"
            algorithm_code = inspect.getsource(RandomForestClassifier)
            # add to registry
            registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                        algorithm_status, algorithm_version, algorithm_owner,
                        algorithm_description, algorithm_code)
            # there should be one endpoint available
            self.assertEqual(len(registry.endpoints), 1)

        def test_et_algorithm(self):
                input_data = {
                    "age": 37,
                    "workclass": "Private",
                    "fnlwgt": 34146,
                    "education": "HS-grad",
                    "education-num": 9,
                    "marital-status": "Married-civ-spouse",
                    "occupation": "Craft-repair",
                    "relationship": "Husband",
                    "race": "White",
                    "sex": "Male",
                    "capital-gain": 0,
                    "capital-loss": 0,
                    "hours-per-week": 68,
                    "native-country": "United-States"
                }
                my_alg = ExtraTreesClassifier()
                response = my_alg.compute_prediction(input_data)
                self.assertEqual('OK', response['status'])
                self.assertTrue('label' in response)
<<<<<<< HEAD
                self.assertEqual('<=50K', response['label'])

class MLTests(TestCase):
    def test_ra_algorithm(self):
        input_data = {"CODE_GENDER": "F",
                    "FLAG_OWN_CAR": "N",
                    "FLAG_OWN_REALTY": "Y",
                    "AMT_INCOME_TOTAL": 135000.0,
                    "AMT_CREDIT": 450000.0,
                    "AMT_ANNUITY": 9000.0,
                    "NAME_INCOME_TYPE": "Working",
                    "NAME_EDUCATION_TYPE": "Secondary / secondary special",
                    "NAME_FAMILY_STATUS": "Married",
                    "NAME_HOUSING_TYPE": "House / apartment",
                    "DAYS_BIRTH": -18248.0,
                    "DAYS_EMPLOYED": 365243.0,
                    "DAYS_ID_PUBLISH": -4033.0,
                    "FLAG_MOBIL": 1.0,
                    "FLAG_EMP_PHONE": 1.0,
                    "FLAG_WORK_PHONE": 0.0,
                    "FLAG_CONT_MOBILE": 1.0,
                    "FLAG_PHONE": 0.0,
                    "FLAG_EMAIL": 0.0,
                    "OCCUPATION_TYPE": "UNKNOWN",
                    "CNT_FAM_MEMBERS": 2.0,
                    "EXT_SOURCE_1": 0.0,
                    "EXT_SOURCE_2": 0.0,
                    "EXT_SOURCE_3": 0.0,
                    "OBS_30_CNT_SOCIAL_CIRCLE": 0.0,
                    "DEF_30_CNT_SOCIAL_CIRCLE": 0.0,
                    "OBS_60_CNT_SOCIAL_CIRCLE": 0.0,
                    "DEF_60_CNT_SOCIAL_CIRCLE": 0.0,
                    "DAYS_LAST_PHONE_CHANGE": 0.0,
                    "FLAG_DOCUMENT_2": 0.0,
                    "FLAG_DOCUMENT_3": 1.0,
                    "FLAG_DOCUMENT_4": 0.0,
                    "FLAG_DOCUMENT_5": 0.0,
                    "FLAG_DOCUMENT_6": 0.0,
                    "FLAG_DOCUMENT_7": 0.0,
                    "FLAG_DOCUMENT_8": 0.0,
                    "FLAG_DOCUMENT_9": 0.0,
                    "FLAG_DOCUMENT_10": 0.0,
                    "FLAG_DOCUMENT_11": 0.0,
                    "FLAG_DOCUMENT_12": 0.0,
                    "FLAG_DOCUMENT_13": 0.0,
                    "FLAG_DOCUMENT_14": 0.0,
                    "FLAG_DOCUMENT_15": 0.0,
                    "FLAG_DOCUMENT_16": 0.0,
                    "FLAG_DOCUMENT_17": 0.0,
                    "FLAG_DOCUMENT_18": 0.0,
                    "FLAG_DOCUMENT_19": 0.0,
                    "FLAG_DOCUMENT_20": 0.0,
                    "FLAG_DOCUMENT_21": 0.0,
                    "AMT_REQ_CREDIT_BUREAU_HOUR": 0.0,
                    "AMT_REQ_CREDIT_BUREAU_DAY": 0.0,
                    "AMT_REQ_CREDIT_BUREAU_WEEK": 0.0,
                    "AMT_REQ_CREDIT_BUREAU_MON": 0.0,
                    "AMT_REQ_CREDIT_BUREAU_QRT": 0.0,
                    "AMT_REQ_CREDIT_BUREAU_YEAR": 0.0,
                    "TARGET": 0}

        my_alg = RiskAssessorClassifier()
        response = my_alg.compute_prediction(input_data)
        self.assertTrue('label' in response)
=======
                self.assertEqual('<=50K', response['label'])
>>>>>>> fe2c9bd2d5d9d693e3b134dfde94bb3dc2d99c4d
