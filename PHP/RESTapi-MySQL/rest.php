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
    $query = "SELECT * FROM flightdata WHERE id LIKE :id OR airline LIKE :airline OR airlineId LIKE :airlineId OR sourceAirport LIKE :sourceAirport OR sourceAirportId LIKE :sourceAirportId OR destinationAirport LIKE :destinationAirport OR destinationAirportId LIKE :destinationAirportId OR stops LIKE :stops OR equipment LIKE :equipment";
    $stmt = $conn->prepare($query);
    $stmt->bindParam(":id", $get_arr['id']);
    $stmt->bindParam(":airline", $get_arr['airline']);
    $stmt->bindParam(":airlineId", $get_arr['airlineId']);
    $stmt->bindParam(":sourceAirport", $get_arr['sourceAirport']);
    $stmt->bindParam(":sourceAirportId", $get_arr['sourceAirportId']);
    $stmt->bindParam(":destinationAirport", $get_arr['destinationAirport']);
    $stmt->bindParam(":destinationAirportId", $get_arr['destinationAirportId']);
    $stmt->bindParam(":stops", $get_arr['stops']);
    $stmt->bindParam(":equipment", $get_arr['equipment']);
    //$stmt = query($stmt);
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
    echo json_encode($flightdata, JSON_PRETTY_PRINT);
    /*
    //Only works if there is data
    if(!empty($data)){

    }else{
        $query = "SELECT * FROM flightdata";
        $stmt = $conn->query($query);
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
        http_response_code(200);
        echo json_encode($flightdata, JSON_PRETTY_PRINT);
    }
    */
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
}
?>