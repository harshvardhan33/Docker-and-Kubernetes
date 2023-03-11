from flask import Flask, render_template,jsonify
import os
from flask import request
import json
import logging
import sys

logging.basicConfig(filename='record.log', level=logging.INFO)
app = Flask(__name__)


@app.route('/home',methods=['GET'])
def fetch_data():
    with open("datafolder/data.txt","r") as f:
        data = f.readlines()
    
    return_packet = {"file_content":data}
    return jsonify(return_packet)
    

@app.route('/home',methods=['POST'])
def home():
    request_data = request.get_json()
    name = request_data["name"]
    with open("datafolder/data.txt","a+") as f:
        f.writelines(name+"\n")
    return_packet = {"status":"Data added successfully"}
    return jsonify(return_packet)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)