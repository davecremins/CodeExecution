import os
from subprocess import call
from utilities.timer import TimeCommand as TC
from commands.language_data import go_data as python

def execute_cmd(command=["ls", "-a"]):
    call(command)

def writeFile(*, cwd, file_name):
    f = open(os.path.join(cwd, file_name), 'w')
    f.write(python.get('default_code'))
    f.close()

if(__name__ == '__main__'):
    cwd = os.getcwd()
    writeFile(cwd=cwd, file_name=python.get('file_name'))

    with TC():
        # execute_cmd(["docker", "run", "--name", "python_and_docker" ,"--rm", "-it", "python_and_docker", "/bin/bash"])
        # execute_cmd(["docker", "run", "--rm", "-it", "-v", f"{os.getcwd()}:/usr/src/app", "-w", "/usr/src/app", "python_and_docker", "python", "-c", "print('Hello from within the container')"])
        # execute_cmd(["docker", "run", "--rm", "-it", "-v", f"{cwd}:/usr/src/app", "-w", "/usr/src/app", "python_and_docker", "python", "./function.py"])
        execute_cmd(python.get('command')(cwd))
        # execute_cmd(["docker", "run", "--rm", "-it", "-v", f"{cwd}:/usr/src/app/", "-w", "/usr/src/app", "python_and_docker", "/bin/bash"])
        # execute_cmd(["docker", "run", "-it", "-v", f"{cwd}:/usr/src/app", "python_and_docker", "bin/bash/"])
