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
        execute_cmd(python.get('command')(cwd))
