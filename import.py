#! /usr/bin/python

import fattoriale

print("1 -- Cicli")
print("2 -- Ricorsione")
i = int(input("Come vuoi calcolare il fattoriale?\n"))

if i == 1:
    n = int(input("Inserisci il numero da calcolare\n"))
    print(fattoriale.fatciclo(n))
elif i == 2:
    n = int(input("Inserisci il numero da calcolare\n"))
    print(fattoriale.fatrico(n))
    
