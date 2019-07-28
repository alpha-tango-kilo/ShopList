import yaml     # handling YAML
import getopt   # parsing args
import sys      # getting args
import os       # validating args

from utils.pathValidate import is_path_exists_or_creatable as validatePath # validating args

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
    # Parse args
    """
    SUPPORTED FLAGS 
    -h | --help                 Help
    -i | --input [file]         Input file (meal plan)
    -o | --output [file]        Output file (shopping list)
    """
    try:
        optList, args = getopt.getopt(sys.argv[1:], "hi:o:", ["input=", "output="])
    except getopt.GetoptError:
        print("Invalid args, use -h for help")
        sys.exit(2)
    
    for opt, arg in optList:
        if opt in ("-h", "--help"):
            help(main)
            sys.exit(0)
        elif opt in ("-i", "--input"):
            if os.path.exists(arg):
                INFILE = arg
            else:
                raise ValueError("Input file not found / Path invalid. Use -h for help")
        elif opt in ("-o", "--output"):
            if validatePath(arg):
                OUTFILE = arg
            else:
                raise ValueError("Invalid output path. Use -h for help")
    
    # Parse args
    recipes = openRecipes(INFILE)
    print(recipes)

if __name__ == '__main__':
    main()