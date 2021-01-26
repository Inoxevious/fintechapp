from django.shortcuts import render
from django.contrib.postgres.aggregates import StringAgg
from django.contrib.postgres.search import (
    SearchQuery, SearchRank, SearchVector, TrigramSimilarity,
)

from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q, F
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.core.paginator import Paginator
import csv
from io import StringIO
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files import File
from django.http import HttpResponse, StreamingHttpResponse
from django.utils.text import slugify
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
# Create your views here.

class IncomeClassfierResultsView(ListView):
   
    template_name = 'dashboards/rf/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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
        
        prediction = algorithm_object.compute_prediction(input_data)
        print("Predictions", prediction)


        label = prediction["label"] if "label" in prediction else "error"
        json
        ml_request = MLRequest(
            input_data=input_data,
            full_response=prediction,
            response=label,
            feedback="",
            parent_mlalgorithm=algs[alg_index],
        )
        ml_request.save()

        prediction["request_id"] = ml_request.id
        print("Predictions reqq", prediction)

        # return Response(prediction)
        context['income_classifier_prediction'] = prediction
        

        return context


def index(request):
    return render(request,'dashboards/landing/index.html')

def application_analytics(request):
    org = Organization.objects.get(id=1)
    client = Clients.objects.filter(insti=org)
    loan = Loan.objects.filter(signing_officer__insti = org)
    totaldict = {}

        

    context = {'client':loan}

    return render(request,'dashboards/application/index.html', context)


def behavioral_analytics(request):
    return render(request,'dashboards/behavioral/index.html')


def retention_analytics(request):
    return render(request,'dashboards/retention/index.html')


def profile(request):
    return render(request,'dashboards/profile/index.html')

def reports(request):
    return render(request,'dashboards/reports/index.html')

def articles(request):
    return render(request,'dashboards/articles/index.html')