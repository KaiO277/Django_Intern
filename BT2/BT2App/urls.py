from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.insert, name='insert'),
    path('insertPerson/', views.insertPerson, name='insertPerson'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('update/<int:pk>/', views.update, name='update'),
    path('updatePerson/<int:pk>/', views.updatePerson, name='updatePerson'),
]
