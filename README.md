
<!DOCTYPE html>
<html>
<head>
	<title>Idex</title>
	<script type="text/javascript" language="javascript">
		function signIn()
		{
			window.location = "http://127.0.0.1:8000/signin"
		}
		function signUp()
		{
			window.location = 'signUp'
		} 
	</script>
</head>
<body style="text-align: center;">
	<button id="signIn" onclick="signIn()" style="margin-top: 400px; height: 40px;width: 70px;">Sign In</button>
	<button id="signUp" onclick="signUp()" style="height: 40px;width: 70px;">Sign up</button>
</body>
</html>
