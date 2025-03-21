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

    id = models.BigAutoField(primary_key=True) 
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20,default='0000000000')
    company = models.CharField(max_length=255,default="xyz")
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    project_scope = models.CharField(max_length=50, choices=PROJECT_SCOPE_CHOICES)
    employees_count = models.CharField(max_length=50, choices=EMPLOYEE_COUNT_CHOICES)
    location = models.CharField(max_length=255)
    additional_info = models.TextField(blank=True, null=True)  # Optional
    document = models.FileField(upload_to="service_requests/documents/", blank=True, null=True)  # Optional
    consent = models.BooleanField(default=False)
    reviewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"{self.name} - {self.service_type}"


from django.utils.timezone import now
from django.db import models

class JobApplication(models.Model):
    JOB_ROLE_CHOICES = [
        ("AI Engineer", "AI Engineer"),
        ("Full Stack Developer", "Full Stack Developer"),
        ("Data Scientist", "Data Scientist"),
        ("Product Manager", "Product Manager"),
    ]

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, default="")  # Default empty string
    email = models.EmailField(default="example@example.com")  # Default email
    phone = models.CharField(max_length=20, default="0000000000")  # Default phone number
    country = models.TextField(default='India')
    experience = models.PositiveIntegerField(default=0)
    job_role = models.CharField(max_length=50, choices=JOB_ROLE_CHOICES, default="Not Specified")
    availability = models.DateField(default=now)  # Set default to current date
    preferred_location = models.CharField(max_length=255, default="Not Specified")  
    willing_to_travel = models.BooleanField(default=False)
    expected_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  
    linkedin = models.URLField(default="https://linkedin.com/")  # Default placeholder
    portfolio = models.URLField(blank=True, null=True)  
    resume = models.FileField(upload_to="resumes/", null=False,default="resume/raj.pdf")  
    consent = models.BooleanField(default=False)
    reviewed = models.BooleanField(default=False)
    applied_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.job_role}"