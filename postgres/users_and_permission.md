### Create users in postgres database

``` CREATE USER "yourusername" WITH PASSWORD 'yourpassword';```

### Grant access to tables in schema other than public
```
GRANT USAGE ON SCHEMA otherthanpublicschema TO "yourusername";
GRANT SELECT ON ALL TABLES IN SCHEMA otherthanpublicschema TO "yourusername";
GRANT SELECT ON ALL TABLES IN SCHEMA public TO "yourusername";
```
