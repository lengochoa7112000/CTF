# NaNNaNNaNNaN-Batman

本题提供给我们一个附件, 是一堆乱码. 我们可以把最后的 `eval()` 换成 `alert()`. 然后进行整理一下, 的到一段 `Java script` 的代码:

```js
<script>
function $(){
    var e=document.getElementById("c").value;
    if(e.length==16)
        if(e.match(/^be0f23/)!=null)
            if(e.match(/233ac/)!=null)
                if(e.match(/e98aa$/)!=null)
                    if(e.match(/c7be9/)!=null){
                        var t=["fl","s_a","i","e}"];
                        var n=["a","_h0l","n"];
                        var r=["g{","e","_0"];
                        var i=["it'","_","n"];
                        var s=[t,n,r,i];
                        for(var o=0;o<13;++o){
                            document.write(s[o%4][0]);
                            s[o%4].splice(0,1)
                        }
                    }
}

document.write('<input id="c"><button onclick=$()>Ok</button>');
delete _
</script>
```

这是一段简单的代码. 如果变数 `e` 符合以上几个要求, 就按照规则显示出 `flag` 的所有字母.

我写了一个简单的 `C++` 脚本:

```cpp
#include <iostream>
#include <string>
using namespace std;

int main()
{
	string a[4][4] = {"fl","s_a","i","e}","a","_h0l","n","","g{","e","_0","","it'","_","n",""};
	
	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++)
			cout << a[j][i];
	}
	return 0;
}
```
