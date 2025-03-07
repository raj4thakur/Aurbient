from django.urls import path
from . import views
app_name='home'
urlpatterns = [
path('', views.home, name='home'),
path('request_service/', views.service_request_view, name='request_service'),
path('thank_you/', views.thank_you_view, name='thank_you'),
]