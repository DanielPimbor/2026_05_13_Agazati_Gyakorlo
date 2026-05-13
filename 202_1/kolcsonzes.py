print('1. feladat')

napi_k_d = int(input('A napi kölcsönzési díj: '))

kolcsonzes_hossz = int(input('A kölcsönzés hossza napokban: '))

fizetendo = napi_k_d * kolcsonzes_hossz

print(f'A teljes kölcsönzési díj: {fizetendo}')

if kolcsonzes_hossz > 21:
    print(f'Az olvasónak járó kedvezmény: {int(fizetendo - (napi_k_d * kolcsonzes_hossz) * ((100-12) / 100))}')
else:
    print('Az olvasónak nem jár kedvezmény.')
