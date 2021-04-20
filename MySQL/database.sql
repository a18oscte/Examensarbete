DROP DATABASE examensarbete;
CREATE DATABASE examensarbete;
USE examensarbete;

CREATE TABLE flightdata (
	id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	airline CHAR(3),
	airlineId INT(6),
	sourceAirport CHAR(4),
	sourceAirportId INT(6),
	destinationAirport CHAR(4),
	destinationAirportId INT(6),
	stops INT(6),
	equipment VARCHAR(32)
) ENGINE=InnoDB;