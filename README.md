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


## References
* [SQL (Relational) Databases in FastAPI](https://fastapi.tiangolo.com/tutorial/sql-databases/).
* [FastAPI, Docker, and Postgres](https://medium.com/@krishnardt365/fastapi-docker-and-postgres-91943e71be92), by Krish Na.
* [Docker compose healthcheck](https://github.com/peter-evans/docker-compose-healthcheck) to wait for postgres to be ready, before starting FastAPI.