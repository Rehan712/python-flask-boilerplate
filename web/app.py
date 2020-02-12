from flask import Flask,jsonify,request
from flask_restful import Api,Resource
import os
import logging
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

class Register(Resource):
    def post(self):
        postedData = request.get_json()
        username = postedData['username']
        password = postedData['password']

api.add_resource(Register,'/register')

app.run(port=5000)












# from flask import Flask,jsonify,request
# from flask_restful import Api,Resource
# import os
# import logging
# from pymongo import MongoClient

# app = Flask(__name__)
# api = Api(app)
# client = MongoClient('mongodb://db:27017')
# db = client.aNewDB
# UserNum = db['UserNum']

# # UserNum.insert({
# #     'num_of_users':0
# # })

# class Visit(Resource):
#     def get(self):
#         # try:
#             prev_num = UserNum.find({})[0]['num_of_users']
#             logging.info('this is prev numberr',prev_num)
#             new_num =  prev_num + 1
            
#             print(prev_num)
#             UserNum.update({},{'$set':{'num_of_users':new_num}})
#             return str('Hello user' + str(new_num))
#         # except:
#         #     return jsonify({'error':'error comes in query'})
        
        


# class Add(Resource):
#     def post(self):
#         requestData = request.get_json()
#         print(requestData)
#         return jsonify({
#             'sum':requestData['a'] + requestData['b']
#         })
#     def get(self):
#         return jsonify({'success':True})    


# stores = [
#     {
#         'name': 'My Store',
#         'items': [
#             {
#                 'name': 'My Item',
#                 'price': 20
#             }
#         ]
#     }
# ]

# # @app.route('/')
# # def home():
# #     return jsonify(stores)

# @app.route('/store',methods=['POST'])
# def create_store():
#     request_data = request.get_json()
#     new_store = {
#         'name':request_data['name'],
#         'items':[]
#     }
#     stores.append(new_store)
#     return jsonify(new_store)
# @app.route('/store/<string:name>')
# def get_store(name):
#     new_stores = list((store for store in stores if store['name'] == name))
#     if len(new_stores) == 0:
#         return jsonify({'message':'store not founds'})
#     return jsonify({'store':new_stores})  
# @app.route('/store/<string:name>',methods=['POST'])
# def update_store():
#     pass


# @app.route('/store/<string:name>',methods=['POST'])
# def delete_store():
#     pass    

# api.add_resource(Add,'/add')
# api.add_resource(Visit,'/')     
# app.run(port=5000)