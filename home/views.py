from django.shortcuts import render
# Create your views here.
def home(request):
    return render(request, 'index.html')
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request,'contact.html' )

def career(request):
    return render(request,'career.html' )

def sign(request):
    return render(request,'sign.html' )

def job(request):
    return render(request,'job.html' )
def postjob(request):
    return render(request,'postjob.html' )
def apply(request):
    return render(request,'apply.html' )
