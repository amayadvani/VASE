from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model_symptoms import *

diagnosis_api = Blueprint('diagnosis_api', __name__,
                   url_prefix='/api/diagnosis')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
d_api = Api(diagnosis_api)

class DiagnosisAPI:
    # not implemented
    class _Create(Resource):
        def post(self, diagnosis):
            pass

    # postSymptoms()
    class _GetDiagnosis(Resource):
        def get(self, symp_list):
            symps = symp_list.split(',')
            symp_index = []
            for s in symps:
                symp_index.append(symptoms_database.index(s.strip()))
            return get_diagnosis(symp_index)

    # getSymptoms()
    class _ReadSymptoms(Resource):
        def get(self):
            return jsonify(get_symptoms())
    
    # getDiagnosis()
    class _ReadDiagnosis(Resource):
        def get(self):
            return jsonify(get_all_diagnosis())
    
    class _ReadTreatments(Resource):
        def get(self):
            return jsonify(get_treatment())

    # building RESTapi resources/interfaces, these routes are added to Web Server
    d_api.add_resource(_Create, '/create/<string:diagnosis>')
    d_api.add_resource(_ReadSymptoms, '/symptoms')
    d_api.add_resource(_ReadDiagnosis, '/')
    d_api.add_resource(_ReadTreatments, '/treatments')
    d_api.add_resource(_GetDiagnosis, '/diagnosis/<string:symp_list>')
    
# if __name__ == "__main__": 
#     # server = "http://127.0.0.1:5000" # run local
#     server = 'https://flask.nighthawkcodingsociety.com' # run from web
#     url = server + "/api/jokes"
#     responses = []  # responses list

#     # get count of jokes on server
#     count_response = requests.get(url+"/count")
#     count_json = count_response.json()
#     count = count_json['count']

#     # update likes/dislikes test sequence
#     num = str(random.randint(0, count-1)) # test a random record
#     responses.append(
#         requests.get(url+"/"+num)  # read joke by id
#         ) 
#     responses.append(
#         requests.put(url+"/like/"+num) # add to like count
#         ) 
#     responses.append(
#         requests.put(url+"/jeer/"+num) # add to jeer count
#         ) 

#     # obtain a random joke
#     responses.append(
#         requests.get(url+"/random")  # read a random joke
#         ) 

#     # cycle through responses
#     for response in responses:
#         print(response)
#         try:
#             print(response.json())
#         except:
#             print("unknown error")

        