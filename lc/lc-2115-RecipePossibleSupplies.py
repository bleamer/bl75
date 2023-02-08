#lc 2115. Find All Possible Recipes from Given Supplies

from collections import defaultdict

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        # recipes  = []
        # ingredients = [i] [a, b, c]
        # recipes [j] = c
        # supplies = [ a, d, f]

        ingRecMap = defaultdict(list) # For each ingreditne waht all recipes can be made
        depIngredCount = defaultdict(int) # dependent recipe ingredient count

        for recipe, ingredient in zip(recipes, ingredients):
            depIngredCount[recipe] = len(ingredient)

            for ingred in ingredient:
                ingRecMap[ingred].append(recipe)
        possRecipe = []

        queue = deque(supplies)
        recipess = set(recipes)

        while queue:
            # iterate through all ingredients / supplies
            supply = queue.popleft()
            if supply in recipess:
                possRecipe.append(supply)
            # for all receipes dependent on this supply, since now we have the supply
            for recipe in ingRecMap[supply]:
                # reduce the number of dependencies
                depIngredCount[recipe] -= 1
                # if for a given receipe all requirement are satisfied, make it available to others
                if depIngredCount[recipe] == 0:
                    queue.append(recipe)
        
        return possRecipe
