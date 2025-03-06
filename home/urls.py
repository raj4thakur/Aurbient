from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('request-service/', views.service_request_view, name='request_service'),
path('thank-you/', views.thank_you_view, name='thank_you'),
]