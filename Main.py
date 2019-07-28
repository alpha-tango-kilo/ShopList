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

def openYAML(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

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
        print("Invalid args")
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == "-h":
            pass
        elif opt in ("-i", "--input"):
            pass
        elif opt in ("-o", "--output"):
            pass
    
    # Parse args
    recipes = openYAML("./Recipes.yaml")
    print(yaml.load(open("./test.yaml", "r"), Loader = yaml.Loader))

if __name__ == '__main__':
    main(str(sys.argv[1:]))