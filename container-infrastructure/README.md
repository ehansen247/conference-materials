## Run Examples


### First example

- `docker-compose up`
- check `localhost:5000/host` and `localhost:50001/host`

### Second example

- Build haproxy docker image `docker build -f Dockerfile-haproxy -t haproxy:local .
- `docker-compose -f docker-compose-lb.yaml up`