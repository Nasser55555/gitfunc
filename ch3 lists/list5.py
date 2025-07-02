def compter_occurrences(a, L):
    compteur = 0  

    for element in L:
        if element == a:
            compteur += 1
    return compteur

L = [7 , 99 , 5 , 99 , 7 , 19 , 99 , 12 , 29]
a = 99
resultat = compter_occurrences(a, L)

print("L'élément", a, "apparaît", resultat, "fois dans la liste.")
