from crypt import methods
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

#init flask object
app = Flask(__name__)

#init object flask restful
api = Api(app)

#init object flask cors
CORS(app)

#init variabel bertype dictionary
identitas = {}

#class resource
class ContohResource(Resource):
    #method get 
    def get(self):
        return identitas
    #method post
    def post(self):
        nama = request.form['nama']
        umur = request.form['umur']
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"data": "data berhasil di masukan"}
        return response
    
# setup resource
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5000)

