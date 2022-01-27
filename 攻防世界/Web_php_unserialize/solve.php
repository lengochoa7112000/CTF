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
