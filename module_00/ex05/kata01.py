#!/usr/bin/env python3
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

if len(kata) == 0:
	print("Dictionnary is empty, nothing to print.")

for i, valeur in kata.items():
	print(f"{i} was created by {valeur}")

# for i in kata:
# 	print("{} was created by {}".format(i, kata[i]))