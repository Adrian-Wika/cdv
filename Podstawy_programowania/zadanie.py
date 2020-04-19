import random

a = eval(input("Podaj poczatek przedzialu: "))
b = eval(input("Podaj koniec przedzialu: "))
x=0
for i in range(5):
    liczba = random.randint(a,b)
    x= x+1
    print("Liczba nr ",x, ": ",liczba)