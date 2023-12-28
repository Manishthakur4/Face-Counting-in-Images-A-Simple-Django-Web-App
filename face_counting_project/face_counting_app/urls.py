# face_counting_app/urls.py
from django.urls import path
from .views import index, count_faces_route

urlpatterns = [
    path('', index, name='index'),
    path('count_faces/', count_faces_route, name='count_faces'),
]