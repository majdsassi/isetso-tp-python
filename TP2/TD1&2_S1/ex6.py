x = int(input("donner x : ")) 
y = int((input("donner y : ")))
choix = int(input("choissir l'operation 1 : +  2 : - , 3 : *  , 4 : /  :  "))
match choix :
    case 1 : 
        print(f" {x} + {y} = {x + y}")
    case 2 :
        print(f" {x} - {y} = {x - y}")
    case 3 :
        print(f" {x} * {y} = {x * y}")
    case 4 :
        if (y == 0) :
            print("il faut y != 0")
        else : 
            print(f" {x} /  {y} = {x / y}")
    case _ :
        print("opertuer invalide ")
        