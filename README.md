# fast-api-postgres 
https://pankajconnect.medium.com/all-about-pg-hba-conf-authentication-methods-postgresql-95137d896105
https://www.youtube.com/watch?v=2X8B_X2c27Q

1. Create Postgres docker container - This will host the database
CLI: Run `docker -v` to verify
CLI: Run `docker pull postgres:alpine`
CLI: Run `docker images` to check images

2. Create Docker Container
`docker run --name <container-name> -e POSTGRES_PASSWORD=<password> -d -p 5432:5432 <postgres-dist>`
Example
`docker run --name fastapi-postgres -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres:alpine`

3. Check Containers
`docker ps`

4. Create Database
`docker exec -it <container-name> bash`
`docker exec -it fastapi-postgres bash`  # This will go into the terminal of your container

# Create User
`psql -U <db_user>`
`psql -U postgres`

# Create Database
`create database <db_name>`
`create database fastapi_database`

# Create username and password
`create user <username> with encrypted password '`<password>`'`
`create user myuser with encrypted password 'password'`;

# Grant privileges
`grant all privileges on database <db_name> to <username>`
`grant all privileges on database fastapi_database to myuser;`

# Connect to database
`\c <db_name>`
`\c fastapi_database`

# Make connection available to outside of container
`psql -h <hostname> -p <port> <db_user>`
`psql -h localhost -p 5432 postgres` # Makes available outside of container


# **STEPS TO REGENERATE** 
1. Create Docker Container
```bash
docker run --name fastapi-postgres -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres:alpine
```
2. Enter docker terminal  
```bash 
docker exec -it fastapi-postgres bash
``` 
3. Create user 
```bash
psql -U myuser
``` 
4. Create Database
```bash 
create database fastapi_database
```
5. Run `database.py` with connection string `postgresql://myuser:password@localhost:5621/fastapi_database` 