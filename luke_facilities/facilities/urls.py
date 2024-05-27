from django.urls import path
from . import views

urlpatterns = [
    path('', views.facility_list, name='facility_list'),
    path('create/', views.facility_create, name='facility_create'),
    path('archive/<int:pk>/', views.facility_archive, name='facility_archive'),
]
