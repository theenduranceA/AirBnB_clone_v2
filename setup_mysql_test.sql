-- A test script for a MySQL server project with database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Creates a new user new user hbnb_test (in localhost) & password set to hbnb_test_pwd
CREATE USER IF NOT EXISTS hbnb_test@localhost IDENTIFIED BY 'hbnb_test_pwd';
-- Granting all priviledges to user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO hbnb_test@localhost;
-- Granting only selected priviledges to user
GRANT SELECT ON performance_schema.* TO hbnb_test@localhost;
FLUSH PRIVILEGES;
