#! /usr/bin/python

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

n = input("Inserisci una stringa da invertire:\n")
print("La stringa originale è", n)
print("La nuova stringa è", reverse(n))
