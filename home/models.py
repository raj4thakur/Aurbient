from django.db import models

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

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    project_scope = models.CharField(max_length=50, choices=PROJECT_SCOPE_CHOICES)
    employees_count = models.CharField(max_length=50, choices=EMPLOYEE_COUNT_CHOICES)
    location = models.CharField(max_length=255)
    additional_info = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service_type}"
