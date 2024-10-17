"""1er Methode :  """
a = int(input("donner a : "))
b = int(input("donner b : "))
c = int(input("donner c : "))
if a > b :
    a,b=b,c
if a > c :
    a,c = c,a 
if b > c :
    b,c = c,b
print("Les valuers coroissanre sont  : " ,a,b,c) 
"""" 2eme methode """

l = []
for i in range(3) :
    x = int(input(f"donner {chr(i+97)}  : "))
    l.append(x)
l.sort()
print("Les valuers coroissanre sont : ",end="")
for e in l :
    print(e,end=" ")
""" 3eme"""