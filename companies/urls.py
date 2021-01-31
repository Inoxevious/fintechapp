from django.conf.urls import url
from django.urls import path, include
from . import views 
<<<<<<< HEAD
# from .views import *
=======
>>>>>>> fe2c9bd2d5d9d693e3b134dfde94bb3dc2d99c4d
# SET THE NAMESPACE!
app_name = 'companies'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
<<<<<<< HEAD
    path("loan_history_listing/", views.Loan_HistoryListing.as_view(), name = 'listing'),
    path("ajax/business/", views.getBusiness, name = 'get_businesses'),
    path("ajax/mortage/", views.getMortage, name = 'get_mortages'),
    path("ajax/school/", views.getSchool, name = 'get_schools'),
    path("ajax/funeral/", views.getFuneral, name = 'get_funerals'),
=======
>>>>>>> fe2c9bd2d5d9d693e3b134dfde94bb3dc2d99c4d
    path('data_aggretation', views.data_aggretation, name="data_aggretation"),
    path('index/$', views.HomeView.as_view(), name="index"),    
    # path('', views.HomeView.as_view(), name="index"), 
    url(
        r"^index/(?P<user_id>.+)", views.HomeView.as_view(), name="index"
    ),
    path('income_classifier/', views.IncomeClassfierResultsView.as_view(), name="income_classifier"),    
    path('application_analytics/', views.ApplicationAnalyticsResultsView.as_view(), name='application_analytics'),
    path('retention_analytics/', views.RetentionAnalyticsResultsView.as_view(), name='retention_analytics'),
    path('behavioral_analytics/', views.BehavioralAnalyticsResultsView.as_view(), name='behavioral_analytics'),
    path('profile/', views.profile, name='profile'),
    path('reports/', views.reports, name='reports'),
    path('articles/', views.articles, name='articles'),
   
]