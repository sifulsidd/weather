from django.shortcuts import render
from rest_framework import generics, status

# Create your views here.
class SearchView(generics.RetrieveAPIView):
    pass

class CategoriesView(generics.RetrieveAPIView):
    pass

class CategorySearch(generics.RetrieveAPIView):
    pass

class IngredientView(generics.RetrieveAPIView):
    pass