from subprocess import call

def execute_cmd(command=["docker", "ps"]):
    call(command)

if(__name__ == '__main__'):
    execute_cmd(["docker", "run", "-it", "python_and_docker", "/bin/bash"])