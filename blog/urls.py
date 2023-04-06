from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('addnew', views.add_new, name='addnew'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.destroy, name='delete'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('update/<int:id>', views.update, name='update'),
]