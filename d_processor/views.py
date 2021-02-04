from django.shortcuts import render
from data_processor import imports as imp
from data_processor import logic as log
from companies.models import LoanApplication
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.income_classifier.random_forest import RandomForestClassifier
from apps.ml.income_classifier.extra_trees import ExtraTreesClassifier # import ExtraTrees ML algorithm
from apps.ml.application_classifier.random_forest import RandomForestApplicationClassifier
from apps.ml.application_classifier.random_f import LoanApplicationClassifier
from rest_framework import views, status
from rest_framework.response import Response
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Create your views here.

def importer(request):
    path_to_artifacts = os.path.join(BASE_DIR, 'apps/ml/algo_data/files/')
    opfile =  path_to_artifacts + 'no_header_data.csv'
    imp.get_data_income_data(opfile)
    data = LoanApplication.objects.all()
    context = {
        'data':data,
    }
    return render(request,'test.html', context)

def test(request):
    data = LoanApplication.objects.all()
    return_data = log.grade_avg(data)
    context = {
        'webdata':return_data
    }
    return render(request, 'test.html', context)


def dash(request):

    return render("dash.html")

def dashboard(request):
    data = LoanApplication.objects.all()
    return_data = log.grade_avg(data)
    context = {
        'webdata':return_data
    }
    return render(request, "dashboard-chartsjs.html", context)


def add_algo(request):
    # ML registry
    try:
        print("Adding ML algorithms to registry")
        registry = MLRegistry() # create ML registry
        # Random Forest classifier
        rf = RandomForestClassifier()
        # add to ML registry
        registry.add_algorithm(endpoint_name="income_classifier",
                                algorithm_object=rf,
                                algorithm_name="random forest",
                                algorithm_status="production",
                                algorithm_version="0.0.1",
                                owner="Dreatol",
                                algorithm_description="Random Forest with simple pre- and post-processing",
                                algorithm_code=inspect.getsource(RandomForestClassifier))

        # Applications Random Forest classifier
        aprf = RandomForestApplicationClassifier()
        # add to ML registry
        registry.add_algorithm(endpoint_name="application_classifier",
                                algorithm_object=aprf,
                                algorithm_name="random forest",
                                algorithm_status="production",
                                algorithm_version="0.0.1",
                                owner="Dreatol",
                                algorithm_description="Random Forest with simple pre- and post-processing",
                                algorithm_code=inspect.getsource(RandomForestApplicationClassifier))

        ln_rf = LoanApplicationClassifier()
        # add to ML registry
        registry.add_algorithm(endpoint_name="loan_application_classifier",
                                algorithm_object=ln_rf,
                                algorithm_name="random forest",
                                algorithm_status="production",
                                algorithm_version="0.0.1",
                                owner="Dreatol",
                                algorithm_description="55 features Random Forest with simple pre- and post-processing",
                                algorithm_code=inspect.getsource(LoanApplicationClassifier))






        # # Extra Trees classifier
        # et = ExtraTreesClassifier()
        # # add to ML registry

        # registry.add_algorithm(endpoint_name="income_classifier",
        #                         algorithm_object=et,
        #                         algorithm_name="extra trees",
        #                         algorithm_status="testing",
        #                         algorithm_version="0.0.1",
        #                         owner="Dreatol",
        #                         algorithm_description="Extra Trees with simple pre- and post-processing",
        #                         algorithm_code=inspect.getsource(RandomForestClassifier))
        # print("Added ML algorithms to registry")
    except Exception as e:
        print("Exception while loading the algorithms to the registry,", str(e))
        error = str(e)

    context = {
        'registry':registry,
    }
    return render(request, "test.html", context)