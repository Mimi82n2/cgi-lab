#!/usr/bin/env python3

import cgi
import os
from re import L
from templates import login_page
import secret
from templates import secret_page

def parse_cookies(cookie_string):
    cookies = cookie_string.split(";")
    result = {}
    for cookie in cookies:
        split_cookie = cookie.split("=")
        result[split_cookie[0]] = split_cookie[1]
    
    return result

cookies = parse_cookies(os.environ["HTTP_COOKIE"])

form = cgi.FieldStorage()

username = form.getfirst("username")
password = form.getfirst("password")

header = ""
header += "Content-Type: text/html\r\n"

body = ""
if (('logged' in cookies and cookies['logged'] == 'true') or
    username is not None and
    username == secret.username and
    password is not None and
    password == secret.password
    ):
    body += secret_page(username, password)
    header += "Set-Cookie: logged=true; Max-Age=30\r\n"
    header += "Set-Cookie: cookie=nom\r\n"
    body += "<h1>A terrible secret</h1>"
else:
    body += login_page()
    

print(header)
print()
print(body)