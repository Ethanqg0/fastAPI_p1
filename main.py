"""
    how to run the server:
        uvicorn main:app --reload #run this in terminal to start server

    flags to add to the command:
        --reload: auto reloads the server when changes are made
        --host: specify host
        --port: specify port
        --workers: specify number of workers. workers are used to handle requests. the more
            workers, the more requests can be handled at once. the default is 1 worker per core
        --log-level: specify log level. default is info. this is important for receiving useful logging info
        --proxy-headers: Indicates whether Uvicorn should trust proxy headers or not. This is important when deploying behind a reverse proxy like Nginx or Apache.
        --proxy-protocol: Enables or disables support for the PROXY protocol, which is often used with load balancers and reverse proxies.
        --limit-concurrency: Limits the maximum number of concurrent connections to the server. This can be useful for controlling the load on your server.
        --limit-max-requests: Specifies the maximum number of requests per worker process before they are recycled. This can help manage memory usage.
        --limit-max-requests-jitter: Adds jitter to the maximum requests limit, which can help distribute load more evenly.
        --ssl-keyfile and --ssl-certfile: If you want to enable HTTPS, you can provide the paths to the SSL certificate and key files.
                
"""

from fastapi import FastAPI, websockets

app = FastAPI() #creates an instance of fastAPI

app.get("/")
async def root():
    return {"message": "Hello World"}