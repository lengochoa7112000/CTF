# warmup

查看源代码, 我们得到提示 source.php. 可以了解一下 source.php:

在 class emmm 中:

$whitelist 定义一个 array

首先, 检查 $page 值是否在 $whitelist 里, 是就返回 true

mb_strpos($page.'?', '?') 返回第一次 '?' 在 $page.'?' 里出现的位置

mb_substr($page, 0, x) 返回 string 从 0 到 x 在 $page 里

然后检查 $_page 值在 $whitelist 里

下面原理也一样

最下面的这一段就容易理解了. 我们需要注入 page 值是 string,使 class emmm 返回 true, 那时候就会 include file 值, 这里我想到读取, 因为我有尝试看 hint.php大它的内容是

flag not here, and flag in ffffllllaaaagggg

应该指 flag 在 ffffllllaaaagggg 文件里.


知道是 mb_substr 有问题, 但我尝试多次 ?file=source.php?../../../../ffffllllaaaagggg 也没能找到 flag (我知道 flag 在这是因为我已经做过这题, 现在重做竟然忘了 ...)

查看一下, 正确 payload 应该是 file=source.php?/../../../../ffffllllaaaagggg !!! 还是不明白为什么有一个 ? 在中间还可以 directory traversal?

还有, ffffllllaaaagggg 在提示有 4 个 ../

一个简单的 directory traversal 就把我耍的团团转!
