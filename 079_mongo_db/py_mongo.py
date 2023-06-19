import pymongo

client = pymongo.MongoClient("mongodb://secret:secret@localhost:27017/admin?ssl=false&authSource=admin")

db = client.blog

post = {"autor": "Martin",
        "titulo": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"]}

posts = db.posts
post_id = posts.insert_one(post).inserted_id

# imprime el id el post recién insertado.
print(post_id)
# imprime el número de elementos en la colección posts.
print(posts.count_documents({}))
