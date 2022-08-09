from flask import Flask
from pymongo import MongoClient



client= MongoClient("mongodb://127.0.0.1:27017/lw")
db = client.lw

app = Flask(__name__)

from main import routes 