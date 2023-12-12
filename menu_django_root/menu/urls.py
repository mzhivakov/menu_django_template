from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("<url_path>/", views.menu_handler),
]