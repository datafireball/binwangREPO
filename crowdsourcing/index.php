<?php
// set up cookie for the user, so later down the road. 
// we can remove the records based on irresponsible user cookie
$cookie_name = "userCookie";
if(!isset($_COOKIE[$cookie_name])) {
  $value = rand(1, 999999);
  setcookie("userCookie",$value, time()+3600*24*7);
} 

$mysql_servername = "localhost";
$mysql_username = "bwang";
$mysql_password = "mypassbwang";
$conn = new mysqli($mysql_servername, $mysql_username, $mysql_password);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 
?>

<html>
<head>
</head>
<body>
<h1>Crowd Sourcing Application</h1>
<h4>Please try to answer the question responsibly and click submit in the end</h4>

<?php
// randomly select a question to give to the user
// maybe down the road, we don't want to give the user that it has seen before
$sql = "SELECT myquestion, myquestion1 FROM mydatabase.a59347_question order by rand() limit 1";
$result = $conn->query($sql);
$row = $result->fetch_assoc();
$myvalue = strtolower($row["myquestion"]) ;
echo "MYQUESTION : " . strtolower($row["myquestion"]) . "<br>";
echo "MYQUESTION1: " . strtolower($row["myquestion1"]) . "<br>";
echo "<br>";
?>

<form action="#" method="post">
<select name="answer">
<?php
$sql = "SELECT question1, answer FROM mydatabase.a59347_answer WHERE question1 = '" . $row["myquestion1"] . "'";
$result1 = $conn->query($sql);
echo "<option>" . "No Match" . "</option>";

if ($result1->num_rows > 0) {

    // output data of each row
    while($row1 = $result1->fetch_assoc()) {
    	echo "<option value='" . strtolower($row1["answer"]) . "'>" . strtolower($row1["answer"]) ."</option>";
    }
} 
?>
</select>
<input type="hidden" name="question" value=<?php echo $row["myquestion"] ?>>
<input type="submit" name="submit" value="Submit" />
</form>

<?php 

   $option = isset($_POST['answer']) ? $_POST['answer'] : false;
   if($option) {
     echo "Your match for " . $_POST['question'] . " was: ";
     echo htmlentities($_POST['answer'], ENT_QUOTES, "UTF-8");
     echo "<br>";
   } else {
     echo "No Answer";
     exit; 
   }

   $sql = "INSERT INTO mydatabase.a59347_useranswer (question, answer, usercookie, ip, useragent) VALUES ('" . 
   	$_POST['question'] . "|" . $row["myquestion1"] . 
   	"', '" . 
   	$_POST['answer'] . 
   	"', '" . 
   	$_COOKIE['userCookie'] .
   	"', '" . 
   	$_SERVER['REMOTE_ADDR'] . 
   	"', '" . 
   	$_SERVER['HTTP_USER_AGENT'] . 
   	"')";

   echo "<br>";
   //echo $sql;
   echo "<br>";


   if ($conn->query($sql) === TRUE) {
       echo "New record created successfully";
   } else {
       echo "Error: " . $sql . "<br>" . $conn->error;
   }

?>

</body>
</html>
