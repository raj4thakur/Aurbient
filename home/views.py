from django.shortcuts import render

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
