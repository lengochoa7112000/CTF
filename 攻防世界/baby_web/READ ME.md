# baby_web

题目描述：想想初始页面是哪个

开始我们得到一个URL: http://111.200.241.244:63012/1.php

因为题目描述是初始页面, 这让我想到 index.php. 试着换 1.php 成 index.php, 页面依旧显示 http://111.200.241.244:63012/1.php.
我想应该这其中有某个跳转, 使 index.php 跳转回 1.php. 使用 burp suite, 观看 HTTP history, 果然有 index.php, flag 就在这里.
