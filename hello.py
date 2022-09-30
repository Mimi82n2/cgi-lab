#!/usr/bin/env python3

import os
import json
import cgi
import os
from re import L
from templates import login_page
from templates import secret_page
import secret


def parse_cookies(cookie_string):
    result = {}
    if cookie_string == "":
        return result
        
    cookies = cookie_string.split(";")
    for cookie in cookies:
        split_cookie = cookie.split("=")
        result[split_cookie[0]] = split_cookie[1]

    return result

env = {}

for env_key, env_value in os.environ.items():
    env[env_key] = env_value

form = cgi.FieldStorage()

username = form.getfirst("username")
password = form.getfirst("password")
header = ""
body = ""
cookies = parse_cookies(os.environ["HTTP_COOKIE"])
if ('logged' in cookies and cookies['logged'] == 'true'):
    body += secret_page(username, password)
    body += "<h1>A terrible secret</h1>"
    print("Content-Type: text/html\r\n")
    print()
    print(header)
    print()
    print(body)
    print()
else:
    if (username is not None and
        username == secret.username and
        password is not None and
        password == secret.password
        ):
        body += secret_page(username, password)
        header += "Set-Cookie: logged=true; Max-Age=30\r\n"
        header += "Set-Cookie: cookie=nom\r\n"
        body += "<h1>A terrible secret</h1>"
        print("Content-Type: text/html\r\n")
        print()
        print(header)
        print()
        print(body)
    else:
        print("Content-Type: text/html\r\n")
        print()
        print(login_page())
        print()
        print("ENVIRONMENT VAR ", json.dumps(env, sort_keys=True))
        print()
        print("<h2>Query String: {}</h2>".format(os.environ["QUERY_STRING"]))
        print()
        print("<h2>Browser Info: {}</h2>".format(os.environ["HTTP_USER_AGENT"]))

