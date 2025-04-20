from django.db import models
import gridfs
from pymongo import MongoClient
from django.conf import settings
from django.utils.timezone import now

# Setup GridFS connection
client = MongoClient(settings.MONGO_URI)  
db = client[settings.GRIDFS_DATABASE]  
fs = gridfs.GridFS(db)  

class ServiceRequest(models.Model):
    SERVICE_CHOICES = [
        ("web_dev", "Web Development"),
        ("app_dev", "App Development"),
        ("digital_marketing", "Digital Marketing"),
        ("ui_ux", "UI/UX Design"),
        ("seo", "SEO Services"),
        ("other", "Other"),
    ]

    PROJECT_SCOPE_CHOICES = [
        ("small", "Small Project"),
        ("medium", "Medium Project"),
        ("large", "Large Scale Project"),
    ]

    EMPLOYEE_COUNT_CHOICES = [
        ("1-10", "1-10 Employees"),
        ("11-50", "11-50 Employees"),
        ("51-200", "51-200 Employees"),
        ("200+", "More than 200"),
    ]

    id = models.BigAutoField(primary_key=True) 
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, default='0000000000')
    company = models.CharField(max_length=255, default="xyz")
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    project_scope = models.CharField(max_length=50, choices=PROJECT_SCOPE_CHOICES)
    employees_count = models.CharField(max_length=50, choices=EMPLOYEE_COUNT_CHOICES)
    location = models.CharField(max_length=255)
    additional_info = models.TextField(blank=True, null=True)
    document = models.CharField(max_length=255, blank=True, null=True)  # Store GridFS file ID
    consent = models.BooleanField(default=False)
    reviewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.service_type}"


class JobApplication(models.Model):
    JOB_ROLE_CHOICES = [
        ("AI Engineer", "AI Engineer"),
        ("Full Stack Developer", "Full Stack Developer"),
        ("Data Scientist", "Data Scientist"),
        ("Product Manager", "Product Manager"),
    ]

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, default="")
    email = models.EmailField(default="example@example.com")
    phone = models.CharField(max_length=20, default="0000000000")
    country = models.CharField(max_length=255, default="India")
    experience = models.PositiveIntegerField(default=0)
    job_role = models.CharField(max_length=50, choices=JOB_ROLE_CHOICES, default="Not Specified")
    availability = models.DateField(default=now)
    preferred_location = models.CharField(max_length=255, default="Not Specified")
    willing_to_travel = models.BooleanField(default=False)
    expected_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    linkedin = models.URLField(default="https://linkedin.com/")
    portfolio = models.URLField(blank=True, null=True)
    resume = models.CharField(max_length=255, blank=True, null=True)  # Store GridFS file ID
    consent = models.BooleanField(default=False)
    reviewed = models.BooleanField(default=False)
    applied_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.job_role}"



# from django.db import models
# from django.utils import timezone

# class Visit(models.Model):
#     ip_address = models.GenericIPAddressField()
#     user_agent = models.TextField(blank=True)
#     path = models.CharField(max_length=255)
#     timestamp = models.DateTimeField(default=timezone.now)

#     def __str__(self):
#         return f"{self.ip_address} at {self.timestamp}"
