from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('shows', views.index),
    path('shows/new', views.add_show),
    path('create_show', views.create_show),
    path('shows/<int:show_id>', views.view_show),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('shows/<int:show_id>/delete', views.delete)
]