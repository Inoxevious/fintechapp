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
from rest_framework.views import APIView
from apps.ml.registry import MLRegistry
# from fintechapp.wsgi import registry
from django.db import transaction
from account.models import Clients, LoanOfficer, Loan, AccountUser
from companies.models import *
from django.forms.models import model_to_dict
from companies.models import Loan_History
# Create your views here.
from data_processor import imports as imp
from data_processor import logic as log
from datetime import datetime, date
from django.db.models import Sum
from apps.ml.income_classifier.random_forest import RandomForestClassifier
from apps.ml.income_classifier.extra_trees import ExtraTreesClassifier
from apps.ml.application_classifier.random_forest import RandomForestApplicationClassifier
from apps.ml.application_classifier.random_f import LoanApplicationClassifier

from django.http import JsonResponse

from rest_framework.generics import ListAPIView
from .serializers import Loan_HistorySerializers
from .models import Loan_History, IncomeData
from .pagination import StandardResultsSetPagination
from mergedeep import merge
from functools import reduce
from collections.abc import MutableMapping
from apps.ml.behavioral_scoring.random_f import BehavioralScoring 
from apps.ml.retent_scroring.random_f import  RetentionScoring
class GetPredictions:
    def __init__(self):
        global algorithm_object, prediction

    def get_application_scores(qry):

        prediction_data_dict = {}
        for ln in qry:
            if ApplicationScores.objects.filter(loan_id=ln.id).exists():
                prediction_data_dict = ApplicationScores.objects.filter(loan_id=ln.id)
            else:
                prediction_data_dict[ln.LOAN_ID] = []
                incomes_prediction = GetPredictions.get_income_pred(ln)
                application_prediction = GetPredictions.get_applications_pred(ln)
                prediction = merge(incomes_prediction, application_prediction)
                if ln.LOAN_ID == prediction["cust_id"]:
                    #result here as a probability
                    prediction['loan_amount'] = ln.AMT_CREDIT
                prediction_data_dict[ln.LOAN_ID].append(prediction)
        # print("predictions",prediction)
        return prediction_data_dict

    def get_retention_scores(qry):
        prediction_data_dict = {}
        for ln in qry:
            prediction_data_dict[ln.LOAN_ID] = []
            incomes_prediction = GetPredictions.get_retention_pred(ln)
            application_prediction = GetPredictions.get_applications_pred(ln)
            prediction = merge(incomes_prediction, application_prediction)
            if ln.LOAN_ID == prediction["cust_id"]:
                #result here as a probability
                prediction['loan_amount'] = ln.AMT_CREDIT
            prediction_data_dict[ln.LOAN_ID].append(prediction)
        # print("predictions",prediction)
        return prediction_data_dict

    def get_behavioral_scores(qry):
        prediction_data_dict = {}
        for ln in qry:
            prediction_data_dict[ln.LOAN_ID] = []
            incomes_prediction = GetPredictions.get_income_pred(ln)
            application_prediction = GetPredictions.get_behavioral_pred(ln)
            prediction = merge(incomes_prediction, application_prediction)
            if ln.LOAN_ID == prediction["cust_id"]:
                #result here as a probability
                prediction['loan_amount'] = ln.AMT_CREDIT
            prediction_data_dict[ln.LOAN_ID].append(prediction)
        # print("predictions",prediction)
        return prediction_data_dict

        
    def get_retention_pred(ln_id):
        algorithm_object = RandomForestClassifier()
        ln_cnt = IncomeData.objects.filter(LOAN_ID=ln_id.LOAN_ID).count()
        if ln_cnt == 0:
            retention_prediction = {}
            retention_prediction['recommendation_process'] = 'Client data missing'
            retention_prediction["classification"] = 'Client data missing'                
            retention_prediction["loan_num"] = 'Client data missing'
            retention_prediction["closure_date"] = 'Client data missing'
            retention_prediction["client_clv"] = 'Client data missing'
            retention_prediction["retention_color"] = 'Client data missing'
        else:
            ln = IncomeData.objects.get(LOAN_ID=ln_id.LOAN_ID)
            object_data_dict = {}
            object_data_dict[ln.LOAN_ID] = []
            data ={'age': ln.age, 'workclass': ln.workclass, 'fnlwgt': ln.fnlwgt, 'education': ln.education, 'education-num': ln.education_num, 'marital-status': ln.marital_status, 'occupation':ln.occupation, 'relationship': ln.relationship, 'race': ln.race, 'sex': ln.sex, 'capital-gain': ln.capital_gain, 'capital-loss': ln.capital_loss, 'hours-per-week': ln.hours_per_week, 'native-country': ln.native_country},
            object_data_dict[ln.LOAN_ID].append(data)
            retention_prediction = algorithm_object.compute_prediction(data)   
            retention_prediction["cust_id"] = ln.LOAN_ID
            predict_dict_data = {}
            if  retention_prediction['income_probability'] > 0.67:
                loan_num = 3
                closure_date = '28/02/2021'
                client_clv = "20"
                color = 'red'
                recommendation_process = "Reject client"
                classification = 'Reject'
                retention_prediction["classification"] = classification                
                retention_prediction["loan_num"] = loan_num
                retention_prediction["closure_date"] = closure_date
                retention_prediction["client_clv"] = client_clv
                retention_prediction["retention_color"] = color
                retention_prediction["recommendation_process"] = recommendation_process
            elif  retention_prediction['income_probability'] > 0.33:
                loan_num = 3
                closure_date = '28/02/2021'
                client_clv = "1100"
                color = 'blue'
                recommendation_process = "Visit business and home"
                classification = 'More detailed'
                retention_prediction["classification"] = classification                
                retention_prediction["loan_num"] = loan_num
                retention_prediction["closure_date"] = closure_date
                retention_prediction["client_clv"] = client_clv
                retention_prediction["retention_color"] = color
                retention_prediction["recommendation_process"] = recommendation_process
            else:
                loan_num = 3
                closure_date = '28/02/2021'
                client_clv = "2000"
                color = 'green'
                recommendation_process = "Automatic approval"
                classification = 'Pre-Approved'
                retention_prediction["classification"] = classification                
                retention_prediction["loan_num"] = loan_num
                retention_prediction["closure_date"] = closure_date
                retention_prediction["client_clv"] = client_clv
                retention_prediction["retention_color"] = color
                retention_prediction["recommendation_process"] = recommendation_process

        return retention_prediction



    def get_income_pred(ln_id):
        algorithm_object = RandomForestClassifier()
        ln_cnt = IncomeData.objects.filter(LOAN_ID=ln_id.LOAN_ID).count()
        print("Income qrty", ln_cnt)
        if ln_cnt == 0:
            incomes_prediction = {}
            incomes_prediction['income_text'] = 'No income data for this client'
        else:
            ln = IncomeData.objects.get(LOAN_ID=ln_id.LOAN_ID)
            print("Income qrty", ln)
            object_data_dict = {}
            object_data_dict[ln.LOAN_ID] = []
            data ={'age': ln.age, 'workclass': ln.workclass, 'fnlwgt': ln.fnlwgt, 'education': ln.education, 'education-num': ln.education_num, 'marital-status': ln.marital_status, 'occupation':ln.occupation, 'relationship': ln.relationship, 'race': ln.race, 'sex': ln.sex, 'capital-gain': ln.capital_gain, 'capital-loss': ln.capital_loss, 'hours-per-week': ln.hours_per_week, 'native-country': ln.native_country},
            object_data_dict[ln.LOAN_ID].append(data)
            print("incomes_prediction data", data)
            incomes_prediction = algorithm_object.compute_prediction(data)   
            print("incomes_prediction respo", incomes_prediction)
            incomes_prediction["cust_id"] = ln.LOAN_ID
            predict_dict_data = {}
            if  incomes_prediction['income_probability'] > 0.67:
                color = 'red'
                text = 'high risk'
                incomes_prediction["income_color"] = color
                incomes_prediction["income_text"] = text
            elif  incomes_prediction['income_probability'] > 0.33:
                color = 'blue'
                text = 'moderate risk'
                incomes_prediction["income_color"] = color
                incomes_prediction["income_text"] = text
            else:
                color = 'green'
                text = 'low risk'
                incomes_prediction["income_color"] = color
                incomes_prediction["income_text"] = text

        return incomes_prediction



    def get_applications_pred(ln):
        algorithm_object = LoanApplicationClassifier()
        applications_prediction = algorithm_object.compute_prediction(model_to_dict(ln))
        applications_prediction["cust_id"] = ln.LOAN_ID
        if  applications_prediction['application_probability'] > 0.67:
            color = 'red'
            text = 'high risk'
            applications_prediction["application_color"] = color
            applications_prediction["application_text"] = text
        elif  applications_prediction['application_probability'] > 0.33:
            color = 'blue'
            text = 'moderate risk'
            applications_prediction["application_color"] = color
            applications_prediction["application_text"] = text
        else:
            color = 'green'
            text = 'low risk'
            applications_prediction["application_color"] = color
            applications_prediction["application_text"] = text

        return applications_prediction

    def get_behavioral_pred(ln):
        algorithm_object = BehavioralScoring()
        print("data to bh  model", model_to_dict(ln))
        behavioral_prediction = algorithm_object.compute_prediction(model_to_dict(ln))
        behavioral_prediction["cust_id"] = ln.LOAN_ID
        if  behavioral_prediction['behavioral_probability'] > 0.67:
            color = 'red'
            text = 'high risk'
            time = '7 days'
            contact_channel = 'phone'
            contact_schedule = '08/02/2021'
            message = " C'mon, use your brains"
            behavioral_prediction["behavioral_color"] = color
            behavioral_prediction["behavioral_text"] = text
            behavioral_prediction["behavioral_time_to_default"] = time
            behavioral_prediction["behavioral_contact_channel"] = contact_channel
            behavioral_prediction["behavioral_contact_schedule"] = contact_schedule
            behavioral_prediction["behavioral_message"] = message
        elif  behavioral_prediction['behavioral_probability'] > 0.33:
            color = 'blue'
            text = 'moderate risk'
            time = '21 days'
            contact_channel = 'phone'
            contact_schedule = '28/02/2021'
            message = " C'mon, use your brains"
            behavioral_prediction["behavioral_color"] = color
            behavioral_prediction["behavioral_text"] = text
            behavioral_prediction["behavioral_time_to_default"] = time
            behavioral_prediction["behavioral_contact_channel"] = contact_channel
            behavioral_prediction["behavioral_contact_schedule"] = contact_schedule
            behavioral_prediction["behavioral_message"] = message
        else:
            color = 'green'
            text = 'low risk'
            time = '48 days'
            contact_channel = 'phone'
            contact_schedule = '08/04/2021'
            message = " C'mon, use your brains"
            behavioral_prediction["behavioral_color"] = color
            behavioral_prediction["behavioral_text"] = text
            behavioral_prediction["behavioral_time_to_default"] = time
            behavioral_prediction["behavioral_contact_channel"] = contact_channel
            behavioral_prediction["behavioral_contact_schedule"] = contact_schedule
            behavioral_prediction["behavioral_message"] = message

        return behavioral_prediction

    def merge(a, b, path=None, update=True):
        "http://stackoverflow.com/questions/7204805/python-dictionaries-of-dictionaries-merge"
        "merges b into a"
        if path is None: path = []
        for key in b:
            if key in a:
                if isinstance(a[key], dict) and isinstance(b[key], dict):
                    merge(a[key], b[key], path + [str(key)])
                elif a[key] == b[key]:
                    pass # same leaf value
                elif isinstance(a[key], list) and isinstance(b[key], list):
                    for idx, val in enumerate(b[key]):
                        a[key][idx] = merge(a[key][idx], b[key][idx], path + [str(key), str(idx)], update=update)
                elif update:
                    a[key] = b[key]
                else:
                    raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
            else:
                a[key] = b[key]
        return a

    def rec_merge(d1, d2):
        '''
        Update two dicts of dicts recursively, 
        if either mapping has leaves that are non-dicts, 
        the second's leaf overwrites the first's.
        '''
        for k, v in d1.items():
            if k in d2:
                # this next check is the only difference!
                if all(isinstance(e, MutableMapping) for e in (v, d2[k])):
                    d2[k] = rec_merge(v, d2[k])
                # we could further check types and merge as appropriate here.
        d3 = d1.copy()
        d3.update(d2)
        return d3