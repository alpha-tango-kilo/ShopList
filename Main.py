import yaml

class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name

def openYAML(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def main():
    recipes = openYAML("./Recipes.yaml")

if __name__ == '__main__':
    main()