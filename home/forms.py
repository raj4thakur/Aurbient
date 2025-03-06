from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['name', 'email', 'phone', 'company', 'service_type', 'project_scope', 'employees_count', 'location', 'additional_info']
        widgets = {
            'service_type': forms.Select(attrs={'class': 'form-control'}),
            'project_scope': forms.Select(attrs={'class': 'form-control'}),
            'employees_count': forms.Select(attrs={'class': 'form-control'}),
            'additional_info': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
        }
