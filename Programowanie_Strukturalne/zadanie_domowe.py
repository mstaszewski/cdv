#Pobieranie danych od użytkownika
Marka = input('Podaj marke pojazdu: ')
Model = input('Podaj model pojazdu: ')
Rocznik = input('Podaj rocznik pojazdu: ')
Pojemnosc = input('Podaj pojemność pojazdu: ')
predkoscMax = input('Podaj maksymalną prędkość pojazdu: ')

#Zapis danych wprowadzonych przez użytkownika
lista = {
0:Marka,
1:Model,
2:Rocznik,
3:Pojemnosc,
4:predkoscMax
}

#Wyświetlenie danych wprowadzonych przez użytkownika
print(f'marka: {lista[0]}')
print(f'model: {lista[1]}')
print(f'rocznik: {lista[2]} r.')
print(f'pojemnosc: {lista[3]}')
print(f'predkoscmax: {lista[4]} KM/H')
