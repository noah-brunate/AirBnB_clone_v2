--script that prepares a MySQL server for user hbnb_test
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- creating new user named : hbnb_test with all privileges on the db hbnb_test_db
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- granting the SELECT privilege for the user hbnb_test on the db performance_schema
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- granting all privileges to the new user on hbnb_test_db
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
