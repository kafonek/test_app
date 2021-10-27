# Overview

This is a toy application that uses some of the same frameworks as our production code.  It might be a good place to explain basic concepts, isolate and reproduce bugs, or use in interviews.  What frameworks do we love?

  * Backend:
    * [FastAPI](https://fastapi.tiangolo.com/)
    * [Pydantic](https://pydantic-docs.helpmanual.io/)
    * [SQLAlchemy](https://www.sqlalchemy.org/)
    * [SQLModel](https://sqlmodel.tiangolo.com/)
 
  * Database:
    * [CockroachDB](https://www.cockroachlabs.com/) (production)
    * [Postgresql](https://www.postgresql.org/) (development)


# Py-Spy

[Py-Spy](https://github.com/benfred/py-spy) is a sampling profiler for Python programs.  I couldn't get it working unfortunately.

1. Install `py-spy` in backend container and add `sys_ptrace` to the container Docker capabilities
2. Get the pid for the running fastapi app with `docker-compose top backend`
3. Run Py-Spy `docker-compose exec backend py-spy top --pid <pid>`

The error I get is when trying any pid is:
```
Error: Failed to get process executable name. Check that the process is running.
Reason: No such file or directory (os error 2)
``