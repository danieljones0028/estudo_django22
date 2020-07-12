from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_page(request):
    return render(request, 'index_login.html')

def login_form(request):
    return render(request, 'login_page.html')

def login_home(request):
    return render(request, 'index_login.html')