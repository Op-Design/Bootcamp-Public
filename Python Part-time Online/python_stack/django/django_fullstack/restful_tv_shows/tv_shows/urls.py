from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('shows/new', views.showsnew),
    path('shows/create', views.showscreate),
    path('shows/<int:id>', views.showsid),
    path('shows', views.shows),
    path('shows/<int:id>/edit', views.showsidedit),
    path('shows/<int:id>/update', views.showsidupdate),
    path('shows/<int:id>/destroy', views.showsiddestroy),
]