""" Tisknutí vybraných řádků"""
import sys

cisla_radku = sys.argv[1:]

for i, radek in enumerate(sys.stdin):
    cislo_aktualniho_radku = i + 1
    if str(cislo_aktualniho_radku) in cisla_radku:
        print(radek, end="")
