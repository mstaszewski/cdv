a = input('Podaj pierwszą wartość: ')
b = input('Podaj drugą warość: ')

def div(a, b):
    try:
        result = a / b
        print(f'{result}')
    except:
        print('error')

div(a, b)
