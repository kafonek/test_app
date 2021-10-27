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
3. Run Py-Spy in the backend container

```
kafonek@DESKTOP-0MLN0FF:~/test_app$ dc ps
        Name                      Command               State                                 Ports                              
---------------------------------------------------------------------------------------------------------------------------------
test_app_backend_1     python -m debugpy --listen ...   Up      0.0.0.0:5678->5678/tcp,:::5678->5678/tcp,                        
                                                                0.0.0.0:8000->8000/tcp,:::8000->8000/tcp                         
test_app_cockroach_1   /cockroach/cockroach.sh st ...   Up      26257/tcp, 8080/tcp                                              
test_app_jupyter_1     tini -g -- start-notebook.sh     Up      0.0.0.0:8888->8888/tcp,:::8888->8888/tcp                         
test_app_postgres_1    docker-entrypoint.sh postgres    Up      5432/tcp        

kafonek@DESKTOP-0MLN0FF:~/test_app$ dc top backend
test_app_backend_1
UID     PID    PPID    C   STIME   TTY     TIME                                          CMD                                     
---------------------------------------------------------------------------------------------------------------------------------
root   20577   20557   1   14:14   ?     00:00:10   python -m debugpy --listen 0.0.0.0:5678 -m uvicorn app.main:app --reload     
                                                    --host 0.0.0.0                                                               
root   20643   20577   0   14:14   ?     00:00:00   /opt/venv/bin/python /opt/venv/lib/python3.9/site-packages/debugpy/adapter   
                                                    --for-server 46249 --host 0.0.0.0 --port 5678 --server-access-token          
                                                    443f67fee0797ef379661733f67f41ce1aa7e738b6ef7c4d75a00453bfa944c0             
root   20656   20577   0   14:14   ?     00:00:02   /opt/venv/bin/python -B -c import sys; sys.path.insert(0,                    
                                                    r'/opt/venv/lib/python3.9/site-packages/debugpy/_vendored/pydevd'); import   
                                                    pydevd; pydevd.PydevdCustomization.DEFAULT_PROTOCOL='http_json';             
                                                    pydevd.settrace(host='127.0.0.1', port=40715, suspend=False,                 
                                                    trace_only_current_thread=False, patch_multiprocessing=True, access_token='44
                                                    3f67fee0797ef379661733f67f41ce1aa7e738b6ef7c4d75a00453bfa944c0',             
                                                    client_access_token=None, __setup_holder__={'access-token':                  
                                                    '443f67fee0797ef379661733f67f41ce1aa7e738b6ef7c4d75a00453bfa944c0', 'client':
                                                    '127.0.0.1', 'json-dap-http': True, 'multiprocess': True, 'port': 40715,     
                                                    'ppid': 1, 'server': False, 'skip-notify-stdin': True}); from                
                                                    multiprocessing.resource_tracker import main;main(5)                         
root   20657   20577   1   14:14   ?     00:00:14   /opt/venv/bin/python -B -c import sys; sys.path.insert(0,                    
                                                    r'/opt/venv/lib/python3.9/site-packages/debugpy/_vendored/pydevd'); import   
                                                    pydevd; pydevd.PydevdCustomization.DEFAULT_PROTOCOL='http_json';             
                                                    pydevd.settrace(host='127.0.0.1', port=40715, suspend=False,                 
                                                    trace_only_current_thread=False, patch_multiprocessing=True, access_token='44
                                                    3f67fee0797ef379661733f67f41ce1aa7e738b6ef7c4d75a00453bfa944c0',             
                                                    client_access_token=None, __setup_holder__={'access-token':                  
                                                    '443f67fee0797ef379661733f67f41ce1aa7e738b6ef7c4d75a00453bfa944c0', 'client':
                                                    '127.0.0.1', 'json-dap-http': True, 'multiprocess': True, 'port': 40715,     
                                                    'ppid': 1, 'server': False, 'skip-notify-stdin': True}); from                
                                                    multiprocessing.spawn import spawn_main; spawn_main(tracker_fd=6,            
                                                    pipe_handle=8) --multiprocessing-fork  

kafonek@DESKTOP-0MLN0FF:~/test_app$ dc exec backend py-spy top --pid 20577
Error: Failed to get process executable name. Check that the process is running.
Reason: No such file or directory (os error 2)
``