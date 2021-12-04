from pymongo import MongoClient
import gridfs
import io
from PIL import Image


client = MongoClient("")

db = client.products_db
products = db.products
grid_fs = gridfs.GridFS(db)

def saveImage(filename,cat):
    with open(filename, 'rb') as f:
        image = f.read()
    name = filename
    id = grid_fs.put(image, filename = name)
    query = {
        'id':id,
        'name':name ,
        'desc':cat,
    }
    status = products.insert_one(query)
    if status:
        return id
    return jsonify({'result': 'Error occurred during uploading'}),500
    

import os
path = "/Users/musadac/Downloads/images to be uploaded/"
dir_list = os.listdir(path)
print(dir_list)

for i in dir_list:
    id = saveImage(path+i,'rule34')
    print(id)
