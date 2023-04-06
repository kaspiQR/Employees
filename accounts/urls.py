from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.sign_in, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
