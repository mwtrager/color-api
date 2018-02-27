from pymongo import MongoClient
import pymongo
from pprint import pprint
import csv
import json
import os

# get creds from environment variables
if "COLOR_USER" and "COLOR_PW" in os.environ:
    coloruser = os.environ["COLOR_USER"]
    colorpw = os.environ["COLOR_PW"]
else:
    print('no creds')

# connect to db
client = MongoClient('mongodb://'+coloruser+':'+colorpw+'@localhost/color')
db=client.color

csvFile = open('palettes.csv', 'r')
jsonFile = open('json_palettes.json', 'w')

fieldnames = ['c1', 'c2', 'c3', 'c4']
reader = csv.DictReader(csvFile, fieldnames)
out = json.dumps([row for row in reader])
jsonFile.write(out)
csvFile.close()

# drop contents of collection and recreate index on empty db (testing)
db.test.remove()
try:
    db.test.drop_index('paletteIndex')
    db.test.create_index([("c1", pymongo.ASCENDING), ("c2", pymongo.ASCENDING), ("c3", pymongo.ASCENDING), ("c4", pymongo.ASCENDING)], unique=True, name="paletteIndex")
except: # NOTE this is bad
    print('error hit')

# prep input JSON object (line) and insert_many
jsonFile = open('json_palettes.json', 'r')
line = jsonFile.readline()
line.strip()
try:
    # NOTE without ordered=False, encountering a dupe will STOP remaining inserts in the queue
    # with ordered=False, mongod be able to move on. i think it's recommended to always use this with insert_many
    result = db.test.insert_many(json.loads(line), ordered=False)
except pymongo.errors.BulkWriteError as e:
    print('Error during insert_many()...')
    pprint(e.details['writeErrors'])
jsonFile.close()

# test query...
docs = db.test.find({"c4": "#eeeeee"})
for doc in docs:
    print(doc)

# close connection
client.close()
