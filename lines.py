""" Tisknutí vybraných řádků"""
import sys

cisla_radku = sys.argv[1:]

seznam_radku_na_pretisknuti = []
for i, cislo in enumerate(cisla_radku):
    if len(cislo) > 1:
        rozsah = cislo.split("-")
        if rozsah[1] < rozsah[0]:
            pass
        else:
            for y in range(int(rozsah[0]), int(rozsah[1]) + 1, 1 if len(rozsah) == 2 else int(rozsah[2])):
                seznam_radku_na_pretisknuti.append(str(y))
    else:
        seznam_radku_na_pretisknuti.append(cislo)

if seznam_radku_na_pretisknuti:
    for i, radek in enumerate(sys.stdin):
        cislo_aktualniho_radku = i + 1
        if str(cislo_aktualniho_radku) in seznam_radku_na_pretisknuti:
            print(radek, end="")
            seznam_radku_na_pretisknuti.remove(str(cislo_aktualniho_radku))
        if not seznam_radku_na_pretisknuti:
            break
