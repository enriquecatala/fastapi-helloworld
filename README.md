# fastapi-helloworld
Very basic API rest for kubernetes demo purposes

>NOTE: This image has been pushed to https://hub.docker.com/r/enriquecatala/fastapi-helloworld

## Setup the container

No special setup required, but the container will return the _HELLOWORLD_ENV_ in the output call. You can edit that variable to check values

In case you are using docker-compose.yml

```yaml
    environment:
      - HELLOWORLD_ENV=enrique catala
```

## Build container

`docker-compose build`

## Run the container locally

`docker-compose up`

## Test the container

1. Go to http://localhost:5000/one/hello
2. Go to http://localhost:5000/two/hello

