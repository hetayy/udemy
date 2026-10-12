import json
from pathlib import Path

recipes = []

for file in Path("recipes").glob("*.json"):
    print(file)
    with open(file, "r") as f:
        recipes.append(json.load(f))
