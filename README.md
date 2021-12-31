# Kubernetes Python Flask Microservice
This project deploys a Python Flask microservice that performs money change. It is set to run locally with Docker or converted to Kubernetes.

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
  ]```
- To stop the docker container, press ```Ctrl + C```.

## Run Kubernetes Locally
- Check Kubernetes is ready with ```kubectl get nodes```.
- Run ```make run-kube``` to setup the load balanced service and run it.
- Check the container is running ```kubectl get pods```
- Describe the load balanced service: ```kubectl describe services hello-flask-change-service```
- Invoke the endpoint ```curl http://foo:8080/change/1/34```
  - Should return again:
  ```
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
  ]```
  
## Cleanup
To cleanup the deployment of kubernetes services: ```kubectl delete deployment hello-python```
