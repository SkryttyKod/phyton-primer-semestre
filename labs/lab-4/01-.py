# 1. Determinar si una palabra ingresada por teclado es una palíndromo.

word = input('Ingrese una palabra ')

word_list = list(word)
rev_word_list = []

for i in word_list:
    rev_word_list.insert(0, i)

print(word_list)
print(rev_word_list)


if word_list == rev_word_list:
    print('La palabra es un palindromo')
else:
    print('La palabra no es un palindromo')