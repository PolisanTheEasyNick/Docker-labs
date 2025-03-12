CREATE DATABASE IF NOT EXISTS movies_db;
USE movies_db;

CREATE TABLE IF NOT EXISTS movie (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    year INT
);

INSERT INTO movie (title, year) VALUES
('The Matrix', 1999),
('Inception', 2010),
('The Dark Knight', 2008);
