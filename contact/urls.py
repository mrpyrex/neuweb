from django.urls import path
from . import views


app_name = 'contact'

urlpatterns = [
    path('', views.contactView, name='contact'),
    path('success', views.successView, name='success'),
]