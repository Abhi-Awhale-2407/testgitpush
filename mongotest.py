import pymongo
client =pymongo.MongoClient("mongodb+srv://abhi_2407:Abhi2407@cluster0.qgm88qm.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {
    "name" : "Abhi",
    "email" : "abc@gmail.com",
    "surname" : "Awhale"
}
d = {
    "name" : "Abhi",
    "email" : "abc@gmail.com",
    "surname" : "Awhale"
}
d = {
    "name" : "Abhi",
    "email" : "abc@gmail.com",
    "surname" : "Awhale"
}
d = {
    "name" : "Abhi",
    "email" : "abc@gmail.com",
    "surname" : "Awhale"
}



db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )