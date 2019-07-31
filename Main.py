import yaml     # handling YAML
import getopt   # parsing args
import sys      # getting args
import os       # validating args

from utils.pathValidate import is_path_exists_or_creatable as validatePath # validating args
from utils.easyFlags import *

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

def main():
    INFILE = "./Recipes.yaml" # Read recipes from here
    OUTFILE = "./ShopList.yaml" # Save shopping list to here
    # Arg functions
    def helpFunc():
        print("""
SUPPORTED FLAGS 
-h | --help                 Help
-i | --input [file]         Input file (meal plan)
-o | --output [file]        Output file (shopping list)
        """)
        sys.exit(0)
    
    def inFunc(arg):
        if os.path.exists(arg):
            global INFILE
            INFILE = arg
        else:
            raise ValueError("Input file not found / Path invalid. Use -h for help")
        
    def outFunc(arg):
        if validatePath(arg):
            global OUTFILE
            OUTFILE = arg
        else:
            raise ValueError("Invalid output path. Use -h for help")
    
    # Parse args
    argHandler = EasyArgHandler([EasyFlag("h", helpFunc, long = "help", isHelpCommand = True),
                                 EasyFlag("i", inFunc, long = "input", needsArg = True),
                                 EasyFlag("o", outFunc, long = "output", needsArg = True)])
    argHandler.handleArgs(sys.argv[1:])
    
    # Load recipes
    recipes = openRecipes(INFILE)
    print(recipes)

if __name__ == '__main__':
    main()