container_name = 'python'
compiler = 'python'

def buildCommand(cwd):
    return ["docker", "run", "--rm", "-it", "-v", f"{cwd}:/usr/src/app", "-w", "/usr/src/app", container_name, compiler, "function.py"]

python_data = {
    'setup': ["docker", "run", "--name", container_name, "-d", "-it", container_name],
    'default_code': "print('Hello from within the container')",
    'command': buildCommand
}