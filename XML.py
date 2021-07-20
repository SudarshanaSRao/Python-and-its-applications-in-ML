import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
s=0
address=input('Enter location:')
if len(address) < 1:
    address='http://py4e-data.dr-chuck.net/comments_990089.xml'
print('Retrieving',address)
uh=urlopen(address,context=ctx).read()
print('Retrieved',len(uh),'characters')
tree=ET.fromstring(uh)
results=tree.findall('.//count')
print('Count:',len(results))
for i in results:
    s+=int(i.text)
print('Sum:',s)
