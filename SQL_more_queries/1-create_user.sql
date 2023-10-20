-- Write a script that creates the MySQL server user user_0d_1.
IF NOT EXIST CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES TO 'user_od_1'@'localhost';
