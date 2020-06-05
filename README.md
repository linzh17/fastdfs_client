## 所需的包

`flask  flask-restful py3Fdfs` 

## 踩坑

### 初始化遇到的错误
```type object argument after ** must be a mapping, not str```

解决方式 ，使用 形如

```client_conf = get_tracker_conf(r’C:\Users\Administrator\PycharmProjects\dailyfresh\utils\fdfs\client.conf’)```

注意 client.conf 必须使用在服务器的绝对路径

### Firestorage 文件内容的读取
使用

```strorage.read()```

注意 因为FileStorage对象是临时文件，对文件的操作只有一次
