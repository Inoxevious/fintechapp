from django.shortcuts import render
from django.contrib.postgres.aggregates import StringAgg
from django.contrib.postgres.search import (
    SearchQuery, SearchRank, SearchVector, TrigramSimilarity,
)
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q, F
import json
from django.db import transaction
from account.models import Clients, LoanOfficer, Loan, AccountUser
from companies.models import *
from datetime import datetime, date
from django.db.models import Sum
from .serializers import Loan_HistorySerializers
from mergedeep import merge
from functools import reduce
from collections.abc import MutableMapping
from apps.endpoints.models import BehaviouralScores
from apps.endpoints.models import  RetentionScores
from apps.endpoints.models import  ApplicationScores
class GetPredictions:
    def __init__(self):
        global algorithm_object, prediction

    def get_application_scores(qry):

        prediction_data = {}
        for ln in qry:
            if ApplicationScores.objects.filter(loan_id=ln.id).exists():
                prediction_data = ApplicationScores.objects.filter(loan_id=ln.id)
            else:
                prediction_data['application_text'] = "Loan prediction scheduled"
                prediction_data['application_label'] = "System validating data"
                # prediction_data_dict[ln.LOAN_ID].append(prediction)
        # print("predictions",prediction)
        return prediction_data_dict

    def get_retention_scores(qry):
        prediction_data_dict = {}
        for ln in qry:
            if RetentionScores.objects.filter(loan_id=ln.id).exists():
                prediction_data_dict = RetentionScores.objects.filter(loan_id=ln.id)
            else:
                prediction_data_dict['retention_text'] = "Loan prediction scheduled"
                prediction_data_dict['retention_label'] = "System validating data"

        # print("predictions",prediction)
        return prediction_data

    def get_behavioral_scores(qry):
        
        for ln in qry:
            if BehaviouralScores.objects.filter(loan_id=ln.id).exists():
                prediction_data_dict = BehaviouralScores.objects.filter(loan_id=ln.id)
            else:
                prediction_data_dict = {}
                prediction_data_dict['application_loan_id'] = ln.id
                prediction_data_dict['application_text'] = "Loan prediction scheduled"
                prediction_data_dict['application_label'] = "System validating data"

        # print("predictions",prediction)
        return prediction_data

        
  