print('2. feladat')

import random

def vekony(a):
    if a < 220:
        return True
    else:
        return False

true_db_szam = 0

for i in range(200):
    i = random.randint(100,500)
    if vekony(i) == True:
        true_db_szam += 1

print(f'A 200 könyvből {true_db_szam} vékonyabb 220 oldalnál.')
print(f'Ez az összes könyv {round(((true_db_szam/200) * 100),2)}')        