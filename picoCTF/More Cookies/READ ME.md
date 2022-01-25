# More Cookies

We can see the notification:

"Welcome to my cookie search page. Only the admin can use it!"

So I need to become the admin in this challenge. Notice that we have a special cookie:

`auth_name=RGhEallxaGRqWGpFUkw3bkp0S3lpdnBFUGJIZlNVY3pBTWFQTG02WFNKN0Z4NTAvNmNwMVJwNFpveUt1cVpoclJFQkMyVTZJYkdraVZCS2R4U1ZYS1QvZEhGdmt3RGVOZGYzNkxDSlZnTTJES2hvcVN2NUp6L2ExVXFDdGFhYlk=`

It is easily to seen that this cookie was encoded in Base64.

The hint of this challenge is `Homomorphic encryption` and we have `CBC` in the description. That's all things I know and I got stuck here.

From some write up, I know that I need to make a `Bit Flipping attack`. By any amazing way, they guess that this cookie contains a string like `admin=0` :D And we need to `xor` one bytes in `Initialization Vector`. It will make one bytes in cipher change too. Specifically, change `admin=0` to `admin=1`.

My script to brute force this byte in python:

```py
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

```

Read more about `Bit Flipping Attack` in this [link](https://crypto.stackexchange.com/questions/66085/bit-flipping-attack-on-cbc-mode/66086#66086)
