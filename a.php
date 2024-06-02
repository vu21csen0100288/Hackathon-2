<?php
// Step 1: Connect to your MySQL database
$servername = "sql12.freesqldatabase.com"; // Change this to your database server's hostname
$username = "sql12711205"; // Change this to your database username
$password = "aAp69rFrPl"; // Change this to your database password
$dbname = "sql12711205"; // Change this to your database name

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Step 2: Receive data sent from the HTML form
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate the data (not shown in this example)
    $start = $_POST["start"];
    $destination = $_POST["destination"];

    // Step 3: Execute SQL queries to interact with the database
    // For example, you can fetch information about available vehicles (route numbers) between the starting point and destination
    $sql = "SELECT route_no FROM bus_routes WHERE from_location = '$start' AND to_location = '$destination'";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // Step 4: Prepare data to be sent back to the client
        $response = array();
        while ($row = $result->fetch_assoc()) {
            $response[] = $row["route_no"];
        }
        echo json_encode($response);
    } else {
        echo json_encode(array()); // Return an empty array if no vehicles are available
    }
}

// Step 5: Close the database connection
$conn->close();
?>
