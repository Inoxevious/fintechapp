from django.conf.urls import url
from django.urls import path, include
from . import views 
# SET THE NAMESPACE!
app_name = 'companies'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[

    path('index/', views.index, name='index'),
    path('<int:co_id>/income_classifier/', views.IncomeClassfierResultsView.as_view(), name="income_classifier"),    
    path('application_analytics/', views.application_analytics, name='application_analytics'),
    path('retention_analytics/', views.retention_analytics, name='retention_analytics'),
    path('behavioral_analytics/', views.behavioral_analytics, name='behavioral_analytics'),
    path('profile/', views.profile, name='profile'),
    path('reports/', views.reports, name='reports'),
    path('articles/', views.articles, name='articles'),
   
]