# Overview

This is a toy Todo application that uses some of the same frameworks as our production code.  It might be a good place to explain basic concepts, isolate and reproduce bugs, or use in interviews.  What frameworks do we love?

  * Backend:
    * [FastAPI](https://fastapi.tiangolo.com/)
    * [Pydantic](https://pydantic-docs.helpmanual.io/)
    * [SQLAlchemy](https://www.sqlalchemy.org/)
    * [SQLModel](https://sqlmodel.tiangolo.com/)
 
  * Database:
    * [CockroachDB](https://www.cockroachlabs.com/) (production)
    * [Postgresql](https://www.postgresql.org/) (development)

# Run

Clone this repository and `docker-compose up`.  It may take a few minutes for the databases to come online.  The backend fastapi app will start once it can connect to the database.  To access Jupyter, watch the logs (`docker-compose logs jupyter`) for the Jupyter url with access token, which will look something like `http://127.0.0.1:8888/?token=a458728e0c549062d578ea9cbaa5ef2d312702c9296363c5`

When the app is up, you can explore its endpoints via OpenAPI/Swagger at `http://localhost:8000/docs`

# Py-Spy

[Py-Spy](https://github.com/benfred/py-spy) is a sampling profiler for Python programs.  It can record your running Python process and generate [flamegraphs](https://www.brendangregg.com/flamegraphs.html) or [speedscope graphs](https://github.com/jlfwong/speedscope).  

For this demo application, the `uvicorn` process will always be pid 1 so we can hardcode it.  `./pyspy_profiles` is being mounted in to `/usr/src/profiles` on this branch so that when you py-spy record inside the container, the saved graph will be available on your host machine.

```
docker-compose exec backend py-spy record -o /usr/src/profiles/profile.svg --pid 1
```
