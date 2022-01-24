# JaWT Scratchpad

Start the challenge, we can login with any username, other than admin. When I try to log in as `admin`, I got:

YOU CANNOT LOGIN AS THE ADMIN! HE IS SPECIAL AND YOU ARE NOT.

To slove this challenge, may be I colde be the admin. Login as `test`, I got a scratchpad to write any things.

Reload this page and notice the request in the Burp suite, you will see a specail cookie:

`jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidGVzdCJ9.IAu_YSHppFe8hXH_BSPb4OLJYGUi8wXqXdS0T33cKbA`

This cookie means that this challenge verifies its user by JWT web token. Therefore, to become the admin, I need to find the secret key of this JWT token.

With [jwt.io](https://jwt.io/) I find the `VERIFY SIGNATURE` of this token in mode `HMACSHA256`. Using `John`, I found the secret key is `ilovepico`

```
$ cat jwt_picoCTF.txt
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoidGVzdCJ9.IAu_YSHppFe8hXH_BSPb4OLJYGUi8wXqXdS0T33cKbA

$ john jwt_picoCTF.txt --wordlist=/usr/share/wordlists/rockyou.txt --format=HMAC-SHA256
Using default input encoding: UTF-8
Loaded 1 password hash (HMAC-SHA256 [password is key, SHA256 256/256 AVX2 8x])
Press 'q' or Ctrl-C to abort, almost any other key for status
ilovepico        (?)     
1g 0:00:00:03 DONE (2022-01-23 19:03) 0.2724g/s 2015Kp/s 2015Kc/s 2015KC/s ilovepinky53..ilovepatri
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

Add the secret key to `VERIFY SIGNATURE` in [jwt.io](https://jwt.io/) and change `"user": "test"` to `"user": "admin"`, we got the new JWT token:

`eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4ifQ.jQ4HVprBiAgctoCSd2vl5kntoB35ftKQf8aTchKr2rY`

Repalce the current JWT token by the new, we will get the flag!
