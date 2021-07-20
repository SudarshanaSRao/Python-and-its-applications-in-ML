import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import ssl
import json
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
s=0
url=input('Enter location:')
if len(url) < 1:
    url="http://py4e-data.dr-chuck.net/comments_990090.json"
print('Retrieving',url)
uh=urlopen(url,context=ctx).read()
print('Retrieved',len(uh),'characters')
js=json.loads(uh)
print('Count:',len(uh))
S=js["comments"]
for i in S:
    N=int(i["count"])
    s+=N
print('Sum:',s)
