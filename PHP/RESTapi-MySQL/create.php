<?php
include_once 'database.php';

//Create database connection
$database = new Database();
$conn = $database->getConnection();

//get the in-data
$data = json_decode(file_get_contents("php://input"));

//Only works if there is data
if(!empty($data)){
    //Preparing the sql statement with the in-data
    $query = "INSERT INTO flightdata SET airline=:airline, airlineId=:airlineId, sourceAirport=:sourceAirport, sourceAirportId=:sourceAirportId, destinationAirport=:destinationAirport, destinationAirportId=:destinationAirportId, stops=:stops, equipment=:equipment";
    $stmt = $conn->prepare($query);
    $stmt->bindParam(":airline", $data->airline);
    $stmt->bindParam(":airlineId", $data->airlineId);
    $stmt->bindParam(":sourceAirport", $data->sourceAirport);
    $stmt->bindParam(":sourceAirportId", $data->sourceAirportId);
    $stmt->bindParam(":destinationAirport", $data->destinationAirport);
    $stmt->bindParam(":destinationAirportId", $data->destinationAirportId);
    $stmt->bindParam(":stops", $data->stops);
    $stmt->bindParam(":equipment", $data->equipment);

    //Executes the sql statement and checks for errors
    if($stmt->execute()){
        http_response_code(200);
        echo json_encode(array("message" => "flightdata was created."));
    }else{
        http_response_code(503);
        echo json_encode(array("message" => "Unable to create flightdata."));
    }
}else{
    //Respones if there is no in-data
    http_response_code(204);
    echo json_encode(array("message" => "Unable to create flightdata. Data is incomplete."));
}
?>