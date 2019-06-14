# -*- coding: utf-8 -*-
import hashlib
import hmac
import base64
import urllib
import urllib.request
import urllib.parse
import time
import json
import gzip

#签名方法
def hash_hmac(key,text):
    temp = hmac.new(key.encode('UTF-8'), text.encode('UTF-8'), hashlib.sha1).digest()
    signature = base64.standard_b64encode(temp)      
    return str(signature, 'UTF-8')

#时间戳
#t = '1535963635'
t = str(int(time.time()))
appid = 'jyo_appid'
requrl = "https://api.jianyu360.com/open"
secret = 'secret&'
keyword = '万达信息股份有限公司'

signature = hash_hmac(secret,'action%3Dgetdata%26appid%3D'+appid+'%26keyword%3D'+urllib.parse.quote(keyword)+'%26pagenum%3D1%26timestamp%3D'+t)


print(signature)

url_data = {'action':'getdata','appid':appid,'keyword':keyword,'pagenum':'1','timestamp':t,'signature':signature}

url_data_urlencode = urllib.parse.urlencode(url_data).encode('UTF-8')

response = urllib.request.urlopen(url = requrl,data =url_data_urlencode)
res_data = response.read()

try:
	data = gzip.decompress(res_data)
	data = str(data,'UTF-8')
	res = json.loads(data)
	print(res)
except:
	print(json.loads(str(res_data,'UTF-8')))