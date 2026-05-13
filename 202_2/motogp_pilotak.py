print('3. feladat')

pilotak = []
with open('pilottak.txt', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        pilota = {'nev': adatok[0],'csapat': adatok[1], 'nemzetiseg': adatok[2], 'rajtszam': int(adatok[3]),'osszpontszam': int(adatok[4])  }
        pilotak.append(pilota)

print('3.2 feladat')

print(f'Az állományban {len(pilotak)} pilóta adatai szerepelnek.')

print('3.3 feladat')


legtobb_pontot_szerzo = pilotak[0]

for pilota in pilotak:
    if pilota['osszpontszam'] > legtobb_pontot_szerzo['osszpontszam']:
        legtobb_pontot_szerzo = pilota

print('A legtöbb pontot szerző pilóta:')
print(f'Név: {legtobb_pontot_szerzo['nev']}')
print(f'Csapat: {legtobb_pontot_szerzo['csapat']}')
print(f'Nemzetiség: {legtobb_pontot_szerzo['nemzetiseg']}')
print(f'Rajtszám: {legtobb_pontot_szerzo['rajtszam']}')
print(f'Pontszám: {legtobb_pontot_szerzo['osszpontszam']}')


print('3.4 feladat')

csapat_nev = input('Írjon be egy csapatnevet: ')

print(f'A {csapat_nev} pilótái.')

for pilota in pilotak:
    if pilota['csapat'] == csapat_nev:
        print(pilota['nev'])

print('3.5 feladat')

spanyol_pilotak_szama = 0

spanyol_pilotak_osszpontszama = 0

for i in pilotak:
    if i['nemzetiseg'] == 'spanyol':
        spanyol_pilotak_szama += 1
        spanyol_pilotak_osszpontszama += i['osszpontszam']

print(f'A spanyol pilóták átlagos ponszáma {round((spanyol_pilotak_osszpontszama / spanyol_pilotak_szama),2)} pont. ')        