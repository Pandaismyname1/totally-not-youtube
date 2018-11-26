#!/usr/bin/env python3
from search import searchOnYoutube
from downloader import download, searchInCache

import cgi
import json


def returnErrorMessage(text):
    response = {}
    response['type'] = 'error'
    response['message'] = text
    print(json.dumps(response))
    exit(0)

def returnSuccesMessage(id):
    response = {}
    response['type'] = 'success'
    response['message'] = 'Your offer has been hidden from other users.'
    response['id'] = id
    print(json.dumps(response))
    exit(0)

def downloadVideo(query):
    videoId = searchOnYoutube(query)
    if(searchInCache(videoId)):
        print('Found Cached Version Of '+videoId)
    else:
        download(videoId)
        print('Downloaded '+videoId)
arguments = cgi.FieldStorage()
print(arguments)
print("test")
jsonObj = {}
print(arguments['json'])
exit(0)
if 'json' not in arguments.keys():
    returnErrorMessage("No JSON found.")
else:
    jsonObj = json.loads(arguments['json'].value.encode('utf-8'))

if(jsonObj['command']=='download'):
    downloadVideo(jsonObj['arguments'][0])
    
