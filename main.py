from subprocess import call
from utilities.timer import Timer

def execute_cmd(command=["docker", "ps"]):
    call(command)

if(__name__ == '__main__'):
    with Timer() as t:
        execute_cmd(["docker", "run", "--rm", "-it", "python_and_docker", "/bin/bash"])
    print(f'Command lasted: {t.elapsed_in_secs} secs')