from pymongo import MongoClient

# -> connect to mongodb
client=MongoClient('mongodb://localhost:27017')

# -> Determiner la DBase
db=client['maDB']

# -> Determiner la collection.
collection=db['utilisateurs']

print("Connexion établie !")
