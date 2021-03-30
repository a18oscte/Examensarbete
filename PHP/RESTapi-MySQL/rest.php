<?php
include_once 'database.php';

//Create database connection
$database = new Database();
$conn = $database->getConnection();

//get the in-data
$data = json_decode(file_get_contents("php://input"));

//check what type of request
switch($_SERVER['REQUEST_METHOD'])
{
//If there is a get request
case 'GET': $the_request = &$_GET;
    //If there is no inparameters
    if(empty($_GET)){
        //Get all flightdatafrom the darabase
        $query = "SELECT * FROM flightdata";
        $stmt = $conn->query($query);
       
        //adding flightdata to a array
        $flightdata = array();
        while ($row = $stmt->fetch()) {
            $tmp = array("id" => $row['id']);
            $tmp += ["airline" => $row['airline']];
            $tmp += ["airlineId" => $row['airlineId']];
            $tmp += ["sourceAirport" => $row['sourceAirport']];
            $tmp += ["sourceAirportId" => $row['sourceAirportId']];
            $tmp += ["destinationAirport" => $row['destinationAirport']];
            $tmp += ["destinationAirportId" => $row['destinationAirportId']];
            $tmp += ["stops" => $row['stops']];
            $tmp += ["equipment" => $row['equipment']];
            array_push($flightdata, $tmp);
        }
       
        //responed with the array with all flightdata
        http_response_code(200);
        echo json_encode($flightdata, JSON_PRETTY_PRINT);
    
    //If there is inparameters
    }else{
        //Get the inparameters into an array
        $get_arr = array(
            "id" =>  isset($_GET['id']) ? $_GET['id'] : null,
            "airline" => isset($_GET['airline']) ? $_GET['airline'] : null,
            "airlineId" => isset($_GET['airlineId']) ? $_GET['airlineId'] : null,
            "sourceAirport" => isset($_GET['sourceAirport']) ? $_GET['sourceAirport'] : null,
            "sourceAirportId" => isset($_GET['sourceAirportId']) ? $_GET['sourceAirportId'] : null,
            "destinationAirport" => isset($_GET['destinationAirport']) ? $_GET['destinationAirport'] : null,
            "destinationAirportId" => isset($_GET['destinationAirportId']) ? $_GET['destinationAirportId'] : null,
            "stops" => isset($_GET['stops']) ? $_GET['stops'] : null,
            "equipment" => isset($_GET['equipment']) ? $_GET['equipment'] : null
    
        );
        
        //get the matching fligtdata from the database
        $query = "SELECT * FROM flightdata WHERE id LIKE :id OR airline LIKE :airline OR airlineId LIKE :airlineId OR sourceAirport LIKE :sourceAirport OR sourceAirportId LIKE :sourceAirportId OR destinationAirport LIKE :destinationAirport OR destinationAirportId LIKE :destinationAirportId OR stops LIKE :stops OR equipment LIKE :equipment";
        $stmt = $conn->prepare($query);
        $stmt->execute(["id" => $get_arr['id'], "airline" => $get_arr['airline'], "airlineId" => $get_arr['airlineId'], "sourceAirport" => $get_arr['sourceAirport'], "sourceAirportId" => $get_arr['sourceAirportId'], "destinationAirport" => $get_arr['destinationAirport'], "destinationAirportId" => $get_arr['destinationAirportId'], "stops" => $get_arr['stops'], "equipment"=> $get_arr['equipment']]); 
        
        //adding flightdata to a array
        $flightdata = array();
        while ($row = $stmt->fetch()) {
            $tmp = array("id" => $row['id']);
            $tmp += ["airline" => $row['airline']];
            $tmp += ["airlineId" => $row['airlineId']];
            $tmp += ["sourceAirport" => $row['sourceAirport']];
            $tmp += ["sourceAirportId" => $row['sourceAirportId']];
            $tmp += ["destinationAirport" => $row['destinationAirport']];
            $tmp += ["destinationAirportId" => $row['destinationAirportId']];
            $tmp += ["stops" => $row['stops']];
            $tmp += ["equipment" => $row['equipment']];
            array_push($flightdata, $tmp);
        }

        //If there is matching flightdata in the database
        if(!empty($flightdata)){
            http_response_code(200);
            //responed with the array with the flightdata
            echo json_encode($flightdata, JSON_PRETTY_PRINT);
        //If there is no matching flightdata in the database
        }else{
            http_response_code(404);
            echo json_encode(array("message" => "No flightdata matched the get request"), JSON_PRETTY_PRINT);
        }
    }
    break;

//If there is a post request
case 'POST': $the_request = &$_POST;
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
    break;

 // Etc.
default:
    http_response_code(503);
}
?>