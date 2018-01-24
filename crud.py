from pymongo import MongoClient
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
jsonFile.close()

# clear collection before adding again
db.test.remove()

jsonFile = open('json_palettes.json', 'r')

for line in jsonFile:
    line.strip()
    db.test.insert_many(json.loads(line))

jsonFile.close()
