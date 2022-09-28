#!/usr/bin/env python3

import os
import json
import cgi
import os
from re import L
from templates import login_page
from templates import secret_page

env = {}

for env_key, env_value in os.environ.items():
    env[env_key] = env_value

form = cgi.FieldStorage()

username = form.getfirst("username")
password = form.getfirst("password")
header = ""
header += "Content-Type: text/html\r\n"
body = ""
#if username is not None or ('logged' in cookies and cookies['logged'] == 'true'):
if username is not None:
    body += secret_page(username, password)
    header += "Set-Cookie: logged=true; Max-Age=60\r\n"
    header += "Set-Cookie: cookie=nom\r\n"
    body += "<h1>A terrible secret</h1>"
else:
    body += login_page()

print("Content-Type: text/html\n")
print()
print("<!doctype html><title>Hello</title><h2>Hello World</h2>")
print("ENVIRONMENT VAR ", json.dumps(env, sort_keys=True))
print()
print("<h2>Query String: {}</h2>".format(os.environ["QUERY_STRING"]))
print()
print("<h2>Browser Info: {}</h2>".format(os.environ["HTTP_USER_AGENT"]))
print()
print(header)
print()
print(body)