from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('student-list', views.index, name='index'),
    path('test-media', views.testMedia, name='testMedia'),
    path('insert', views.insert, name='insert'),
    path('add', views.add, name='add'),
    path('delete/<str:pk>', views.remove, name='delete'),
    path('update/<str:pk>', views.update, name='update'),
    path('edit/<str:pk>', views.edit, name='edit'),
    path('send', views.send, name='send'),
    path('send-email', views.sendEmail, name='sendEmail'),
    path('check-login', views.check_login, name='check_login'),
    path('login', views.login, name='login'),
    # path('google-login', views.login_google, name='google_login'),
    path('', views.main,name='main'),
]
