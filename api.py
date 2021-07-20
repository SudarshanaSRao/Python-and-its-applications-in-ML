import urllib.request, urllib.parse, urllib.error
import json
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
serviceurl="http://py4e-data.dr-chuck.net/json?"
data_address='Universidad de Buenos Aires'
parameters={"key":42,"address":data_address}
paramsurl=urllib.parse.urlencode(parameters)
queryurl=serviceurl+paramsurl
print("Data URL:",queryurl)
data=urllib.request.urlopen(queryurl,context=ctx).read()
data_read=data.decode()
jsondata=json.loads(data_read)
place_id=jsondata["results"][0]["place_id"]
print("Place ID:",place_id)
