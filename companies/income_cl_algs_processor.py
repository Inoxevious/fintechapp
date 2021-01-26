import json # will be needed for saving preprocessing details
import numpy as np # for data manipulation
import pandas as pd # for data manipulation
from sklearn.model_selection import train_test_split # will be used for data split
import requests
from apps.ml.income_classifier import random_forest as rf
from apps.ml.income_classifier import  extra_trees as et

from apps.endpoints.models import Endpoint
from apps.endpoints.serializers import EndpointSerializer

from apps.endpoints.models import MLAlgorithm
from apps.endpoints.serializers import MLAlgorithmSerializer

from apps.endpoints.models import MLAlgorithmStatus
from apps.endpoints.serializers import MLAlgorithmStatusSerializer

from apps.endpoints.models import MLRequest
from apps.endpoints.serializers import MLRequestSerializer
import json
from numpy.random import rand
from rest_framework import views, status
from rest_framework.response import Response
from apps.ml.registry import MLRegistry
from fintechapp.wsgi import registry
from django.db import transaction
from account.models import Clients, LoanOfficer, Loan, AccountUser
from companies.models import *


def ic_processor_algorithm_object(request):
    # algorithm_status = self.request.query_params.get("status", "production")
    algorithm_status = "production"
    # algorithm_version = self.request.query_params.get("version")
    algorithm_version = None
    endpoint_name = 'income_classifier'
    input_data = cust_data
    print("End point name found", endpoint_name)
    algs = MLAlgorithm.objects.filter(parent_endpoint__name = endpoint_name, ml_algorithm_status__status = algorithm_status, ml_algorithm_status__active=True)

    if algorithm_version is not None:
        algs = algs.filter(version = algorithm_version)

    if len(algs) == 0:
        return Response(
        {"status": "Error", "message": "ML algorithm is not available"},
    status=status.HTTP_400_BAD_REQUEST,
        )
    if len(algs) != 1 and algorithm_status != "ab_testing":
        return Response(
        {"status": "Error", "message": "ML algorithm selection is ambiguous. Please specify algorithm version."},
    status=status.HTTP_400_BAD_REQUEST,
        )
    alg_index = 0
    if algorithm_status == "ab_testing":
        alg_index = 0 if rand() < 0.5 else 1

    algorithm_object = registry.endpoints[algs[alg_index].id]
    return algorithm_object
