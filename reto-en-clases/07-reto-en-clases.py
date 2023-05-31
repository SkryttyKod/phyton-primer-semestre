
def convert_dict(phrase_list):
    for i in phrase_list:
        diccionary[i] = len(i)

while True:
    try:
        phrase = input('Ingresa una frase: ')
        phrase_empty = phrase.replace(' ', '')
        if not phrase_empty.isalpha():
            print('Ingresa una frase valida')
        else:
            break
    except:
        print('Ingresa una frase valida')

phrase_list = phrase.split()

diccionary = {}

convert_dict(phrase_list)
print(diccionary)