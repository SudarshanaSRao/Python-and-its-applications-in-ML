import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
ctx=ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url=input('Enter the URL - ')
c=input('Enter the count:')
p=input('Enter the position:')
count=int(c)
position=int(p)-1
html=urlopen(url,context=ctx).read()
soup=BeautifulSoup(html,"html.parser")
href=soup('a')
for tags in href:
    print('Retrieving:',tags.get('href',None))
for i in range(count):
    link=href[position].get('href',None)
    print(href[position].contents[0])
    html=urlopen(link).read()
    soup=BeautifulSoup(html,"html.parser")
    href=soup('a')
