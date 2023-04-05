from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('addnew', views.add_new, name='addnew'),
]