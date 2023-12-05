from connect import *

# -> Inserer une valeur dans la DB.
document={"name":"SpongeBob","age":14, "city":"bikiniBottom"}
collection.insert_one(document)
print("Création réussite !")

# -> Inserer plusieurs valeur dans la base de donnée.
# documents=[
#     {"name":"Patrick","age":26,"city":"bikiniBottom"},
#     {"name":"Picsou","age":58,"city":"donaldVille"},
#     {"name":"Donald","age":28,"city":"donaldVille"}
# ]
# collection.insert_many(documents)
# print("Opération réussite !")