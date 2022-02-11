import hashlib

filename = '/fllllllllllllag'
cookie_secret = '22894d2e-48f5-4dc1-8818-1d41327a50e2'

filename_md5 = hashlib.md5(filename.encode()).hexdigest()
filehash = hashlib.md5((cookie_secret + filename_md5).encode()).hexdigest()

print(filehash)
