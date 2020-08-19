VERSION=0.0.1

build:
	docker build -t hello-world-python:${VERSION} .
run:
	docker run --name "hello-world" -d -p 8080:8080 hello-world-python:${VERSION}

app: build run
