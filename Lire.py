from connect import *

#-> Trouver un document avec le nom.

query={"name":"SpongeBob"}
document=collection.find_one(query)
print("Utilisateur Trouvé !")
print(type(document))
print(document)

#-> Trouver tous les documents contenus dans la collection.

# documents=collection.find()

# for element in documents:
#     print(element)