from django.urls import path
from .views import login_page, login_form, login_home


urlpatterns = [
    path('login/', login_page),
    path('', login_form),
    path('home/', login_home, name="loginhome"),
]