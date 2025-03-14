from django.shortcuts import render
from django.http import JsonResponse
def home(request):
    return render(request,'home/home.html')

def thank_you_view(request):
    return render(request, 'home/thank_you.html')

from django.shortcuts import render, redirect
from .forms import ServiceRequestForm

def service_request_view(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:thank_you')  # Redirect to thank-you page
    else:
        form = ServiceRequestForm()

    return render(request, 'home/service_request.html', {'form': form})

def blogsView(request):
    return render(request, 'home/blogs.html')

def techView(request):
    return render(request, 'home/technology.html')

def careerView(request):
    return render(request, 'home/career.html')

def aboutView(request):
    return render(request, 'home/about.html')

def contactView(request):
    return render(request, 'home/contact.html')

import gridfs
import pymongo
from django.conf import settings
from django.shortcuts import render, redirect
from .models import JobApplication

# Connect to MongoDB and GridFS
client = pymongo.MongoClient(settings.DATABASES['default']['CLIENT']['host'])
db = client['AurbientFit']
fs = gridfs.GridFS(db)  
def apply_job(request):
    if request.method == "POST" and request.is_ajax():
        name = request.POST.get("name")
        email = request.POST.get("email")
        job_position = request.POST.get("job_position")
        resume = request.FILES.get("resume")

        # Store resume in GridFS
        resume_id = None
        if resume:
            resume_id = fs.put(resume, filename=resume.name, contentType=resume.content_type)

        # Save job application details
        application = JobApplication.objects.create(
            name=name,
            email=email,
            job_position=job_position,
            resume_id=str(resume_id)  # Store GridFS file ID
        )

        # Return JSON response (AJAX success message)
        return JsonResponse({"message": "Application submitted successfully!", "applicant": name})

    return JsonResponse({"error": "Invalid request"}, status=400)

from django.http import HttpResponse

def download_resume(request, file_id):
    try:
        file = fs.get(file_id)  # Fetch file from GridFS
        response = HttpResponse(file.read(), content_type=file.content_type)
        response['Content-Disposition'] = f'attachment; filename="{file.filename}"'
        return response
    except gridfs.errors.NoFile:
        return HttpResponse("File not found", status=404)
