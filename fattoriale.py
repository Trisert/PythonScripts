#! /usr/bin/python

def fatrico(n):
    if n == 1:
        return n
    else:
        return n*fatrico(n-1)

def fatciclo(num):
    factorial = 1
    if num < 0:
        print("No esiste")
    elif num == 0:
        print("E' 1")
    else:
        for i in range(1,num+1):
            factorial = factorial*i
        print("Il fattoriale di",num,"è",factorial)
