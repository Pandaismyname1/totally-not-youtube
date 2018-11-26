#!/usr/bin/env python3
import cgitb
import cgi
cgitb.enable()

print("Content-Type: text/plain;charset=utf-8\n")
print("Hello World!")

arguments = cgi.FieldStorage()
print(arguments)