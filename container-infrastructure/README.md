## Run Examples


### First example (2 flask apps)

- `docker-compose up`
- check `localhost:5000/host` and `localhost:50001/host`

### Second example (load balanced flask apps)

- Build haproxy docker image `docker build -f Dockerfile-haproxy -t haproxy:local .
- `docker-compose -f docker-compose-lb.yaml up`

### Third Example (Google Kubernetes Engine)

- `kubectl run nginx --image=nginx --port 8080`