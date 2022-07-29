from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wikiPage, name="wikiPage"),
    path("new-page", views.newPage, name="newPage"),
    path("edit-page", views.editPage, name="editPage"),
    path("random-page", views.randomPage, name="randomPage"),
]
