from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/<int:id>/', views.user_profile),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]