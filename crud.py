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

# don't need this anymore
csvFile.close()

# clear collection before adding again
db.test.remove()

jsonFile = open('json_palettes.json', 'r')
line = jsonFile.readline()
line.strip()


# create the index, order matters
db.test.create_index([("c1", pymongo.ASCENDING), ("c2", pymongo.ASCENDING), ("c3", pymongo.ASCENDING), ("c4", pymongo.ASCENDING)], unique=True, name="paletteIndex")

# NOTE catches all errors, but we want to change this to ignore duplicates
try:
  result = db.test.insert_many(json.loads(line))
except pymongo.errors.BulkWriteError as e:
  print(e.details['writeErrors'])

# close jsonFile
jsonFile.close()
