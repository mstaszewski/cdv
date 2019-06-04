# wprowadzanie wartości przez użytkownika
marka = input('Podaj markę pojazdu: ')
rocznik = input('Podaj rocznik produkcji pojazdu: ')
pojemnosc = input('Podaj pojemnosc pojazdu: ')
predkoscmax = input('Podaj prędkość maksymalną pojazdu: ')

#odczyt danych przez system i zapisanie w liście
lista = {
0:marka,
1:rocznik,
2:pojemnosc,
3:predkoscmax
}

#wyświetlenie zawartości wprowadzonej przez użytkownika
print(f'marka: {lista[0]}')
print(f'rocznik: {lista[1]} r.')
print(f'pojemnosc: {lista[2]}')
print(f'predkoscmax: {lista[3]} KM/H')
