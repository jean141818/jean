def cakes(recipe, available):
    if (len(available)<len(recipe)):
        return 0
    else:
        aux = []
        for clave,valor in available.items():
            for key,value in recipe.items():
                if clave == key:
                   if (value > valor ):
                       return 0
                   else:
                       aux.append(int(valor/value))
        if(len(aux)!= len(recipe)):
            return 0                               
       
    return (aux)
                      
recipe = {'oil': 94, 'eggs': 70, 'flour': 27}
available = {'cream': 938, 'cocoa': 4560, 'oil': 8589, 'chocolate': 3615, 'apples': 358, 'pears': 9374, 'milk': 7313, 'flour': 8543, 'butter': 579, 'nuts': 6230}
print(cakes(recipe,available))