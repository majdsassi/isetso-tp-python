while True : 
    ai = float(input("donner anicien index : "))
    if ai > 0 : break
while True :
    ni = float(input("donner n index : "))
    if ni > ai  : break

dif = ni - ai
if dif <= 100 :
    equation = 0.2 * dif
elif  100 < dif <= 250 :
    equation = 100 * 0.2 + (dif - 100 * 0.3)
else :
    equation = (100 * 0.2) + (150 * 0.3) + ((dif - 250) * 0.4)
equation = (equation + 25 ) *  1.1
print(f"Le montant est {equation:.3f} DT")
####################################################################

    