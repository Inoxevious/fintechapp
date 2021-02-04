from django.shortcuts import render
from django.contrib.postgres.aggregates import StringAgg
from django.contrib.postgres.search import (
    SearchQuery, SearchRank, SearchVector, TrigramSimilarity,
)
from mergedeep import merge
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

from django.http import JsonResponse

from rest_framework.generics import ListAPIView
from .serializers import Loan_HistorySerializers
from .models import Loan_History, IncomeData
from .pagination import StandardResultsSetPagination
from .get_income_pred import GetPredictions as gpred

class Loan_ApplicationView(APIView):
    def get(self, request, *args, **kw):
        # filter the queryset based on the filters applied
        global qry
        pagination_class = StandardResultsSetPagination
        qry = Loan_History.objects.all()[:50]
        NAME_INCOME_TYPE = self.request.query_params.get('business', None)
        ORGANIZATION_TYPE = self.request.query_params.get('mortage', None)
        OCCUPATION_TYPE = self.request.query_params.get('funeral', None)
        CODE_GENDER = self.request.query_params.get('school', None)
        sort_by = self.request.query_params.get('sort_by', None)


        if NAME_INCOME_TYPE:
            qry = Loan_History.objects.filter(NAME_INCOME_TYPE = NAME_INCOME_TYPE)[:50]

        if ORGANIZATION_TYPE:
            qry = Loan_History.objects.filter(ORGANIZATION_TYPE = ORGANIZATION_TYPE)[:50]

        if OCCUPATION_TYPE:
            qry = Loan_History.objects.filter(OCCUPATION_TYPE = OCCUPATION_TYPE)[:50]
        if CODE_GENDER:
            qry = Loan_History.objects.filter(CODE_GENDER = CODE_GENDER)[:50]  
        # sort it if applied on based on price/points
        if sort_by == "income":
            qry = qry.order_by("AMT_INCOME_TOTAL")
        elif sort_by == "credit_amount":
            qry = qry.order_by("AMT_CREDIT")

# get predictions for applications scoring predictions
        application_classifier_data = gpred.get_pred(qry)
        return Response(data={
            # 'labels': labels,
            # 'pagination_class':pagination_class,
            'data': application_classifier_data,
            
        })

class HomeView(ListView):
    template_name = 'dashboards/landing/index.html'
    def get_queryset(self, **kwargs):
        global cust_data, loan, user_name, input_data,acc_user, time
        user = self.request.user
        time = end = datetime.today()
        user_name = user
        acc_user = AccountUser.objects.get(user=user)
        org = Organization.objects.get(id=1)
        client = Clients.objects.filter(insti=org)

    def get_context_data(self, **kwargs):
        context = {
            'user_name':user_name,
            'acc_user':acc_user,
        }
        return context

class BehavioralAnalyticsResultsView(ListView):
    template_name = 'dashboards/behavioral/index.html'
    def get_queryset(self, **kwargs):
        global cust_data, loan, user_name, input_data,acc_user, time
        user = self.request.user
        time = end = datetime.today()
        user_name = user
        acc_user = AccountUser.objects.get(user=user)
        org = Organization.objects.get(id=1)
        client = Clients.objects.filter(insti=org)

    def get_context_data(self, **kwargs):
        context = {
            'user_name':user_name,
            'acc_user':acc_user,
        }
        return context


class ApplicationAnalyticsResultsView(ListView):
    template_name = 'dashboards/application/index.html'
    def get_queryset(self, **kwargs):
        global cust_data, loan, user_name, input_data,acc_user, time
        user = self.request.user
        time = end = datetime.today()
        user_name = user
        acc_user = AccountUser.objects.get(user=user)
        org = Organization.objects.get(id=1)
        client = Clients.objects.filter(insti=org)

    def get_context_data(self, **kwargs):
        context = {
            'user_name':user_name,
            'acc_user':acc_user,
        }
        return context

class RetentionAnalyticsResultsView(ListView):
    template_name = 'dashboards/retention/index.html'
    def get_queryset(self, **kwargs):
        global cust_data, loan, user_name, input_data,acc_user, time
        user = self.request.user
        time = end = datetime.today()
        user_name = user
        acc_user = AccountUser.objects.get(user=user)
        org = Organization.objects.get(id=1)
        client = Clients.objects.filter(insti=org)

    def get_context_data(self, **kwargs):
        context = {
            'user_name':user_name,
            'acc_user':acc_user,
        }
        return context


def profile(request):
    return render(request,'dashboards/profile/index.html')

def reports(request):
    return render(request,'dashboards/reports/index.html')

def articles(request):
    return render(request,'dashboards/articles/index.html')

import csv
from django.http import HttpResponse
def some_view(request):
# Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    return response


def application_report_export_csv(request):
    
     return render(request,'dashboards/articles/index.html')

def application_report(request):
     return render(request,'dashboards/articles/index.html')

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
    for entry in queryset:
        labels.append(entry['OCCUPATION_TYPE'])
        data.append(entry['amount_borrowed'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

