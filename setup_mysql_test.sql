-- Create a MySQL server with:
--  Database `hbnb_test_db`
--  New user `hbnb_test` in localhost with password `hbnb_test_pwd`
--  ALL privileges for `hbnb_test` user on `hbnb_test_db` database
--  SELECT privileges for `hbnb_test` user on `performance_schema` database

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER
    IF NOT EXISTS 'hbnb_test'@'localhost'
    IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES
   ON hbnb_test_db.*
   TO 'hbnb_test'@'localhost';
GRANT SELECT
   ON performance_schema.*
   TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
