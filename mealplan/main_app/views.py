from django.shortcuts import render
from django.http import HttpResponse
from chefkoch.recipe import Recipe
from chefkoch.retrievers import SearchRetriever
import json

def home(request):
    return render(request, "main_app/home.html")

def about(request):
    context = {
        "title": "Über uns",
        "content": "Das ist eine Django WebApp Demonstration."
    }
    return render(request, "main_app/about.html", context)

def random(request):
    recipe = Recipe("https://www.chefkoch.de/rezepte/3814751580479131/Pinsa.html")

    retriever = SearchRetriever(
        properties=["Einfach"],
    )
    recipes = retriever.get_recipes(search_query="Lasagne", page=1)
    retriever.close()

    re = json.dumps(
        recipes[0].rating,
        default=lambda o: o.__dict__, 
        sort_keys=True,
        indent=4
    )

    context = {
        "test": re,
    }

    return render(request, "main_app/random.html", context)