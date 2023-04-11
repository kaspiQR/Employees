from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index_visit'),
    path('detail_visit/<int:id>', views.detail, name='detail_visit'),
    path('delete_visit/<int:id>', views.delete, name='delete_visit'),
    path('edit_visit/<int:id>', views.edit, name='edit_visit'),
    path('add_visit', views.add_visit, name='add_visit'),
]
