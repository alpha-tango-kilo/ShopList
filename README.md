# ShopList
## Idea
This project was created because I'd always leave something crucial to a recipe out of my shopping list when I was planning what I was going to eat and what I needed to buy. This program aims to provide a commandline tool to solve that problem.

## Features
### Currently Implemented
0. None! :)

### Planned/Possible
1. Shopping list generation
    1. Handling of optional ingredients
    2. Accounting for items you already have
2. Google Tasks integration
3. Recipe creation tool

## How to use
By default, the script will read recipes from `./Recipes.yaml` and save your shopping list to `./ShopList.yaml`

The script is intended to be used as a command line tool, and so usage flags are shown as follows, although none are required:

```
SUPPORTED FLAGS 
    -h | --help                 Help
    -i | --input [file]         Input file (meal plan)
    -o | --output [file]        Output file (shopping list)
```

To add your own recipes, simply edit `Recipes.yaml` (or make your own file), and use the following format:
```yaml
recipe 1:
    ingredients:
        - ingredient 1
        - ingredient 2
        # To use a recipe as an ingredient (meaning that all ingredients of the referenced recipe should be used in this recipe),
        # use the recipe name and end the line with an ampersand (&)
        - recipe 2&
    optional:
        - optional ingredient 1
        - side dish 1
recipe 2:
    ingredients:
        - ingredient 3
        - ingredient 4
```
See `Recipes.yaml` to get a better idea.

Things to note:
* A recipe doesn't have to have both `ingredients` and `optional`, but it must have one
* You can nest as many recipes inside recipes as you like, just don't lead yourself into a feedback loop