# PHP2

难度系数: 1.0

一开始, 只有下面的要求:

`Can you anthenticate to this website?`

authenticate 被写成 anthenticate 让我还以为是作者的什么用意 ?!

尝试了几个常用的: robots.txt, index.php, login.php... 都没有收获.

就在感到绝望的时候,突然想到 phps, 果然, index.phps 有 source code.

```php
<?php
if("admin"===$_GET[id]) {
  echo("<p>not allowed!</p>");
  exit();
}

$_GET[id] = urldecode($_GET[id]);
if($_GET[id] == "admin")
{
  echo "<p>Access granted!</p>";
  echo "<p>Key: xxxxxxx </p>";
}
?>
```

其实 phps 是 php 的原代码, 应该是经验让我想到这个把. 我想如果用 dirsearch 应该也会得到这个页面.

这段代码挺简单的. 如果 id 的值等于 admin 返回 not allowed! 如果 id 的 urldecode 等于 admin 返回 flag.

这里我们只需要注意 id 将 urlencode 2 次, 因为在 url 中已经有一次自动的 urldecode.

payload: `?id=%25%36%31%25%36%34%25%36%64%25%36%39%25%36%65`
