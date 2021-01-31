"""
WSGI config for fintechapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fintechapp.settings')

application = get_wsgi_application()

# ML registry
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.income_classifier.random_forest import RandomForestClassifier
from apps.ml.income_classifier.extra_trees import ExtraTreesClassifier # import ExtraTrees ML algorithm
<<<<<<< HEAD
from apps.ml.risk_assessor.risk_assessor import RiskAssessorClassifier
try:
    print("Adding ML algorithms to registry")
=======

try:
>>>>>>> fe2c9bd2d5d9d693e3b134dfde94bb3dc2d99c4d
    registry = MLRegistry() # create ML registry
    # Random Forest classifier
    rf = RandomForestClassifier()
    # add to ML registry
    registry.add_algorithm(endpoint_name="income_classifier",
                            algorithm_object=rf,
                            algorithm_name="random forest",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Piotr",
                            algorithm_description="Random Forest with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(RandomForestClassifier))




    # Extra Trees classifier
    et = ExtraTreesClassifier()
    # add to ML registry
<<<<<<< HEAD

    registry.add_algorithm(endpoint_name="income_classifier",
                            algorithm_object=et,
                            algorithm_name="extra trees",
                            algorithm_status="production",
=======
    registry.add_algorithm(endpoint_name="income_classifier",
                            algorithm_object=et,
                            algorithm_name="extra trees",
                            algorithm_status="testing",
>>>>>>> fe2c9bd2d5d9d693e3b134dfde94bb3dc2d99c4d
                            algorithm_version="0.0.1",
                            owner="Piotr",
                            algorithm_description="Extra Trees with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(RandomForestClassifier))
<<<<<<< HEAD

    #Risk Assessor
    
    ra = RiskAssessorClassifier()
    registry.add_algorithm(endpoint_name="risk_assessor",
                            algorithm_object=ra,
                            algorithm_name="cust applied risk",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Dreatol",
                            algorithm_description="Custom applic with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(RiskAssessorClassifier))
    print("Added ML algorithms to registry")
=======
>>>>>>> fe2c9bd2d5d9d693e3b134dfde94bb3dc2d99c4d
except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))