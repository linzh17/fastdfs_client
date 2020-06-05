from flask import Flask
from flask_restful import Api
from API import *


app =  Flask(__name__)
api = Api(app)

api.add_resource(File,'/api/fdfsfile')

if __name__ =='__main__':
    app.run()
