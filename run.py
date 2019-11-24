import io
import os

import json
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')


@app.route('/store/<store_id>', methods=['POST','GET'])
@app.route('/store/', methods=['POST','GET'])
def store(store_id=None):
    #TO-DO implementar logica para tratar o id, buscando do Aug
    return render_template('stores.html')


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5001, debug=True)
