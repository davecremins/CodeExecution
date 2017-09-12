PD = 'python_and_docker'
DI = 'django_interface'

build-python:
	@docker build -t ${PD} .
run-python:
	@docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -ti ${PD}
build-django:
	@cd Interface/ && docker build -t ${DI} .
run-django:
	@cd Interface/ && docker run -p 8000:8000 --rm -ti ${DI}
clean:
	@docker container prune
	@docker image prune