from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def show_recipe(request, food_type):
    number_of_portions = int(request.GET.get("servings", 1))
    ingredients = DATA.get(food_type)
    copy_ingredients = ingredients.copy()
    copy_ingredients.update((ing, ing_amount * number_of_portions) for ing, ing_amount in copy_ingredients.items())
    context = {'recipe': copy_ingredients}
    return render(request, 'calculator/index.html', context)

