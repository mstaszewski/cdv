#listy
programowanie = ['PHP', 'Python', 'Java']
print(type(programowanie))
programowanie.append('C#')
programowanie.append('PHP')
print(programowanie)
ile = programowanie.count('PHP')
print(f'ile razy jest PHP: {ile}')

#tuple

imiona = ('Julia', 'Anna', 'Tomek')
print(imiona)
print(type(imiona))

pierwszy = imiona[0]
print(pierwszy)

#slowniki

osoba = {
    'imie':'Julia',
    'nazwisko':'Kowalska',
    'wiek':23
} #tablica asocjacyjna

print(osoba)
print(type(osoba))
print(osoba['imie'])
print(osoba.keys())
print(osoba.get('wzrost', 'brak danych'))

#nowy slownik

'''
    Utwórz slownik i przypisz mu trzy imiona podane z klawiatury
    wyświetl te dane na ekranie w formacie:
    Imie1:...
    Imie2...
    Imie3...
'''
i1 = input('Podaj pierwsze imie: ')
i2 = input('Podaj drugie imie: ')
i3 = input('Podaj trzecie imie: ')

imiona = {
    0:i1,
    1:i2,
    2:i3
}

print(f'imie1: {imiona[0]}')
print(f'imie2: {imiona[1]}')
print(f'imie3: {imiona[2]}')
