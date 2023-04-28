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

Build and run the both postgres and the FastAPI webapp:
```
docker compose up --build
```

Open the root endpoint at http://localhost:8000/

Open the api documentation at http://localhost:8000/redoc

### Running only one component
To run only the database:
```
docker compose up --build db
```

To run only the FastAPI web app:
```
docker compose up --build server
```

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

## Debugging the FastAPI app
### Option 1 - Run the web app on the host, with the db in the docker container.

* Install python on the host.
* Create and activate a virtual environment with the tool of your choice (venv, pyenv, virtualenv...).
* Install the dependencies: `pip install -r requirements.txt`
* Set the following environment variables:
  - `POSTGRES_SERVER=localhost`
  - `POSTGRES_PORT=9432`
* Run the webapp app in debug mode using your IDE/tool of choice, specifying `app/main.py` as the Python script to debug.
* Open the root endpoint at http://localhost:8001/

Note: the webapp run this way is run on port 8001, and can be run at the same time as the webapp
inside the docker container, which runs on port 8000.
However, if you don't want two webapps running, you can make sure that in
docker, only the db is started, with  `docker compose up --build db`.

### Option 2 - Attach to the debugger inside the container, with vscode (with debugpy)
* Rerun everything with `DEBUG` set to `debugpy` in the environment:
    ```shell
    env DEBUG=debugpy docker compose up --build
    ```
* Inside vscode, launch the `Python: Remote Attach` configuration.
* Also, in vscode, you can use "Remote explorer" to browse the files inside the container.
  That will open a new window. You can also launch the debugger from the new window.

### Option 3 - Web-pdb
* Add the following to the line of code you want to debug:
    ```python
    import web_pdb; web_pdb.set_trace()
    ```
* Rerun everything with `DEBUG` set to `pdb` in the environment:
    ```shell
    env DEBUG=pdb docker compose up --build
    ```
* Open http://localhost:5555/ to see the web-pdb interface.


## References
* [SQL (Relational) Databases in FastAPI](https://fastapi.tiangolo.com/tutorial/sql-databases/).
* [FastAPI, Docker, and Postgres](https://medium.com/@krishnardt365/fastapi-docker-and-postgres-91943e71be92), by Krish Na.
* [Docker compose healthcheck](https://github.com/peter-evans/docker-compose-healthcheck) to wait for postgres to be ready, before starting FastAPI.