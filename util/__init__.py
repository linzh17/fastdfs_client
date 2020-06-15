
import json
import requests
import hashlib


def Md5Content(content):
    m = hashlib.md5()
    m.update(content)
    return m.hexdigest()



def Generate_UUID(Ret):
    restcontent = json.dumps(Ret)
    m = hashlib.md5()
    m.update(restcontent.encode('utf-8'))
    return m.hexdigest()


def sendMsg(UUID, Url, FileMd5, Size, StorageIP, RemoteFileId, GroupName):
    url = "http://47.113.185.200/traffic/" + UUID

    ParametersData = {
        "Url": Url,
        "FileMd5": FileMd5,
        "Size": Size,
        "StorageIP": StorageIP,
        "RemoteFileId": RemoteFileId,
        "GroupName": GroupName
    }

    response = requests.put(url, data=ParametersData)
    result = response.json()
    return result



Test = {
    "UUID": "UUID12345667",
    "Url": "http://47.113.225.179/scnu/group1/M00/00/00/L3Hhs17kxH-AUDyAAAQKtTOy9SE304.jpg",
    "FileMd5": "01af48bd2d8a94d3e39a3a6f521ee41c",
    "Size": "258.68KB",
    "StorageIP": "47.113.225.179",
    "RemoteFileId": "group1/M00/00/00/L3Hhs17kxH-AUDyAAAQKtTOy9SE304.jpg",
    "GroupName": "group1",
    "tsHash": "0x15df3c7cea6498518265d08fee6e74dd8876e6d83a3892326c6788f3b77acea3"
}


if __name__ == '__main__':
    response = sendMsg(Test["UUID"], Test["Url"], Test["FileMd5"], Test["Size"], Test["StorageIP"], Test["RemoteFileId"], Test["GroupName"])
    print (response.status_code)
    print (response.json())












