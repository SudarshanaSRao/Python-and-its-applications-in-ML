import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode=ssl.CERT_NONE
url=input('Enter the URL -')
html=urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,"html.parser")
s=0
count=0
tags=soup('span')
for tag in tags:
    count+=1
    s+=int(tag.contents[0])
print('Count',count)
print('Sum',s)
