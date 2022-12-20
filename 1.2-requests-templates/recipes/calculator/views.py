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

def omlet(request):
    number_dishes = int(request.GET.get('servings', '1'))
    rez = {}
    for ingridient, quantity in DATA['omlet'].items():
        rez[ingridient] = quantity * number_dishes
    templates = 'calculator/index.html'
    context = {
        'recipe':
            rez
    }
    return render(request, templates, context)

def pasta(request):
    number_dishes = int(request.GET.get('servings', '1'))
    rez = {}
    for ingridient, quantity in DATA['pasta'].items():
        rez[ingridient] = quantity * number_dishes
    templates = 'calculator/index.html'
    context = {
        'recipe':
            rez
    }
    return render(request, templates, context)

def buter(request):
    number_dishes = int(request.GET.get('servings', '1'))
    rez = {}
    for ingridient, quantity in DATA['buter'].items():
        rez[ingridient] = quantity * number_dishes
    templates = 'calculator/index.html'
    context = {
        'recipe':
            rez
    }
    return render(request, templates, context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
