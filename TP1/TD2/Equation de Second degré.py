from math import sqrt 

a = float(input("Donner a : "))
b = float(input("Donner b : "))
c = float(input("Donner c : "))

while c == 0:
    c = float(input("Donner c (ne peut pas être zéro) : "))

delta = b**2 - 4 * a * c

if delta < 0:
    print("Pas de solution dans R")
elif delta > 0:
    sol1 = (-b - sqrt(delta)) / (2 * a)
    sol2 = (-b + sqrt(delta)) / (2 * a)
    print(f"Il existe deux solutions : Sol1 : {sol1} Sol2 : {sol2}")
else:
    sol = -b / (2 * a)
    print(f"Il existe une seule solution : {sol}")