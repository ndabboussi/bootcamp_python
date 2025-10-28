#!/usr/bin/env python3

# cookbook = {'Sandwich': (['ham', 'bread', 'cheese', 'tomatoes'], 'lunch', '10'),
# 			'Cake': (['flour', 'sugar', 'eggs'], 'dessert', '60'),
# 			'Salad': (['avocado', 'arugula', 'tomatoes', 'spinach'], 'lunch', '15')}

cookbook = {
    'Sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10 },
    'Cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60 },
    'Salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15 }
}


def print_cookbook():
	for i in cookbook.keys():
		print(i)

def print_recipe(name):
	if name in cookbook.keys():
		print("Recipe for {}:".format(name))
		print("Ingredient list: {}".format(cookbook[name]['ingredients']))
		# print()


# def delete_recipe():

# def add_recipe():

print_cookbook()
print_recipe("Cake")
