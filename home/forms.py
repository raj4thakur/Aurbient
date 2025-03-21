from django import forms
from .models import ServiceRequest
class ServiceRequestForm(forms.ModelForm):
    consent = forms.BooleanField(required=True, error_messages={'required': 'You must give consent to submit the form.'})

    class Meta:
        model = ServiceRequest
        fields = [
            "name", "email", "phone", "company", "service_type",
            "project_scope", "employees_count", "location",
            "additional_info", "document", "consent"
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-input", "placeholder": "Full Name", "required": True}),
            "email": forms.EmailInput(attrs={"class": "form-input", "placeholder": "Your Email", "required": True}),
            "phone": forms.TextInput(attrs={"class": "form-input", "placeholder": "Your Phone Number", "required": True}),
            "company": forms.TextInput(attrs={"class": "form-input", "placeholder": "Company Name", "required": True}),
            "service_type": forms.Select(attrs={"class": "form-select", "required": True}),
            "project_scope": forms.Select(attrs={"class": "form-select", "required": True}),
            "employees_count": forms.Select(attrs={"class": "form-select", "required": True}),
            "location": forms.TextInput(attrs={"class": "form-input", "placeholder": "Your Location", "required": True}),
            "additional_info": forms.Textarea(attrs={"class": "form-textarea", "placeholder": "Any additional details..."}),  # Optional
            "document": forms.FileInput(attrs={"class": "form-input"}),  # Optional
            "consent": forms.CheckboxInput(attrs={"class": "form-checkbox", "required": True}),
        }



from django import forms
from .models import JobApplication

from django import forms
from .models import JobApplication
class JobApplicationForm(forms.ModelForm):
    consent = forms.BooleanField(
        required=True,
        label="I agree to the processing of my data for recruitment purposes.",
        error_messages={'required': 'You must give consent to submit the form.'}
    )

    class Meta:
        model = JobApplication
        fields = [
            "name", "email", "phone", "country", "experience", "job_role",
            "availability", "preferred_location", "willing_to_travel",
            "expected_salary", "linkedin", "portfolio", "resume", "consent"
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-input", "placeholder": "Full Name", "required": True}),
            "email": forms.EmailInput(attrs={"class": "form-input", "placeholder": "Your Email", "required": True}),
            "phone": forms.TextInput(attrs={"class": "form-input", "placeholder": "Your Phone Number", "required": True}),
            "country": forms.TextInput(attrs={"class": "form-input", "placeholder": "Country", "required": True}),
            "experience": forms.NumberInput(attrs={"class": "form-input", "placeholder": "Years of Experience", "min": "0", "required": True}),
            "job_role": forms.Select(attrs={"class": "form-select", "required": True}),
            "availability": forms.DateInput(attrs={"type": "date", "class": "form-input", "required": True}),
            "preferred_location": forms.TextInput(attrs={"class": "form-input", "placeholder": "Preferred Location", "required": True}),
            "willing_to_travel": forms.Select(choices=[(True, "Yes"), (False, "No")], attrs={"class": "form-select", "required": True}),
            "expected_salary": forms.NumberInput(attrs={"class": "form-input", "placeholder": "Expected Salary in USD", "min": "0", "required": True}),
            "linkedin": forms.URLInput(attrs={"class": "form-input", "placeholder": "LinkedIn Profile URL", "required": True}),
            "portfolio": forms.URLInput(attrs={"class": "form-input", "placeholder": "Portfolio Website (if any)"}),  # Optional
            "resume": forms.FileInput(attrs={"class": "form-input", "required": True}),  # Required
            "consent": forms.CheckboxInput(attrs={"class": "form-checkbox", "required": True}),
        }
