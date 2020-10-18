#! /usr/bin/python

import fattoriale

print("Cosa vuoi calcolare?")
print("1 -- Somma")
print("2 -- Fattoriale")
h = int(input("Inserisci il valore corrispondente all'operazione che vuoi eseguire:\n"))

if h == 1:
    g = int(input("Primo valore:\n"))
    e = int(input("Secondo valore:\n"))
    print(fattoriale.somma(g,e))
elif h == 2:
    print("1 -- Cicli")
    print("2 -- Ricorsione")
    i = int(input("Come vuoi calcolare il fattoriale?\n"))

    if i == 1:
       n = int(input("Inserisci il numero da calcolare\n"))
       print(fattoriale.fatciclo(n))
    elif i == 2:
       n = int(input("Inserisci il numero da calcolare\n"))
       print(fattoriale.fatrico(n))
    
