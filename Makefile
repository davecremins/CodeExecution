IMG = 'python_and_docker'

build:
	@docker build -t ${IMG} .
run:
	@docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -ti ${IMG}
clean:
	@docker container prune
	@docker image prune