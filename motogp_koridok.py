print('2. feladat')

import random

def gyors_kor(a):
    if a < 105:
        return True
    else:
        return False
    

db_szam = 0

for i in range(120):
    i = random.randint(95,120)
    if gyors_kor(i) == True:
        db_szam += 1

szazalek = (db_szam / 120) * 100

print(f'A 120 körből {db_szam} volt 105 másodpercnél gyorsabb.')
print(f'Ez az összes kör {round(szazalek,2)}%-a.')