-- for auth method 2
CREATE DATABASE auth;

CREATE TABLE  auth_method2(
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255)
);

-- for todo
CREATE TABLE  todo(
    todo_id SERIAL PRIMARY KEY,
    description VARCHAR(255)
);