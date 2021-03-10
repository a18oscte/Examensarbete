DROP DATABASE examensarbete;
CREATE DATABASE examensarbete;
USE examensarbete;

CREATE TABLE flightdata (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
airline CHAR(3) NOT NULL,
airlineId INT(6) NOT NULL,
sourceAirport CHAR(4) NOT NULL,
sourceAirportId INT(6) NOT NULL,
destinationAirport CHAR(4) NOT NULL,
destinationAirportId INT(6) NOT NULL,
stops INT(6) NOT NULL,
equipment VARCHAR(32) NOT NULL
) ENGINE=InnoDB;