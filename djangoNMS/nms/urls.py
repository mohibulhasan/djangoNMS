from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='nms-home'),
    path('about/', views.about, name='nms-about'),
]