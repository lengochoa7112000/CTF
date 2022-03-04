<?php
$miwen="a1zLbgQsCESEIqRLwuQAyMwLyq2L5VwBxqGA3RQAyumZ0tmMvSGM2ZwB4tws";

function encode($str){
    $_o=strrev($str);
    // echo $_o;
        
    for($_0=0;$_0<strlen($_o);$_0++){
       
        $_c=substr($_o,$_0,1);
        $__=ord($_c)+1;
        $_c=chr($__);
        $_=$_.$_c;   
    } 
    return str_rot13(strrev(base64_encode($_)));
}

function decode($str){
	$str = base64_decode(strrev(str_rot13($str)));
    for ($_0 = 0; $_0 < strlen($str); $_0++){
    	$_c = substr($str, $_0, 1);
        $_temp = ord($_c) - 1;
        $ans = $ans.chr($_temp);
    }
    $ans = strrev($ans);
    return $ans;
}

echo decode($miwen);
?>
