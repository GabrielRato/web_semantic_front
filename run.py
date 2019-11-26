import io
import os

import json
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')


@app.route('/store/<search_term>', methods=['POST','GET'])
def search_store(search_term=None):

    response_data = []

    # get all stores than filter...
    r = requests.get('https://ws-music-gallery-system.herokuapp.com/store/get-all')
    if r.status_code == 200:
        data_store = json.loads(r.text)
    else:
        data_store = []

    #look for stores with name like searched
    for store in data_store:
        if search_term in store['name']:
            response_data.append(store)

    # TO-DO draw those pages
    if len(response_data) == 0:
        return render_template('store_not_found.html')
    elif len(response_data) > 1:
        return render_template('store_list.html', store_list=response_data)
    else:
        return render_template('store.html', store_data=response_data)


if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5001, debug=True)
