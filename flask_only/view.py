from flask import Flask, render_template,jsonify
import os
from flask import request
import json
import logging
import sys

logging.basicConfig(filename='record.log', level=logging.INFO)
app = Flask(__name__)


@app.route('/test',methods=['POST','GET'])
def testing():
    os._exit(0)



@app.route('/home',methods=['POST','GET'])
def home():
    request_data = request.get_json()
    name = request_data["name"]
    host = request_data["host"]
    return_packet = {"name":name,"status":"success"}
    return jsonify(return_packet)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)