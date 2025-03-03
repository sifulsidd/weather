from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
import requests

# Create your views here.
class SearchView(generics.RetrieveAPIView):
    def get(self, request):
        query = request.GET.get('search', None)
        
        if query:
            try:
                api_url = f"https://www.themealdb.com/api/json/v1/1/search.php?s={query}"
                response = requests.get(api_url)
                return Response(response.json())
            except requests.exceptions.Timeout:
                print("The request timed out.")
            except requests.exceptions.HTTPError as err:
                print(f"HTTP error occurred: {err}")
            except requests.exceptions.ConnectionError:
                print("A connection error occurred.")
            except requests.exceptions.RequestException as e:
                print(f"An unexpected error occurred: {e}")
                
    
    # request.data gets the data from the front end and makes it viewable for us in the backend
class CategoriesView(generics.RetrieveAPIView):
    pass

class CategorySearch(generics.RetrieveAPIView):
    pass

class IngredientView(generics.RetrieveAPIView):
    pass

class RandomView(generics.RetrieveAPIView):
    pass