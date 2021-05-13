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

if seznam_radku_na_pretisknuti:
    for i, radek in enumerate(sys.stdin, start=1):
        if i in seznam_radku_na_pretisknuti:
            sys.stdout.write(radek)
            seznam_radku_na_pretisknuti.remove(i)
        if not seznam_radku_na_pretisknuti:
            break
