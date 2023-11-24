from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.insert, name='insert'),
    path('insertUser/', views.insertUser, name='insertUser'),
    path('deleteUser/<int:pk>/', views.deleteUser, name='deleteUser'),
    path('update/<int:pk>/', views.update, name='update'),
    path('updateUser/', views.updateUser, name='updateUser'),
]

urlpatterns += staticfiles_urlpatterns() 
