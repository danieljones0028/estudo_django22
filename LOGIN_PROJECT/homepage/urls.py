from django.urls import path
from .views import homepage, app_logout


urlpatterns = [
    path('', homepage, name='home'),
    path('logout/', app_logout, name='logout')
]