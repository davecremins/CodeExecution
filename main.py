from subprocess import call
from utilities.timer import CommandTimer as CT

def execute_cmd(command=["docker", "ps"]):
    call(command)

if(__name__ == '__main__'):
    with CT():
        execute_cmd(["docker", "run", "--rm", "-it", "python_and_docker", "/bin/bash"])