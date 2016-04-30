class Recipe:
    name = "";
    ingredients = []
    def __init__(self, rec_name):
        self.name = rec_name

    def add_ingredient(self, ing_name, ing_qnty):
        self.ingredients.append([])
        self.ingredients[len(ingredients) - 1].append(ing_name)
        self.ingredients[len(ingredients) - 1].append(ing_qnty)

    def return_recipe_name(self):
        return(self.name)

    def return_ingredient_name(self, index):
        return(self.ingredients[index][0])

    def return_ingredient_qnty(self, index):
        return(self.ingredients[index][1])
