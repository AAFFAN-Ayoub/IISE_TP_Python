#EX4
Dictionnaire=dict()

def compte_occurences(liste):
   for mot in liste:
      if mot in Dictionnaire:
          
            Dictionnaire[mot]+=1
      else :
            Dictionnaire[mot]=1
            
   return Dictionnaire     

mots = ["Toyota", "Honda", "Ford", "BMW","Toyota", "Ford","Mercedes", "Audi","Honda", "BMW"]
print(compte_occurences(mots))