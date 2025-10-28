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
	print("\nAvailable recipe(s):")
	for i in cookbook.keys():
		print(i)


def print_recipe(name):
    if name in cookbook.keys():
        print("\nRecipe for {}:".format(name))
        print("\tIngredient list: {}".format(cookbook[name]['ingredients']))
        print("\tTo be eaten for {}.".format(cookbook[name]['meal']))
        print("\tTakes {} minutes of cooking.".format(cookbook[name]['prep_time']))
    else:
        print("\tError: invalid recipe name.")


def delete_recipe(name):
    if name in cookbook.keys():
        cookbook.pop(name, None)
        print("\n\tSuccesfully deleted {} recipe.".format(name))
    else:
        print("\n\tError: invalid recipe name.")


# def add_recipe():

def print_menu():
    print("Please select an option by typing the corresponding number:")
    print("\t1: Add a recipe")
    print("\t2: Delete a recipe")
    print("\t3: Print a recipe")
    print("\t4: Print the cookbook")
    print("\t5: Quit\n")



print("\Welcome to the Python Cookbook !")
while (True):
    print_menu()
    choice = input("Please select an option:\n")

    if choice == '1':
        add_recipe()
    elif choice == '2':
        name = input("Please enter a recipe name to get its details:")
        delete_recipe(name)
    elif choice == '3':
        name = input("Please enter a recipe name to delete:")
        print_recipe(name)
    elif choice == '4':
        print_cookbook()
    elif choice == '5':
        print("Closed cookbook, see yah!")
        break
    else:
        print("Sorry, this option does not exist.")

# def add_recipe(name, ingredients, meal, time):
#     if name in cookbook.keys():
#         print("'{}' already exists, overwriting...".format(name))
#     cookbook[name] = (ingredients, meal, time)
#     print("Added '{}' to cookbook.".format(name))


# def print_all():
#     for x in cookbook.keys():
#         print_recipe(x)
#         print()


# cookbook = {'sandwich': (['ham', 'bread', 'cheese', 'tomatoes'],
#             'lunch', '10'),
#             'cake': (['flour', 'sugar', 'eggs'], 'dessert', '60'),
#             'salad': (['avocado', 'arugula', 'tomatoes', 'spinach'],
#                       'lunch', '15')}

# choice = 0
# while not choice == 5:
#     print("Please select an option by typing the corresponding number:")
#     print("1: Add a recipe")
#     print("2: Delete a recipe")
#     print("3: Print a recipe")
#     print("4: Print the cookbook")
#     print("5: Quit")
#     print(">> ", end="")
#     sys.stdout.flush()
#     try:
#         choice = int(sys.stdin.readline())
#     except ValueError:
#         choice = 0
#     print("")
#     if choice == 1:
#         name = input("Enter the name of the recipe you'd like to add: ")
#         ingredients = input("Enter the ingredients in the format "
#                             "'bread,butter,jam...': ").split(',')
#         meal = input("Enter the type of meal (lunch, dessert...): ")
#         time = input("Enter the recipe's prep time, in minutes: ")
#         add_recipe(name, ingredients, meal, time)
#     elif choice == 2:
#         name = input("Enter the name of the recipe you'd like to delete: ")
#         del_recipe(name)
#     elif choice == 3:
#         name = input("Please enter the recipe's name to get its details: ")
#         print_recipe(name)
#     elif choice == 4:
#         print_all()
#     elif choice == 5:
#         print("Cookbook closed.")
#     else:
#         print("This option does not exist.")
#     print()