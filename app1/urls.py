from django.urls import path
from .views import *


urlpatterns = [
    path ('home/',homepage),
    path ('hospital_form/',hospital_form, name='hospital_form'),
    path ('client_form/',client_form, name='client_form'),
    path ('signup_view/',signup_view, name='signup'),
    path ('login_view/',login_view, name='login'),
    path ('edit_client/<int:pk>/',edit_client, name='edit_client'),
    path ('delete_client/<int:pk>/',delete_client, name='delete_client')
]