-- Create a MySQL server with:
--  Database `hbnb_dev_db`
--  New user `hbnb_dev` and password `hbnb_dev_pwd`
--  ALL privileges for `hbnb_dev` user on `hbnb_dev_db` database
--  SELECT privilege for `hbnb_dev` user on `performance_schema` databse

CREATE DATABASE
    IF NOT EXISTS hbnb_dev_db;

CREATE USER
    IF NOT EXISTS 'hbnb_dev'@'localhost'
    IDENTIFIED BY 'hbnb_dev_pwd';

GRANT ALL PRIVILEGES
   ON hbnb_dev_db.*
   TO 'hbnb_dev'@'localhost';

GRANT SELECT
   ON performance_schema.*
   TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
