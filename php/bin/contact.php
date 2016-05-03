<?php
// check if fields passed are empty
if(empty($_POST['name'])  		||
   empty($_POST['email']) 		||
   empty($_POST['grade']) 		||
   empty($_POST['detail'])	||
   !filter_var($_POST['email'],FILTER_VALIDATE_EMAIL))
   {
	echo "No arguments Provided!";
	return false;
   }

$name = $_POST['name'];
$email_address = $_POST['email'];
$grade = $_POST['grade'];
$message = $_POST['detail'];
$reciever = $_POST['reciever'];

// create email body and send it
$to = sikim@students.logoscambodia.org; // PUT YOUR EMAIL ADDRESS HERE
$email_subject = "Serice Portal Sign Up:  $name"; // EDIT THE EMAIL SUBJECT LINE HERE
$email_body = "You have received a new message from the Service Portal.\n\n"."Here is a potential volunteer:\n\nName: $name\n\nPhone: $phone\n\nEmail: $email_address\n\nStatement:\n$message";
$headers = "From: Service Portal\n";
$headers .= "Reply-To: $email_address";
mail($to,$email_subject,$email_body,$headers);
return true;
?>
