n = int(input("nombre de personnes: "))
oeufs =  int(3 * n/4) # calculer le Nombre Des Oeufs nesssaire pour n personnes
chocolat =  int(100 * n/4) # Calculer la Contite de choccolate nesseaine pour n Personnes
sucre_vanille = max(int(n / 4), 1) # Calculer la Contite de Sucre vannlle  nesseaine pour n Personnes
print("nombre d'oeufs ", oeufs)
print("quantité de chocolat (g): ", chocolat)
print("quantité de sucre_vanillé", sucre_vanille)
print("----------------Version ameliorée-------------------------")
print(f"nombre d'oeufs {int(3 * n/4)}\nquantité de chocolat (g): {int(100 * n/4)}\nquantité de sucre_vanillé {max(int(n / 4), 1)}" )



