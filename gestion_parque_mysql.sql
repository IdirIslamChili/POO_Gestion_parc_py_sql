drop database if exists db_voitures;
create database if not exists db_voitures;
Use db_voitures;
CREATE USER IF NOT EXISTS 'user_python'@'localhost' IDENTIFIED BY 'Python2026';
GRANT ALL PRIVILEGES ON *.* TO 'user_python'@'localhost';
FLUSH PRIVILEGES;