CREATE DATABASE auth;

CREATE TABLE  auth_method1(
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255)
);