""" Tisknutí vybraných řádků"""
import sys

cisla_radku = sys.argv[1:]

seznam_radku_na_pretisknuti = set()
for cislo in cisla_radku:
    rozsah = cislo.split("-")
    if len(rozsah) > 1:
        seznam_radku_na_pretisknuti.update(range(int(rozsah[0]), int(rozsah[1]) + 1, 1 if len(rozsah) == 2 else int(rozsah[2])))
    else:
        seznam_radku_na_pretisknuti.add(int(cislo))

konec = max(seznam_radku_na_pretisknuti, default=0)
for i, radek in zip(range(1, konec + 1), sys.stdin):
    if i in seznam_radku_na_pretisknuti:
        print(radek, end="")
