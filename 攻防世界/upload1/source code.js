<script type="text/javascript">
 

Array.prototype.contains = function (obj) {  
    var i = this.length;  
    while (i--) {  
        if (this[i] === obj) {  
            return true;  
        }  
    }  
    return false;  
}  

function check(){
upfile = document.getElementById("upfile");
submit = document.getElementById("submit");
name = upfile.value;
ext = name.replace(/^.+\./,'');

if(['jpg','png'].contains(ext)){
	submit.disabled = false;
}else{
	submit.disabled = true;

	alert('请选择一张图片文件上传!');
}


}

</script>
