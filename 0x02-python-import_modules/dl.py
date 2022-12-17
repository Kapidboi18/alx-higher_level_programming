#!/usr/bin/python3
# dl.py

import requests

url = 'https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc'
r = requests.get(url, allow_redirects=True)
open('hidden_4.pyc', 'wb').write(r.content)
