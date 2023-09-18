-- A script that prepares a MySQL server for the project with database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Creates a new user new user hbnb_dev (in localhost) & password set to hbnb_dev_pwd
CREATE USER IF NOT EXISTS hbnb_dev@localhost IDENTIFIED BY 'hbnb_dev_pwd';
-- Granting all priviledges to user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO hbnb_dev@localhost;
-- Granting only selected priviledges to user
GRANT SELECT ON performance_schema.* TO hbnb_dev@localhost;
FLUSH PRIVILEGES;
