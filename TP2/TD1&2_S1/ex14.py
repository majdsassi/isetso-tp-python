x = int(input("donner x : "))
while x < 1 :
    x = int(input("donner x : "))
for i in range(x) :
    print(" "*i+"*"*(x-i))
