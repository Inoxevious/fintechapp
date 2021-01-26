from django.conf.urls import url
from django.urls import path, include
from .views import register, login, activate, account_activation_sent, logout, index

# SET THE NAMESPACE!
app_name = 'account'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('index/', index, name='index'),
    url(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        activate, name='activate'),
]