a = int(input("donner une anneé : "))
while not(a >=0 ) :
     a = int(input("donner une anneé : "))
print("---------------------solution Composeé--------------------")
if ((a % 400) == 0) :
    print(f"{a} est une année bissextile.")
elif (a % 4 == 0): 
    print(f"{a} est une année bissextile.")
elif ((a % 100 == 0)) :
    print(f"{a} n'est une année bissextile.")
else : 
    print(f"{a} n'est une année bissextile.")

print("-------------Solution Alternatif----------------------")

if (a%400==0 or a % 4 == 0 and a % 100 !=  0) : 
    print(f"{a} est une année bissextile.")
    
else : 
    print(f"{a} n'est une année bissextile.\n")
    