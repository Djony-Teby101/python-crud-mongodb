from connect import *

#-> Modifier un document dans la collection.
query={"name":"SpongeBob"}
update={"$set":{"city":"Los Angeles"}}
collection.update_one(query, update)
print("Modification réussite !")