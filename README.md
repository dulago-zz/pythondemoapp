# pythondemoapp
This repo contains the configuration to create a simple Python API that runs on Docker and is monitored using Datadog.
-------------------------------------------------
Before building a new version of the image, uppdate the DD_VERSION variable value on the Dockerfile to the version you're going to build.
To build a new version of the Docker image just run:
``` 
docker build -t dulago/pythondemoapp:version .
```
And then
``` 
docker push dulago/pythondemoapp:version
```
-------------------------------------------------
To run the image locally:
``` 
docker run -d -p 80:80 dulago/pythondemoapp:version
```
> Note that this will bind the Docker host's port 80 to the container. If that's not possible, change the first '80' to a port that's available. You'll then need to call the application using this port.

