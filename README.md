# Kubernetes Python Flask Microservice
This project stablish a Python Flask application service that performs money change. It is set to run locally with Docker or converted to Kubernetes.

## Get started
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
- Install [Kubernetes](https://www.youtube.com/watch?v=MyNnVurtSf0&ab_channel=Simplilearn)
- Create Python virtual enviroment ```python3 -m venv ~/.kube-hello && source ~/.kube-hello/bin/activate```
- Run ```make all``` to install python libraries, lint project and run tests.

## Run Docker Container
- Run ```make build``` to build the image locally
- Run ```make run``` to run the container
- Open a separate terminal
  - Run ```make invoke```. It will call the change function for $1.34.
  This should return 5 quarters, 1 nickels and 4 pennies:
  ```
  curl http://127.0.0.1:8080/change/1/34
  [
    {
      "5": "quarters"
    }, 
    {
      "1": "nickels"
    }, 
    {
      "4": "pennies"
    }
  ]
```
