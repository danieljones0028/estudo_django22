from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.
@login_required
def homepage(request):
    return render(request, 'homepage.html')

def app_logout(request):
    logout(request)
    return redirect('login')
