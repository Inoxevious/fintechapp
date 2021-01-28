from django.shortcuts import render
from data_processor import imports as imp
from data_processor import logic as log
from companies.models import LoanApplication
# Create your views here.

def importer(request):
    opfile =  '/home/greats/Documents/projects/dreatol/webapp/fintechapp/clean_data.csv'
    imp.get_data(opfile)
    data = LoanApplication.objects.all()
    pri
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