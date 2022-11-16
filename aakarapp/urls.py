from django.urls import path,include
from . import views

from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name="home"),
    path('accounts/', include('allauth.urls')),
    path('submission', views.submission, name="submission"),
    path('submitted', views.submitted, name="submitted"),
]
