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

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ServiceRequestForm
import gridfs
from bson import ObjectId

# Initialize GridFS
client = pymongo.MongoClient(settings.MONGO_URI)
db = client[settings.GRIDFS_DATABASE]
fs = gridfs.GridFS(db)

def service_request_view(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST, request.FILES)
        
        if form.is_valid():
            service_request = form.save(commit=False)

            # Handle file upload to GridFS
            if "document" in request.FILES:
                file = request.FILES["document"]
                file_id = fs.put(file, filename=file.name)
                service_request.document = str(file_id)  # Store the file ID

            service_request.save()
            messages.success(request, "Your request has been submitted successfully!")
            return redirect("home:home")

        else:
            print("Form Errors:", form.errors)
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
        form = JobApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            job_application = form.save(commit=False)

            # Handle file upload to GridFS
            if "resume" in request.FILES:
                file = request.FILES["resume"]
                file_id = fs.put(file, filename=file.name)
                job_application.resume = str(file_id)  # Store the file ID

            job_application.save()
            messages.success(request, "Your application has been submitted successfully!")
            return redirect("home:career")

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
from .models import ServiceRequest, JobApplication,Visit
def admin_dashboard(request):
    service_requests = ServiceRequest.objects.all()
    job_applications = JobApplication.objects.all()
    visit_count = Visit.objects.count()
    return render(request, "home/admin_dashboard.html", {
        "service_requests": service_requests,
        "job_applications": job_applications,
        'visit_count': visit_count,
    })
def update_status(request, request_id, status):
    request_obj = ServiceRequest.objects.get(id=request_id)
    request_obj.status = status
    request_obj.save()
    return JsonResponse({"success": True})

from django.http import HttpResponse, Http404
import gridfs

def serve_gridfs_file(request, file_id):
    """ Retrieve and serve files from GridFS """
    try:
        file = fs.get(ObjectId(file_id))
        response = HttpResponse(file.read(), content_type="application/octet-stream")
        response["Content-Disposition"] = f'attachment; filename="{file.filename}"'
        return response
    except gridfs.errors.NoFile:
        raise Http404("File not found")

def export_data(request):
    # response = HttpResponse(content_type="text/csv")
    # response["Content-Disposition"] = 'attachment; filename="admin_data.csv"'

    # writer = csv.writer(response)
    # writer.writerow(["Type", "Name", "Email", "Service/Job Role", "Submitted At", "Status"])

    # service_requests = ServiceRequest.objects.all()
    # for req in service_requests:
    #     writer.writerow(["Service Request", req.name, req.email, req.service_type, req.created_at, req.status])

    # job_applications = JobApplication.objects.all()
    # for job in job_applications:
    #     writer.writerow(["Job Application", job.name, job.email, job.job_role, job.applied_at, "N/A"])

    # return response
    return 


