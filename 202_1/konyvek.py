class Konyv():
    def __init__(self, nev, cim, ev, oldalszam, ekonyv):
        self.nev = nev
        self.cim = cim
        self.ev = int(ev)
        self.oldalszam = int(oldalszam)
        self.ekonyv = int(ekonyv)


konyvek = []
with open('202_1/konyvek.txt', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        konyv = Konyv(adatok[0], adatok[1], adatok[2], adatok[3], adatok[4])
        konyvek.append(konyv)

print('3.2 feladat')

print(f'Az állományban {len(konyvek)} db könyv adatai szerepelnek.')

print('3.3 feladat')

legtobb_oldalas_konyv = konyvek[0]

for konyv in konyvek:
    if konyv.oldalszam > legtobb_oldalas_konyv.oldalszam:
        legtobb_oldalas_konyv = konyv

print('A legtöbb oldalas könyv:')
print(f'Szerző: {legtobb_oldalas_konyv.nev}')
print(f'Cím: {legtobb_oldalas_konyv.cim}')
print(f'Kiadás éve: {legtobb_oldalas_konyv.ev}')
print(f'Oldalszám: {legtobb_oldalas_konyv.oldalszam}')

print('3.4 feladat')

szerzo_nev = input('Írjon be egy szerzőnevet: ')

print(f'{szerzo_nev} könyvei:')
for k in konyvek:
    if k.nev == szerzo_nev:
        print(k.cim)

print('3.5 feladat')

ossz_oldalszam = 0

nyomtatott_konyvek_szama = 0

for k in konyvek:
    if k.ekonyv == 0:
        nyomtatott_konyvek_szama += 1
        ossz_oldalszam += k.oldalszam

print(f'A nyomtatott könyvek átlagos oldalszáma {round((ossz_oldalszam / nyomtatott_konyvek_szama),2)}')