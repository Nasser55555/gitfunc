stock = ["Stylo", 25, "Classeur", 100, "Crayon", 12, "Surligneur", 40, "Feutre", 5]
print("Liste initiale :", stock)

noms = []
quantites = []

for item in stock:
    if isinstance(item, str):
        noms.append(item)
    elif isinstance(item, int):
        quantites.append(item)

noms.sort()  
quantites.sort(reverse=True)  
print("Liste des noms triés :", noms)
print("Liste des quantités triées :", quantites)
