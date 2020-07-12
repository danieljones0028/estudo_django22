from django.http import HttpResponseRedirect
from django.shortcuts import render

# https://docs.djangoproject.com/pt-br/2.2/topics/forms/
from .forms import LoginForm

# Create your views here.
def login_page(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/home/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'index_login.html', {'form': form})