n = int(input('donner n : '))
terme = 1
terme_p = 0 
for i in range (n) :
    terme_n = terme + terme_p
    terme_p , terme = terme , terme_n
    print(terme_n,end="|")

