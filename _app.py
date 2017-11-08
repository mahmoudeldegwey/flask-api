from flask import Flask,jsonify, request
from f
app = Flask(__name__)

stores = [
    {
        'name':'my wonderful stor',
        'items': [
            {
                'name':'my items',
                'price':'1564'
            }
        ]
    }
]


@app.route('/store',methods=['post'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name']
        'items': []
    }

    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'messages':'store not found'})

@app.route('/stores')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>/item')
def item_in_store(name):
    for store in stores:
        if store['name'] ==  name:
            return jsonify({'items':store['items']})
    return jsonify({'messages':'not found'})


@app.route('/store/<string:name>/item',methods=['post'])
def create_item_in_stores(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)

    return jsonify({'messages':'not found'})


"""


@app.route('/store',method=['post'])
def create_store():
    pass

"""







app.run(port=5000)
