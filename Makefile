IMG = 'python_and_docker'

build:
	@docker build -t ${IMG} .
run: build
	@docker run -v /var/run/docker.sock:/var/run/docker.sock -ti ${IMG}