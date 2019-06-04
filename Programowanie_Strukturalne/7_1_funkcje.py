#przekazywanie argumentów przez referencję
def show(name):
    print(f'przed modyfikacją: {name}')
    name[0] = 'Beata'
    name[1] = 'Barbara'
    name[2] = 'Bogdan'
    print(f'po modyfikacji: {name}')
    print(f'ID po modyfikacji: {id(name)}')

data = ['Anna', 'Agnieszka', 'Andrzej']
print(f'Przed wywolaniem funkcji show: {data} ')
print(f'Id obiektu show: {id(data)}')
print()
show(data)
print(f'po wywolaniu funkcji show: {data}')

#slownik
print('\n\nslownik')
data1 = {0: 'Artur', 1: 'Andrzej'}
print(f'Id przed modyfikacją: {id(data1)}')
show(data1)

#przekazywanie argumentu przez wartość
print('\n\n')
def show1(city):
    print(f'przed modyfikacją: {city}')
    city[0] = 'Berlin'
    city[1] = 'Londyn'
    print(f'Po modyfikacji: {city}')
    print(f'ID po modyfikacji: {id(city)}')

miasto = ['Gniezno', 'Poznań']

print(f'Przed wywolaniem funkcji show1: {miasto}')
print(f'Id miasto show1: {id(miasto)}')
show1(list(miasto))
print(f'Po wywolaniu funkcji show1: {miasto}')

#slownik II
miasto1 = {
    0: 'Gniezno',
    1: 'Poznań'
}

print(f'\n\nPrzed wywolaniem funkcji show1: {miasto1}')
print(f'Id miasto show1: {id(miasto1)}')
show1(dict(miasto1))
print(f'Po wywolaniu funkcji show1: {miasto1}')

#try except

def div(x, y):
    try:
        result = x / y
        print(f'{x} / {y} = {result}')
    except:
        print('error')


div(2, 4)
