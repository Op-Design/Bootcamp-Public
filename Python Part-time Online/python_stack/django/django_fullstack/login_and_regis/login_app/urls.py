from django.urls import path
from . import views

urlpatterns = [
    path('', views.register),
    path('success', views.success),
    path('logout', views.logout),
    path('users', views.users),
]