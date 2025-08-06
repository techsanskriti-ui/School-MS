from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'user/index.html')
def about(request):
    return render(request, 'user/about.html')
def admission(request):
    return render(request, 'user/admission.html')
def contact(request):
    return render(request, 'user/contact.html')
