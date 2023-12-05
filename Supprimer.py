from connect import*

# -> supprimer un document de la collection

query={"name":"Donald"}
collection.delete_one(query)
print("Suppression réussite !")