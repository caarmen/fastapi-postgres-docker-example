# Example FastAPI app with Postgres, docker-compose

Minimal example of a setup with docker-compose which
starts a postgres database and a FastAPI webapp.

The FastAPI webapp has one endpoint, which:
* Inserts a row into a db table "greetings", which is
  a string representation of the current timestamp.
* Returns the list of all the rows of the table.


☝️ The purpose of this repo is to note minimum wiring
to have postgres and FastAPI configured in docker-compose.
It may not use best practices. (For example, the db password
is committed to git in the .env file.)

## Running

Build and run the server:
```
docker compose up --build
```

Open the root endpoint at http://localhost:8000/

Open the api documentation at http://localhost:8000/redoc

## Inspecting the database

Connect to the database by opening an interactive session to
the docker container for the db:

```
docker exec -it fastapi-postgres-docker-example-db-1 /usr/bin/psql --username=postgres --dbname=app
```

Example session to list all the greetings:
```
% docker exec -it fastapi-postgres-docker-example-db-1 /usr/bin/psql --username=postgres --dbname=app

psql (15.2 (Debian 15.2-1.pgdg110+1))
Type "help" for help.

app=# select * from greetings;
 id |            text            
----+----------------------------
  1 | 2023-04-28 15:18:02.150314
  2 | 2023-04-28 15:31:12.426155
(2 rows)
```

## References
* [SQL (Relational) Databases in FastAPI](https://fastapi.tiangolo.com/tutorial/sql-databases/).
* [FastAPI, Docker, and Postgres](https://medium.com/@krishnardt365/fastapi-docker-and-postgres-91943e71be92), by Krish Na.
* [Docker compose healthcheck](https://github.com/peter-evans/docker-compose-healthcheck) to wait for postgres to be ready, before starting FastAPI.