def rechercheElement(element, liste):
    if element in liste:
        return liste.index(element)
    else:
        return False

ma_liste = [1, 2, 3, 4, 99]

resultat1 = rechercheElement(1, ma_liste)
print("Résultat 1 :", resultat1)  

resultat2 = rechercheElement(100, ma_liste)
print("Résultat 2 :", resultat2) 
