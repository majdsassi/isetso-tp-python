#Suite de Pell
#Recursive
def Suite_De_Pell_Rec(n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    else :
        return 2*Suite_De_Pell_Rec(n-1) + Suite_De_Pell_Rec(n-2)


#Itertive
def Suite_de_Pell_Iter(n) :
    l = [0,1]
    for i in range (2,n) :
        l.append(l[i-1]*2 + l[i-2])
    return l
n = 10
Suite_de_Pell_Iter(n)
def isTerme(n) :
    i = 0 
    while True :
        if Suite_De_Pell_Rec(i) == n :
            print(f"{n} est un terme de la suite de pell")
            break
        else :
            i+=1
def isTerme_iter(n) :
    i = 0 
    while True :
        terme = Suite_de_Pell_Iter(i)[-1]
        if n == terme  :
            print(n,"est un terme de la suite de pell ")
            break
        else :
            if n  < terme :
                print(n,"n'est pas un terme de la suite de pell")
                break
            else :  i+=1

#isTerme(24)
isTerme_iter(24)
#for i in range(n) :
    #print(Suite_De_Pell(i))

