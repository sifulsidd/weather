from django.urls import path

from . import views

urlpatterns = [
    path("search/", views.SearchView.as_view(), name="search"),
    path("random/", views.RandomView.as_view(), name="random")
]