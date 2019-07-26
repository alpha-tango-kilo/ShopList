import yaml

def openYAML(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def main():
    recipes = openYAML("./Recipes.yaml")

if __name__ == '__main__':
    main()