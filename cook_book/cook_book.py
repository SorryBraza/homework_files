with open('cook_book/recipes.txt', 'rt') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ing_count = int(file.readline())
        ingredients =[]
        for _ in range(ing_count):
            ing = file.readline()
            ing_name, q, m = ing.strip().split(' | ')
            ingredient = {
                'ingredient_name': ing_name,
                'quantity': q,
                'measure': m
            }
            ingredients.append(ingredient)
        file.readline()
        cook_book[dish_name] = ingredients


def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for ing in cook_book[dish]:
                if ing['ingredient_name'] in result:
                    result[ing['ingredient_name']]['quantity'] \
                        += int(ing['quantity']) * person_count
                else:
                    result[ing['ingredient_name']] = \
                     {'measure': ing['measure'], 
                      'quantity': int(ing['quantity']) * person_count}
        else:
            return 'Нет блюда в книге рецептов'
    return result
