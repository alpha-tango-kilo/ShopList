import yaml     # handling YAML
import getopt   # parsing args
import sys      # getting args

class Recipe:
    def __init__(self, name, ingredients = [], optional = []):
        self.name = name
        self.ingredients = ingredients
        self.optional = optional
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name

def openRecipes(path = "./Recipes.yaml"):
    def openYAML(filePath):
        with open(filePath, "r") as f:
            return yaml.safe_load(f)
    
    rawYAML = openYAML(path)
    recipes = []
    for recipe, ingCategories in rawYAML.items():
        try:
            ingredients = ingCategories["ingredients"]
        except KeyError:
            ingredients = []
        try:
            optionals = ingCategories["optional"]
        except KeyError:
            if not ingredients:
                raise RuntimeError("Found recipe with no ingredients or optionals, exiting...") from KeyError
            optionals = []
        recipes.append(Recipe(recipe, ingredients, optionals))
        
    return recipes

def main(sysArgs):
    # Parse args
    """
    SUPPORTED ARGS 
    -h                          Help
    -i | --input [file]         Input file (meal plan)
    -o | --output [file]        Output file (shopping list)
    """
    try:
        opts, args = getopt.getopt(sysArgs, "hi:o:", ["input=", "output="])
    except getopt.GetoptError:
        print("Invalid args, use -h for help")
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == "-h":
            pass
        elif opt in ("-i", "--input"):
            pass
        elif opt in ("-o", "--output"):
            pass
    
    # Parse args
    recipes = openRecipes("./Recipes.yaml")
    print(recipes)

if __name__ == '__main__':
    main(str(sys.argv[1:]))