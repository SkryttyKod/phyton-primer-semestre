# 4. Disenar un algoritmo que pueda actuar como un cajero, que devuelve y desglosa el vuelto
# en billetes y monedas (pesos chilenos). Utilizando funciones en Python

#=#=#=#=#=#=#=#=#=    INICIO    =#=#=#=#=#=#=#=#=#

def buy():
    while True:
        try:
            buy = int(input('Ingresa el valor de la compra: '))
            if buy < 10:
                print('Ingresa un monto igual o mayor a $10.')
                continue
            elif buy % 10 != 0:
                print('Ingresa un monto multiplo de 10.')
                continue
            else:
                break
        except:
            print('Ingresa un numero valido.')
    while True:
        try:
            pay = int(input('Ingresa el monto con el que pagarás: '))
            if pay < buy:
                print(f'Ingrese un cantidad mayor al valor de la compra. ({buy})')
                continue
            elif pay % 10 != 0:
                print('Ingresa un monto multiplo de 10.')
                continue
            else:
                break
        except:
            print('Ingresa un numero valido.')
        
    amount = pay - buy
    print('\nSu vuelto es: $', amount)
    return amount

def bills_and_coins(amount):
    bills = [20000, 10000, 5000, 2000, 1000]
    coins = [500, 100, 50, 10]
    reg = {}

    if amount > 990:
        for i in bills:
            if amount // i > 0:
                reg[i] = amount // i
                amount -= i * reg[i]

    if amount <= 990:
        for i in coins:
            if amount // i > 0:
                reg[i] = amount // i
                amount -= i * reg[i]
    return reg

def show_screen():
    amount = buy()
    print('\nDesglose:\n')
    for k, v in bills_and_coins(amount).items():
        print('➼  $', k, ' x ', v, sep='')


print('\n##### EJERCICIO 02 #####\n')
show_screen()
print('\n##### FIN EJERCICIO #####\n')

#=#=#=#=#=#=#=#=#=#=    FIN    #=#=#=#=#=#=#=#=#=#=#