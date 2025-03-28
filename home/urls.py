from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path("blogs/", views.blogsView, name='blogs'),
    path('request_service/', views.service_request_view, name='request_service'),
    path('thank_you/', views.thank_you_view, name='thank_you'),
    path("technology/", views.techView, name='technology'),
    path('career/', views.careerView, name='career'), 
    path('contact/', views.contactView, name='contact'), 
    path("about/", views.aboutView, name="about"),
    path("admin-dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("admin/update_status/<int:request_id>/<str:status>/", views.update_status, name="update_status"),
    path("admin/export-data/", views.export_data, name="export_data"),
    path('files/<str:file_id>/', views.serve_gridfs_file, name='serve_gridfs_file'),
]
