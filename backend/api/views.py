from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
import requests

# Create your views here.

# the search feature is populating 
class SearchView(generics.RetrieveAPIView):
    def get(self, request):
        # this is basically getting the url where search is the paramter and the value is going to be the thing we input
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
    def get(self, request):
        try:
            response = requests.get("https://www.themealdb.com/api/json/v1/1/categories.php")
            # sends back to front end in json form
            return Response(response.json())
        except requests.exceptions.Timeout:
            print("The request timed out")
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occured: {err}")
        except requests.exceptions.ConnectionError:
            print("A connection error occurred.")
        except requests.exceptions.RequestException as e:
            print(f"An unexpected error occurred: {e}")
    
class CategorySearch(generics.RetrieveAPIView):
    pass

class IngredientView(generics.RetrieveAPIView):
    pass

# gets just the random information 
class RandomView(generics.RetrieveAPIView):
    # the get method needs a request parameter even if unused
    def get(self, request):
        try:
            response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")
            return Response(response.json())
        except requests.exceptions.Timeout:
            print("The request timed out")
        except requests.exceptions.HTTPError as err:
            print(f"HTTP error occured: {err}")
        except requests.exceptions.ConnectionError:
            print("A connection error occurred.")
        except requests.exceptions.RequestException as e:
            print(f"An unexpected error occurred: {e}")