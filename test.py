# -*- encoding: utf-8 -*-
import urllib2
import json
url="http://www.google.com.mx/speech-api/v2/recognize?output=json&lang=es&key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw"
#Post a la url el archivo
r= urllib2.Request(url, open('output.flac').read())
r.add_header("Content-Type","audio/x-flac; rate=16000") #agrego content type
response = urllib2.urlopen(r).read().strip('{"result":[]}') #elimino primer json que es nulo
jon= json.loads(response) #cargo json 
print jon['result'][0]['alternative'][0]['transcript']