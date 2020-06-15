from flask_restful import Api, Resource, reqparse
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from flask import jsonify
import os
from fdfs_client.client import *
from .error_code import *
from util import Generate_UUID, sendMsg, Md5Content

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
          client_conf = get_tracker_conf(r'/root/fastdfs_client/API/client.conf')
          client = Fdfs_client(client_conf)
          #print(file.read())
          #获取文件后缀
          ext_name = os.path.splitext(file.filename)[-1][1:]
          FileContent = file.read()
          ret = client.upload_by_buffer(FileContent, file_ext_name = ext_name)
          ret = convert(ret)

          Url = "http://47.113.225.179/scnu/" + ret["Remote file_id"]
          UUID = Generate_UUID(ret)
          FileMd5 = Md5Content(FileContent)
          Size = ret["Uploaded size"]
          StorageIP = ret["Storage IP"]
          RemoteFileId = ret["Remote file_id"]
          GroupName = ret["Group name"]

          result = sendMsg(UUID, Url, FileMd5, Size, StorageIP, RemoteFileId, GroupName)

          if ret["Status"] == "Upload successed.":
              ret = jsonify(result)
              ret.status_code = 201
              return ret
          else: 
              abort(404, message=ERROR_CODE[404])
          
          
          '''
          ret = client.upload_by_filename('/home/lin/Desktop/项目练习/fastdfs_client/fastdfsclient/API/15052410471317.png')
          print(ret)
          '''
     

       
