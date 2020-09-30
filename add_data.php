<?php
require "conn.php";
$temperature = $_GET['temperature'];
$date = $_GET[date];
$wind_direction = $_GET[wind_direction];
$wind_speed = $_GET[wind_speed];

$res=mysqli_query($conn,$sql);

$mysql_qry = "INSERT INTO entries (temperature, date, wind_direction, wind_speed) VALUES ('$temperature','$date','$wind_direction','$wind_speed')";
echo "Data entry succesful";

if($conn->query($mysql_qry) === TRUE) {
}
$conn->close();
?>