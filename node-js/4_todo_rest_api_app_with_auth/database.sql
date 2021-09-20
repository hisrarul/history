-- for auth method 1
CREATE DATABASE auth;

CREATE TABLE  auth_method1(
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255)
);

-- for auth method 2
CREATE TABLE  auth_method2(
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255)
);

-- for auth method 3
CREATE TABLE  auth_method3(
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255),
    salt VARCHAR(255)
);

-- for auth method 4
CREATE TABLE  auth_method4(
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255)
);

-- for auth method 5
CREATE TABLE  auth_method5(
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    userdata VARCHAR(255)
);

-- for todo
CREATE TABLE  todo(
    todo_id SERIAL PRIMARY KEY,
    description VARCHAR(255)
);