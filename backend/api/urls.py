from django.urls import path

from . import views

urlpatterns = [
    path("search/", views.SearchView.as_view(), name="search"),
    path("random/", views.RandomView.as_view(), name="random"),
    path("categories/", views.CategoriesView.as_view(), name="all-categories"),
    path("ingredient/", views.IngredientView.as_view(), name="ingredient-search")
]