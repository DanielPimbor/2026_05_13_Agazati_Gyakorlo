print('1. feladat')

teljesitendo_korok = int(input('Körök száma: '))

korre_eso_atlagos_fogy = float(input('Átlagos fogyasztás körönként (liter): '))

tartaly = int(input('A tartály mérete (liter): '))

szukseges_uzemanyag = teljesitendo_korok * korre_eso_atlagos_fogy

print(f'A versenyhez szükséges üzemanyag: {szukseges_uzemanyag} liter.')

if szukseges_uzemanyag <= tartaly:
    print('A tartály elegendő a versenyyhez.')
else:
    print(f'A tartály NEM elegendő! Még {szukseges_uzemanyag - tartaly} liter üzemanyag szükséges.')