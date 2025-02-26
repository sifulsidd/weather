# first let's make a call for a specific meal

import requests

# change the value after s= to search for specific recipe
def information_about_recipe():
    # get an arrabiata
    response = requests.get("https://www.themealdb.com/api/json/v1/1/search.php?s=ARRABIATA")

    # print(response.status_code)

    res = None
    if response.status_code == 200:
        # print(response.json())
        res = response.json()

    item = res['meals'][0]
    ingredients = []
    for i in range(1,21):
        ingredient = item[f"strIngredient{i}"]
        measurement = item[f"strMeasure{i}"]
        sentence = ""
        if ingredient is not None and len(ingredient) > 0:
            sentence += ingredient
        
        if measurement is not None and len(measurement) > 0:
            sentence += ": " + measurement
        
        if len(sentence) > 0:
            ingredients.append(sentence)
    print(item['strMeal'])
    print(ingredients)
    print(item['strYoutube'])
    print(item['strInstructions'])
    print(item['strMealThumb'])
    # return ingredients


# information_about_recipe()

# random recipe received with all the information necessary
def random_recipe():
    response = requests.get("https://www.themealdb.com/api/json/v1/1/random.php")

        # print(response.status_code)

    res = None
    if response.status_code == 200:
        # print(response.json())
        res = response.json()
    
    item = res['meals'][0]
    ingredients = []
    for i in range(1,21):
        ingredient = item[f"strIngredient{i}"]
        measurement = item[f"strMeasure{i}"]
        sentence = ""
        if ingredient is not None and len(ingredient) > 0:
            sentence += ingredient
        
        if measurement is not None and len(measurement) > 0:
            sentence += ": " + measurement
        
        if len(sentence) > 0:
            ingredients.append(sentence)
    print(item['strMeal'])
    print(ingredients)
    print(item['strYoutube'])
    print(item['strInstructions'])
    print(item['strMealThumb'])
    
# random_recipe()

# change vegetarian to make it different category
def first_10_meals_in_category():
    response = requests.get("https://www.themealdb.com/api/json/v1/1/filter.php?c=Vegetarian")

    if response.status_code == 200:
        res = response.json()

    items = res['meals']

    meals = []

    for i in range(0, 10):
        meals.append(items[i]["strMeal"])

    print(meals)


# all categories set up
def categories():
    response = requests.get("https://www.themealdb.com/api/json/v1/1/categories.php")
    
    if response.status_code == 200:
        res=response.json()
    
    items = res["categories"]
    
    categories = []
    
    for category in items:
        categories.append(category["strCategory"])
        print(category["strCategoryThumb"])
    
    print(categories)

# categories()