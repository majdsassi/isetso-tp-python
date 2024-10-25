from functools import lru_cache
def Saisie() :
    n = int(input("donner n : ( n > 2 ) : "))
    while n < 2 :
        n = int(input("donner n : ( n > 2 ) : "))
    return n
def isPerfect(x) :
    s = 0 
    for i in range(1,x // 2 + 1) :
        if x % i == 0 :
            s+=i 
    return x == s
@lru_cache
def N_Nombres_Parfait(n) :
    i = 1 
    s = 0 
    while s < n :
        if(isPerfect(i)) :
            print(f"{i} est nombre parfait")
            s+=1
        i+=1
n = Saisie()
print(isPerfect(n))
N_Nombres_Parfait(n)