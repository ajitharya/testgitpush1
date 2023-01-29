import pymongo

client = pymongo.MongoClient('mongodb+srv://ajitharya91:Mongodb1@cluster0.w1lyzut.mongodb.net/?retryWrites=true&w=majority')
mydb =client.test
print(mydb)

d = {
    "name":"AjithArya",
    "email":"arya@ineuron.ai",
    "company":"yazaki"
}
db1 = client['mongodbtest']
coll = db1['test1']
coll.insert_one(d)
