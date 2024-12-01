#EX10
def fusionner_dicts(dict1, dict2):

    fusion = dict(dict1)
    
    for clé, valeur in dict2.items():
        
        if clé in fusion:
            fusion[clé] += valeur
        else:
            
            fusion[clé] = valeur
    
    return fusion

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 3, "c": 4, "d": 5}

resultat = fusionner_dicts(dict1, dict2)
print(resultat)