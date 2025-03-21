from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from bson import ObjectId
import pymongo
import gridfs
from django.conf import settings

from .forms import ServiceRequestForm, JobApplicationForm
from .models import JobApplication

# Home Page View
def home(request):
    form = ServiceRequestForm()  # Pass form to template
    return render(request, 'home/home.html', {'form': form})


# Thank You Page View
def thank_you_view(request):
    return render(request, 'home/thank_you.html')


def service_request_view(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your request has been submitted successfully!")
            return redirect("home:home")  # Redirect on success
        else:
            print("Form Errors:", form.errors)  # Debugging: Print errors in terminal
            messages.error(request, "There were errors in your submission. Please correct them.")
    else:
        form = ServiceRequestForm()

    return render(request, "home/home.html", {"form": form})



# Blog Page View
def blogsView(request):
    return render(request, 'home/blogs.html')


# Technology Page View
def techView(request):
    return render(request, 'home/technology.html')


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import JobApplicationForm

def careerView(request):
    form = JobApplicationForm()

    if request.method == "POST":
        form = JobApplicationForm(request.POST, request.FILES)  # Handle file uploads

        if form.is_valid():
            form.save()  # Saves the form and handles the resume file upload automatically
            messages.success(request, "Your application has been submitted successfully!")
            return redirect("home:career")  # Stay on the same page

        else:
            messages.error(request, "There were errors in your submission. Please correct them.")
            print("Job Application Form Errors:", form.errors)

    return render(request, "home/career.html", {"form": form})

# About Us Page View
def aboutView(request):
    return render(request, 'home/about.html')

# Contact Page View
def contactView(request):
    return render(request, 'home/contact.html')


from django.shortcuts import render
from .models import ServiceRequest, JobApplication

def admin_dashboard(request):
    service_requests = ServiceRequest.objects.all()
    job_applications = JobApplication.objects.all()
    return render(request, "home/admin_dashboard.html", {
        "service_requests": service_requests,
        "job_applications": job_applications
    })
