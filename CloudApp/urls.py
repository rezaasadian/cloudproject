from django.conf.urls import url, include
from CloudApp import views


urlpatterns = [
    url('post-user', views.create_user),
    url('profile', views.profile)
]