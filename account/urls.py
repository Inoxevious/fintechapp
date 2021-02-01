from django.conf.urls import url
from django.urls import path, include
from .views import register, view_client,login, activate, account_activation_sent, logout, index,home

# SET THE NAMESPACE!
app_name = 'account'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('index/', index, name='index'),
    path('home/', home, name='home'),
    path('<int:loan_id>view_client/', view_client, name='view_client'),
    url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
]