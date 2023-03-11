from flask import Flask, render_template,jsonify
import os
from flask import request
import json
import pymongo
from pymongo import MongoClient
import logging

logging.basicConfig(filename='record.log', level=logging.INFO)
app = Flask(__name__)


def mongo_insert(name,host):
    try:
        app.logger.info("Pymongo Function Start")
        if host=="local":client = MongoClient('mongodb://localhost:27017/');
        elif host=="docker_to_docker":client=MongoClient('mongodb://some-mongo:27017/');
        else:
            client=MongoClient('mongodb://host.docker.intenal:27017/');
            

        db = client["test_db"]
        collection = db["test_collection_docker"]
        status = collection.insert_one(name)
        app.logger.info("Pymongo Function Stops")
    except Exception as e:
        app.logger.info(f"Exception occurred : {e}")



@app.route('/home',methods=['POST','GET'])
def home():
    request_data = request.get_json()
    name = request_data["name"]
    host = request_data["host"]
    mongo_insert(request_data,host)
    return_packet = {"name":name,"status":"success"}
    return jsonify(return_packet)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)