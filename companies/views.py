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

from django.http import JsonResponse

from rest_framework.generics import ListAPIView
from .serializers import Loan_HistorySerializers
from .models import Loan_History
from .pagination import StandardResultsSetPagination



class Loan_HistoryListing(ListAPIView):
    # set the pagination and serializer class

	pagination_class = StandardResultsSetPagination
	serializer_class = Loan_HistorySerializers

	def get_queryset(self):
        # filter the queryset based on the filters applied

		queryList = Loan_History.objects.all()
        #dummy for business filter is NAME_INCOME_TYPE
		NAME_INCOME_TYPE = self.request.query_params.get('business', None)

		ORGANIZATION_TYPE = self.request.query_params.get('mortage', None)
		OCCUPATION_TYPE = self.request.query_params.get('funeral', None)
		CODE_GENDER = self.request.query_params.get('school', None)
		sort_by = self.request.query_params.get('sort_by', None)

		if NAME_INCOME_TYPE:
		    queryList = queryList.filter(NAME_INCOME_TYPE = NAME_INCOME_TYPE)

		if ORGANIZATION_TYPE:
		    queryList = queryList.filter(ORGANIZATION_TYPE = ORGANIZATION_TYPE)

		if OCCUPATION_TYPE:
		    queryList = queryList.filter(OCCUPATION_TYPE = OCCUPATION_TYPE)
		if CODE_GENDER:
		    queryList = queryList.filter(CODE_GENDER = CODE_GENDER)    

        # sort it if applied on based on price/points

		if sort_by == "income":
		    queryList = queryList.order_by("AMT_INCOME_TOTAL")
		elif sort_by == "credit_amount":
		    queryList = queryList.order_by("AMT_CREDIT")
		return queryList

#Get Business Loan Filter
def getBusiness(request):
    # get all the business loans from the database excluding 
    # null and blank values

    if request.method == "GET" and request.is_ajax():
        business = Loan_History.objects.exclude(NAME_INCOME_TYPE__isnull=True).\
            exclude(NAME_INCOME_TYPE__exact='').order_by('NAME_INCOME_TYPE').values_list('NAME_INCOME_TYPE').distinct()
        business = [i[0] for i in list(business)]
        data = {
            "business": business, 
        }
        return JsonResponse(data, status = 200)

#Get mortage Loan Filter
def getMortage(request):
    # get all the mortage loans from the database excluding 
    # null and blank values

    if request.method == "GET" and request.is_ajax():
        mortage = Loan_History.objects.exclude(ORGANIZATION_TYPE__isnull=True).\
            exclude(ORGANIZATION_TYPE__exact='').order_by('ORGANIZATION_TYPE').values_list('ORGANIZATION_TYPE').distinct()
        mortage = [i[0] for i in list(mortage)]
        data = {
            "mortage": mortage, 
        }
        return JsonResponse(data, status = 200)

#Get funeral Loan Filter
def getFuneral(request):
    # get all the funeral loans from the database excluding 
    # null and blank values

    if request.method == "GET" and request.is_ajax():
        funeral = Loan_History.objects.exclude(OCCUPATION_TYPE__isnull=True).\
            exclude(OCCUPATION_TYPE__exact='').order_by('OCCUPATION_TYPE').values_list('OCCUPATION_TYPE').distinct()
        funeral = [i[0] for i in list(funeral)]
        data = {
            "funeral": funeral, 
        }
        return JsonResponse(data, status = 200)


#Get mortage Loan Filter
def getSchool(request):
    # get all the school loans from the database excluding 
    # null and blank values

    if request.method == "GET" and request.is_ajax():
        school = Loan_History.objects.exclude(ORGANIZATION_TYPE__isnull=True).\
            exclude(ORGANIZATION_TYPE__exact='').order_by('ORGANIZATION_TYPE').values_list('ORGANIZATION_TYPE').distinct()
        school = [i[0] for i in list(school)]
        data = {
            "school": school, 
        }
        return JsonResponse(data, status = 200)




def data_aggretation(request):
    labels = []
    data = []
    queryset =  Loan_History.objects.values('OCCUPATION_TYPE').annotate(amount_borrowed=Sum('AMT_CREDIT')).order_by('-amount_borrowed')
    print("QRYSET", queryset)
    for entry in queryset:
        labels.append(entry['OCCUPATION_TYPE'])
        data.append(entry['amount_borrowed'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
class HomeView(ListView):
    template_name = 'dashboards/landing/index.html'
    def get_queryset(self, **kwargs):
        global cust_data, loan, user_name, input_data,acc_user, time
        user = self.request.user
        time = end = datetime.today()
        print("TIME", time)
        user_name = user.first_name
        acc_user = AccountUser.objects.get(user=user)
        print("Found USer", user_name)
        org = Organization.objects.get(id=1)
        client = Clients.objects.filter(insti=org)
        loan = Loan.objects.filter(signing_officer__insti = org)
        application_data = Loan_History.objects.all()
        print("loan application_data loan", loan)

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)

        # algorithm_status = self.request.query_params.get("status", "production")
        algorithm_status = "production"
        # algorithm_version = self.request.query_params.get("version")
        algorithm_version = None
        endpoint_name = 'income_classifier'
        print("End point name found", endpoint_name)
        if endpoint_name == 'income_classifier':
            algorithm_object = RandomForestClassifier()
        elif endpoint_name == 'application_classifier':
            algorithm_object = RandomForestApplicationClassifier()

        # prediction = algorithm_object.compute_prediction(request.data)
        algs = MLAlgorithm.objects.get(parent_endpoint__name = endpoint_name)
        query_object_data_dict ={}
        for ln in loan:
            query_object_data_dict[ln.client_id] = []
            query_object_data_dict[ln.client_id].append(model_to_dict(ln))
        print("query object data", query_object_data_dict)
        # qury_predict_dict_data = {}
        # for d_id, d_info in query_object_data_dict.items():
        #     print("\nQuery Data ID:", d_id)
        #     for key in d_info:
        #         qury_predict_dict_data[d_id] = []
                
        #         print(key) 
        #         prediction = algorithm_object.compute_prediction(key)
        #         qury_predict_dict_data[d_id].append(prediction)
        #     print("Query  Predictions data", qury_predict_dict_data)
        object_data_dict = {}
        for ln in loan:
            object_data_dict[ln.client_id] = []
            data ={'age': 32, 'workclass': 'Private', 'fnlwgt': 70984, 'education': 'Assoc-voc', 'education-num': 11, 'marital-status': 'Married-civ-spouse', 'occupation': 'Machine-op-inspct', 'relationship': 'Husband', 'race': 'White', 'sex': 'Male', 'capital-gain': 0, 'capital-loss': 0, 'hours-per-week': 40, 'native-country': 'United-States'},
            object_data_dict[ln.client_id].append(data)
            print("object data", object_data_dict)

        predict_dict_data = {}
        for d_id, d_info in object_data_dict.items():
            print("\nQuery Data ID:", d_id)
            for key in d_info:
                predict_dict_data[d_id] = []
                input_data = key
                print("Key value", key)
                # prediction here
                prediction = algorithm_object.compute_prediction(key)
                print("Prediction Error",prediction )
                prediction["cust_id"] = d_id #result here as a probability
                # print(prediction['probability'])
                if  prediction['probability'] > 0.67:
                    color = 'red'
                    text = 'high risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a high risk of defaulting the loan'.format(d_id))
                elif  prediction['probability'] > 0.33:
                    color = 'blue'
                    text = 'moderate risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a moderate risk of defaulting the loan'.format(d_id))
                else:
                    color = 'green'
                    text = 'low risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a low risk of defaulting the loan'.format(d_id))
                predict_dict_data[d_id].append(prediction)
            print( 'Prediction:', predict_dict_data)


        label = prediction["label"] if "label" in prediction else "error"
        ml_request = MLRequest(
            input_data=input_data,
            full_response=prediction,
            response=label,
            feedback="",
            parent_mlalgorithm=algs,
        )
        ml_request.save()



        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Chart JS Data~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        data = Loan_History.objects.all()
        return_data = log.grade_avg(data)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~Chart JS Data End ~~~~~~~~~~~~~~~~~~~~~~
        prediction["request_id"] = ml_request.id
        context = {
            'income_classifier_prediction': predict_dict_data,
            'loan': loan,
            'user_name':user_name,
            'acc_user':acc_user,
            'webdata':return_data
        }
        return context





class IncomeClassfierResultsView(ListView):
    template_name = 'dashboards/rf/index.html'
    def get_queryset(self, **kwargs):
        global cust_data, loan, user_name, input_data,acc_user
        user = self.request.user
        user_name = user.first_name
        acc_user = AccountUser.objects.get(user=user)
        print("Found USer", user_name)
        org = Organization.objects.get(id=1)
        client = Clients.objects.filter(insti=org)
        loan = Loan.objects.filter(signing_officer__insti = org)

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)

        # algorithm_status = self.request.query_params.get("status", "production")
        algorithm_status = "production"
        # algorithm_version = self.request.query_params.get("version")
        algorithm_version = None
        endpoint_name = 'income_classifier'
        print("End point name found", endpoint_name)
        if endpoint_name == 'income_classifier':
            algorithm_object = RandomForestClassifier()
        elif endpoint_name == 'application_classifier':
            algorithm_object = RandomForestApplicationClassifier()

        # prediction = algorithm_object.compute_prediction(request.data)
        algs = MLAlgorithm.objects.get(parent_endpoint__name = endpoint_name)
        query_object_data_dict = {}

        for ln in loan:
            query_object_data_dict[ln.client_id] = []
            query_object_data_dict[ln.client_id].append(model_to_dict(ln))
        print("query object data", query_object_data_dict)
        # qury_predict_dict_data = {}
        # for d_id, d_info in query_object_data_dict.items():
        #     print("\nQuery Data ID:", d_id)
        #     for key in d_info:
        #         qury_predict_dict_data[d_id] = []
                
        #         print(key) 
        #         prediction = algorithm_object.compute_prediction(key)
        #         qury_predict_dict_data[d_id].append(prediction)
        #     print("Query  Predictions data", qury_predict_dict_data)
        object_data_dict = {}
        for ln in loan:
            object_data_dict[ln.client_id] = []
            data ={'age': 32, 'workclass': 'Private', 'fnlwgt': 70984, 'education': 'Assoc-voc', 'education-num': 11, 'marital-status': 'Married-civ-spouse', 'occupation': 'Machine-op-inspct', 'relationship': 'Husband', 'race': 'White', 'sex': 'Male', 'capital-gain': 0, 'capital-loss': 0, 'hours-per-week': 40, 'native-country': 'United-States'},
            object_data_dict[ln.client_id].append(data)
            print("object data", object_data_dict)

        predict_dict_data = {}
        for d_id, d_info in object_data_dict.items():
            print("\nQuery Data ID:", d_id)
            for key in d_info:
                predict_dict_data[d_id] = []
                input_data = key
                prediction = algorithm_object.compute_prediction(key)
                prediction["cust_id"] = d_id
                print(prediction['probability'])
                if  prediction['probability'] > 0.67:
                    color = 'red'
                    text = 'high risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a high risk of defaulting the loan'.format(d_id))
                elif  prediction['probability'] > 0.33:
                    color = 'blue'
                    text = 'moderate risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a moderate risk of defaulting the loan'.format(d_id))
                else:
                    color = 'green'
                    text = 'low risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a low risk of defaulting the loan'.format(d_id))
                predict_dict_data[d_id].append(prediction)
            print( 'Prediction:', predict_dict_data)


        label = prediction["label"] if "label" in prediction else "error"
        ml_request = MLRequest(
            input_data=input_data,
            full_response=prediction,
            response=label,
            feedback="",
            parent_mlalgorithm=algs,
        )
        ml_request.save()
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Chart JS Data~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # data = Loan_History.objects.all()
        # return_data = log.grade_avg(data)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~Chart JS Data End ~~~~~~~~~~~~~~~~~~~~~~
        prediction["request_id"] = ml_request.id
        context = {
            'income_classifier_prediction': predict_dict_data,
            'loan': loan,
            'user_name':user_name,
            'acc_user':acc_user,
            # 'webdata':return_data
        }
        return context



class ApplicationAnalyticsResultsView(ListView):
    template_name = 'dashboards/application/index.html'
    def get_queryset(self, **kwargs):
        global cust_data, loan, user_name, input_data,acc_user
        user = self.request.user
        user_name = user.first_name
        acc_user = AccountUser.objects.get(user=user)
        print("Found USer", user_name)
        org = Organization.objects.get(id=1)
        client = Clients.objects.filter(insti=org)
        loan = Loan.objects.filter(signing_officer__insti = org)

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)

        # algorithm_status = self.request.query_params.get("status", "production")
        algorithm_status = "production"
        # algorithm_version = self.request.query_params.get("version")
        algorithm_version = None
        endpoint_name = 'income_classifier'
        print("End point name found", endpoint_name)
        if endpoint_name == 'income_classifier':
            algorithm_object = RandomForestClassifier()
        elif endpoint_name == 'application_classifier':
            algorithm_object = RandomForestApplicationClassifier()

        # prediction = algorithm_object.compute_prediction(request.data)
        algs = MLAlgorithm.objects.get(parent_endpoint__name = endpoint_name)
        query_object_data_dict = {}

        for ln in loan:
            query_object_data_dict[ln.client_id] = []
            query_object_data_dict[ln.client_id].append(model_to_dict(ln))
        print("query object data", query_object_data_dict)
        # qury_predict_dict_data = {}
        # for d_id, d_info in query_object_data_dict.items():
        #     print("\nQuery Data ID:", d_id)
        #     for key in d_info:
        #         qury_predict_dict_data[d_id] = []
                
        #         print(key) 
        #         prediction = algorithm_object.compute_prediction(key)
        #         qury_predict_dict_data[d_id].append(prediction)
        #     print("Query  Predictions data", qury_predict_dict_data)
        object_data_dict = {}
        for ln in loan:
            object_data_dict[ln.client_id] = []
            data ={'age': 32, 'workclass': 'Private', 'fnlwgt': 70984, 'education': 'Assoc-voc', 'education-num': 11, 'marital-status': 'Married-civ-spouse', 'occupation': 'Machine-op-inspct', 'relationship': 'Husband', 'race': 'White', 'sex': 'Male', 'capital-gain': 0, 'capital-loss': 0, 'hours-per-week': 40, 'native-country': 'United-States'},
            object_data_dict[ln.client_id].append(data)
            print("object data", object_data_dict)

        predict_dict_data = {}
        for d_id, d_info in object_data_dict.items():
            print("\nQuery Data ID:", d_id)
            for key in d_info:
                predict_dict_data[d_id] = []
                input_data = key
                prediction = algorithm_object.compute_prediction(key)
                prediction["cust_id"] = d_id
                print(prediction['probability'])
                if  prediction['probability'] > 0.67:
                    color = 'red'
                    text = 'high risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a high risk of defaulting the loan'.format(d_id))
                elif  prediction['probability'] > 0.33:
                    color = 'blue'
                    text = 'moderate risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a moderate risk of defaulting the loan'.format(d_id))
                else:
                    color = 'green'
                    text = 'low risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a low risk of defaulting the loan'.format(d_id))
                predict_dict_data[d_id].append(prediction)
            print( 'Prediction:', predict_dict_data)


        label = prediction["label"] if "label" in prediction else "error"
        ml_request = MLRequest(
            input_data=input_data,
            full_response=prediction,
            response=label,
            feedback="",
            parent_mlalgorithm=algs,
        )
        ml_request.save()
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Chart JS Data~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # data = Loan_History.objects.all()
        # return_data = log.grade_avg(data)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~Chart JS Data End ~~~~~~~~~~~~~~~~~~~~~~
        prediction["request_id"] = ml_request.id
        context = {
            'income_classifier_prediction': predict_dict_data,
            'loan': loan,
            'user_name':user_name,
            'acc_user':acc_user,
            # 'webdata':return_data
        }
        return context






class RetentionAnalyticsResultsView(ListView):
    template_name = 'dashboards/application/index.html'
    def get_queryset(self, **kwargs):
        global cust_data, loan, input_data
        org = Organization.objects.get(id=1)
        client = Clients.objects.filter(insti=org)
        loan = Loan.objects.filter(signing_officer__insti = org)

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)

        # algorithm_status = self.request.query_params.get("status", "production")
        algorithm_status = "production"
        # algorithm_version = self.request.query_params.get("version")
        algorithm_version = None
        endpoint_name = 'income_classifier'
        print("End point name found", endpoint_name)
        if endpoint_name == 'income_classifier':
            algorithm_object = RandomForestClassifier()
        elif endpoint_name == 'application_classifier':
            algorithm_object = RandomForestApplicationClassifier()

        # prediction = algorithm_object.compute_prediction(request.data)
        algs = MLAlgorithm.objects.get(parent_endpoint__name = endpoint_name)
        query_object_data_dict = {}

        for ln in loan:
            query_object_data_dict[ln.client_id] = []
            query_object_data_dict[ln.client_id].append(model_to_dict(ln))
        print("query object data", query_object_data_dict)
        # qury_predict_dict_data = {}
        # for d_id, d_info in query_object_data_dict.items():
        #     print("\nQuery Data ID:", d_id)
        #     for key in d_info:
        #         qury_predict_dict_data[d_id] = []
                
        #         print(key) 
        #         prediction = algorithm_object.compute_prediction(key)
        #         qury_predict_dict_data[d_id].append(prediction)
        #     print("Query  Predictions data", qury_predict_dict_data)
        object_data_dict = {}
        for ln in loan:
            object_data_dict[ln.client_id] = []
            data ={'age': 32, 'workclass': 'Private', 'fnlwgt': 70984, 'education': 'Assoc-voc', 'education-num': 11, 'marital-status': 'Married-civ-spouse', 'occupation': 'Machine-op-inspct', 'relationship': 'Husband', 'race': 'White', 'sex': 'Male', 'capital-gain': 0, 'capital-loss': 0, 'hours-per-week': 40, 'native-country': 'United-States'},
            object_data_dict[ln.client_id].append(data)
            print("object data", object_data_dict)

        predict_dict_data = {}
        for d_id, d_info in object_data_dict.items():
            print("\nQuery Data ID:", d_id)
            for key in d_info:
                predict_dict_data[d_id] = []
                input_data = key
                prediction = algorithm_object.compute_prediction(key)
                prediction["cust_id"] = d_id
                print(prediction['probability'])
                if  prediction['probability'] > 0.67:
                    color = 'red'
                    text = 'high risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a high risk of defaulting the loan'.format(d_id))
                elif  prediction['probability'] > 0.33:
                    color = 'blue'
                    text = 'moderate risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a moderate risk of defaulting the loan'.format(d_id))
                else:
                    color = 'green'
                    text = 'low risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a low risk of defaulting the loan'.format(d_id))
                predict_dict_data[d_id].append(prediction)
            print( 'Prediction:', predict_dict_data)


        label = prediction["label"] if "label" in prediction else "error"
        ml_request = MLRequest(
            input_data=input_data,
            full_response=prediction,
            response=label,
            feedback="",
            parent_mlalgorithm=algs,
        )
        ml_request.save()
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Chart JS Data~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # data = Loan_History.objects.all()
        # return_data = log.grade_avg(data)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~Chart JS Data End ~~~~~~~~~~~~~~~~~~~~~~
        prediction["request_id"] = ml_request.id
        context = {
            'income_classifier_prediction': predict_dict_data,
            'loan': loan,
        }
        return context

class BehavioralAnalyticsResultsView(ListView):
    template_name = 'dashboards/application/index.html'
    def get_queryset(self, **kwargs):
        global cust_data, loan, input_data
        org = Organization.objects.get(id=1)
        client = Clients.objects.filter(insti=org)
        loan = Loan.objects.filter(signing_officer__insti = org)

    def get_context_data(self, **kwargs):
        # context = super().get_context_data(**kwargs)

        # algorithm_status = self.request.query_params.get("status", "production")
        algorithm_status = "production"
        # algorithm_version = self.request.query_params.get("version")
        algorithm_version = None
        endpoint_name = 'income_classifier'
        print("End point name found", endpoint_name)
        if endpoint_name == 'income_classifier':
            algorithm_object = RandomForestClassifier()
        elif endpoint_name == 'application_classifier':
            algorithm_object = RandomForestApplicationClassifier()

        # prediction = algorithm_object.compute_prediction(request.data)
        algs = MLAlgorithm.objects.get(parent_endpoint__name = endpoint_name)
        query_object_data_dict = {}

        for ln in loan:
            query_object_data_dict[ln.client_id] = []
            query_object_data_dict[ln.client_id].append(model_to_dict(ln))
        print("query object data", query_object_data_dict)
        # qury_predict_dict_data = {}
        # for d_id, d_info in query_object_data_dict.items():
        #     print("\nQuery Data ID:", d_id)
        #     for key in d_info:
        #         qury_predict_dict_data[d_id] = []
                
        #         print(key) 
        #         prediction = algorithm_object.compute_prediction(key)
        #         qury_predict_dict_data[d_id].append(prediction)
        #     print("Query  Predictions data", qury_predict_dict_data)
        object_data_dict = {}
        for ln in loan:
            object_data_dict[ln.client_id] = []
            data ={'age': 32, 'workclass': 'Private', 'fnlwgt': 70984, 'education': 'Assoc-voc', 'education-num': 11, 'marital-status': 'Married-civ-spouse', 'occupation': 'Machine-op-inspct', 'relationship': 'Husband', 'race': 'White', 'sex': 'Male', 'capital-gain': 0, 'capital-loss': 0, 'hours-per-week': 40, 'native-country': 'United-States'},
            object_data_dict[ln.client_id].append(data)
            print("object data", object_data_dict)

        predict_dict_data = {}
        for d_id, d_info in object_data_dict.items():
            print("\nQuery Data ID:", d_id)
            for key in d_info:
                predict_dict_data[d_id] = []
                input_data = key
                prediction = algorithm_object.compute_prediction(key)
                prediction["cust_id"] = d_id
                print(prediction['probability'])
                if  prediction['probability'] > 0.67:
                    color = 'red'
                    text = 'high risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a high risk of defaulting the loan'.format(d_id))
                elif  prediction['probability'] > 0.33:
                    color = 'blue'
                    text = 'moderate risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a moderate risk of defaulting the loan'.format(d_id))
                else:
                    color = 'green'
                    text = 'low risk of defaulting the loan'
                    prediction["color"] = color
                    prediction["text"] = text
                    print('Client with ID # {} has a low risk of defaulting the loan'.format(d_id))
                predict_dict_data[d_id].append(prediction)
            print( 'Prediction:', predict_dict_data)


        label = prediction["label"] if "label" in prediction else "error"
        ml_request = MLRequest(
            input_data=input_data,
            full_response=prediction,
            response=label,
            feedback="",
            parent_mlalgorithm=algs,
        )
        ml_request.save()
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Chart JS Data~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # data = Loan_History.objects.all()
        # return_data = log.grade_avg(data)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~Chart JS Data End ~~~~~~~~~~~~~~~~~~~~~~
        prediction["request_id"] = ml_request.id
        context = {
            'income_classifier_prediction': predict_dict_data,
            'loan': loan,
        }
        return context



def profile(request):
    return render(request,'dashboards/profile/index.html')

def reports(request):
    return render(request,'dashboards/reports/index.html')

def articles(request):
    return render(request,'dashboards/articles/index.html')

