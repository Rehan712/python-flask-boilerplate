from flask import Flask,jsonify,request

app = Flask(__name__)


stores = [
    {
        'name': 'My Store',
        'items': [
            {
                'name': 'My Item',
                'price': 20
            }
        ]
    }
]

@app.route('/')
def home():
    return jsonify(stores)

@app.route('/store',methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items':[]
    }
    stores.append(new_store)
    return jsonify(new_store)
@app.route('/store/<string:name>')
def get_store(name):
    new_stores = list((store for store in stores if store['name'] == name))
    if len(new_stores) == 0:
        return jsonify({'message':'store not founds'})
    return jsonify({'store':new_stores})  
@app.route('/store/<string:name>',methods=['POST'])
def update_store():
    pass


@app.route('/store/<string:name>',methods=['POST'])
def delete_store():
    pass    
app.run(port=5000)