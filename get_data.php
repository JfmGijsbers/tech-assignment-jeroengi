<?php
require "conn.php";

$sql = "select * from entries";
$res=mysqli_query($conn,$sql);
$rows = array();
while($r = mysqli_fetch_assoc($res)) {
	$rows[] = $r;
}
echo json_encode($rows);


if($conn->query($mysql_qry) === TRUE) {
}
$conn->close();
?>