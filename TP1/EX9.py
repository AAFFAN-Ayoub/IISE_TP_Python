#EX9
def analyse_texte(texte):
   
    nombre_caracteres = len(texte.replace(" ", ""))
   
    nombre_mots = len(texte.split())
    return {
        "nombre_mots": nombre_mots,
        "nombre_caracteres": nombre_caracteres
    }
resultat = analyse_texte("Bonjour comment cava je t'ai apple mais  tu n'as pas repondu")
print(resultat) 