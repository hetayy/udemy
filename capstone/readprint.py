import json
from pathlib import Path

recipes = []

for file in Path("recipes").glob("*.json"):
    with open(file, "r") as f:
        recipes.append(json.load(f))

#for recipe in recipes:
#    print(recipe["name"])

#print(recipe)
#print(recipe["name"])
#print(recipe["times"]["total_minutes"])
#print(f"Total Cook Time is: {recipe['times']['total_minutes']} minutes")


for recipe in recipes:
    if recipe["name"] == "Chicken Stir Fry":
        for ingredient in recipe["ingredients"]:
            print(f"{ingredient['quantity']} {ingredient['unit']} {ingredient['name']}")


"""
for recipe in recipes:
    if recipe["name"] == "Chicken Stir Fry":
        for ingredient in recipe["ingredients"]:
            print(ingredient)
"""