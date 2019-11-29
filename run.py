import io
import os

import json
from flask import Flask, request, jsonify, render_template, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')


@app.route('/store/<search_term>', methods=['POST','GET'])
def search_store(search_term=None):

    response_data = []
    print(10101)
    # get all stores than filter...
    r = requests.get('https://ws-music-gallery-system.herokuapp.com/store/get-all')
    if r.status_code == 200:
        data_store = json.loads(r.text)
    else:
        data_store = []
    #look for stores with name like searched
    for store in data_store:
        if search_term.lower() in store['name'].lower():
            response_data.append(store)
    print(response_data)
    # TO-DO draw those pages
    if len(response_data) == 0:
        return render_template('store_not_found.html')
    elif len(response_data) > 1:
        return render_template('store_list.html', store_list=response_data)
    else:
        return redirect(url_for('store_products', store_name=response_data[0]['name']))
        #return render_template('store.html', store_data=response_data)

@app.route('/store_products/<store_name>', methods=['POST','GET'])
def store_products(store_name=None):
    req = requests.get('https://ws-music-gallery-system.herokuapp.com/get-products/'+store_name)
    if req.status_code == 200:
        store_product = json.loads(req.text)
    else:
        store_product = []

    req = """  {
    "name": "Camiseta Branca",
    "typeProductAndBusiness": "CLOTHING",
    "branch": "Levis",
    "price": 80,
    "soldByStore": {
      "name": "All Rock TShirts",
      "typeBusiness": "CLOTHING",
      "uri": "nullAllRockTshirts"
    },
    "size": "P",
    "designatedGender": "MALE",
    "mainColor": "Branca",
    "typeOfFiber": "Algodão",
    "uri": null
  },
  {
  "name": "Camiseta Branca",
  "typeProductAndBusiness": "CLOTHING",
  "branch": "Levis",
  "price": 80,
  "soldByStore": {
    "name": "All Rock TShirts",
    "typeBusiness": "CLOTHING",
    "uri": "nullAllRockTshirts"
  },
  "size": "P",
  "designatedGender": "MALE",
  "mainColor": "Branca",
  "typeOfFiber": "Algodão",
  "uri": null
}"""
    store_product = json.loads(req)
    print (store_product)

    return render_template('stores.html', store_product=store_product)




if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5001, debug=True)
