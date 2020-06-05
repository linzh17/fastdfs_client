from flask_restful import Api, Resource, reqparse
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from flask import jsonify
import os
from fdfs_client.client import *
from .error_code import *

# 将字典中的byte 类型 转化为str
def convert(data):
    if isinstance(data, bytes):  return data.decode('ascii')
    if isinstance(data, dict):   return dict(map(convert, data.items()))
    if isinstance(data, tuple):  return map(convert, data)
    return data

class File(Resource):

    def post(self):
          parser = reqparse.RequestParser()
          parser.add_argument('file', type=FileStorage, location='files')
          args = parser.parse_args()

          file = args['file']
          #file.save(os.path.join('/home/lin/Desktop/项目练习/fastdfs_client/fastdfsclient/API/', file.filename))
          client_conf = get_tracker_conf(r'/home/lin/Desktop/项目练习/fastdfs_client/fastdfsclient/API/client.conf')
          client = Fdfs_client(client_conf)
          #print(file.read())
          #获取文件后缀
          ext_name = os.path.splitext(file.filename)[-1][1:]
          ret = client.upload_by_buffer(file.read(), file_ext_name = ext_name)

          if ret["Status"] == "Upload successed.":
              ret = jsonify(convert(ret))
              ret.status_code = 201
              return ret
          else: 
              abort(404, message=ERROR_CODE[404])
          
          
          '''
          ret = client.upload_by_filename('/home/lin/Desktop/项目练习/fastdfs_client/fastdfsclient/API/15052410471317.png')
          print(ret)
          '''
     

       