# backend/server/server/urls.py file
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from account.views import home
from companies import views
from apps.endpoints.urls import urlpatterns as endpoints_urlpatterns
urlpatterns = [
    path('', home, name='home'),
    path('companies_home_dash', views.HomeView.as_view(), name="companies_home_dash"),
    path('admin/', admin.site.urls),
    path('companies/', include('companies.urls')),
    path('d_processor/', include('d_processor.urls')),
    path('account/', include('account.urls')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
]

urlpatterns += endpoints_urlpatterns
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)