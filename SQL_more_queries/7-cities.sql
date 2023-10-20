-- Write a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
USE `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `cities` ('id' NOT NULL INT UNIQUE AUTO_INCREMENT PRIMARY KEY, 'state_id' NOT NULL FOREIGN KEY REFERENCES states(id), 'name' VARCHAR(256) NOT NULL);
