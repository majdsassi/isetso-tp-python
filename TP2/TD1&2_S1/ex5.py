def saisir() :
    x = float(input("donner la moyenne : "))
    while not ( 0 <= x <=20) :
        x = float(input("incorrect re-entre la la moyenne : "))
    return x
n1 = saisir()
n2 = saisir()
n3 = saisir()
l = [n1,n2,n3]
moy = 10 <= ((n1+n2+n3) / 3)
if (9<=min(l)) or ( moy and  8.0 <= min(l)) :
    print("Admisss")
else : print("refusé")
