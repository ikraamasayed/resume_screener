from flask import Flask,jsonify,request,render_template

app = Flask(__name__)

stores = [
    {
        'name' : 'Lenskart',
        'items': [
            {
                'name':'JJ',
                'price':2999
            }
        ]
    }
]

#POST - used to receive data 
#GET - used to send data back only


@app.route('/')
def home():
    return render_template('index.html')


#POST / store data : {name:}
@app.route('/store',methods =['POST'])
def create_store():
    request_data = request.get_json()
    new_store= {
        'name': request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)


#GET /store/<string:name>
@app.route('/store/<string:name>')
@app.route('/store/<string:name>/')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found'})


#GET/stores
@app.route('/store/')
def get_stores():
    return jsonify({'stores': stores}) 
# jsonify({'dukan':stores}) = convert dukan variable into json which has stores list as value


#POST / store/<string:name>/item {name:,price:}
@app.route('/store/<string:name>/item',methods =['POST'])
def create_item_in_stores(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found enter a valid store name'})


#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name :
            return jsonify({'items':store['items']})
    return jsonify({'message':'store not found'})



if __name__ =="__main__":
    app.run(port=5000,debug=True)
    