from django.conf.urls import url
from django.urls import include, path

from . import views
urlpatterns = [
    url(r'^$', views.login, name='login'),
    path('main_menu', views.main_menu, name='main_menu'),
    path('signup', views.signup, name='signup'),
    path('register', views.register, name='register'),
    path('welcome', views.welcome, name='welcome'),
    path('logout', views.logout, name='logout'),
path('upload_image', views.upload_image, name='upload_image'),

]