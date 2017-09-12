PD = 'python_and_docker'
DI = 'django_interface'

build-python:
	@docker build -t ${PD} .
python:
	@docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -ti ${PD}
build-django:
	@cd Interface/ && docker build -t ${DI} .
django:
	@cd Interface/ && docker run -p 8000:8000 --rm -ti ${DI}
django-bash:
	@docker exec -ti ${DI} /bin/bash
django-detached:
	@cd Interface/ && docker run --name ${DI} -d -p 8000:8000 --rm -ti ${DI}
clean:
	@docker container prune
	@docker image prune