#!/usr/bin/env python3
import cgitb
import cgi
import json
cgitb.enable()

print("Content-Type: text/plain;charset=utf-8\n")
print("Hello World!")

arguments = cgi.FieldStorage()
print(arguments)
jsonObj = {}
if 'json' not in arguments.keys():
    returnErrorMessage("No JSON found.")
else:
    jsonObj = json.loads(arguments['json'].value.encode('utf-8'))

print(jsonObj)