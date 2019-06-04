#zmienne globalne i lokalne

#precyzja
x = "{0:.3f}".format(5)
print(x) #5.000
'''
napisz funkcję, która jako argument przyjmuje wartość zlotych i:
* zamienia dane po kursie dzisiejszym franka.
* Wyświetl użytkownikowi ile franków kupi za podaną kwotę.
'''

def plnToChf(value):
    kursChf = 3.81849933
    iloscChf = value // kursChf
    iloscChf = "{0:.0f}".format(iloscChf)
    print(f'Ilość CHF: {iloscChf}')

plnToChf(500)

#zmienna globalna

zmiennaGlobal = 10
print(f'Wartość zmiennej globalnej:{zmiennaGlobal}')
print(f'Id zmiennej globalnej:{id(zmiennaGlobal)}')
def spr():
    global zmiennaGlobal
    zmiennaGlobal = 20
    print(f'\nWartość zmiennej globalnej wewnątrz funkcji:{id(zmiennaGlobal)}')

spr()
print(f'\nId zmiennej globalnej po wywolaniu funkcji:{id(zmiennaGlobal)}')
print(f'\nWartość zmiennej globalnej wewnątrz funkcji:{id(zmiennaGlobal)}')
