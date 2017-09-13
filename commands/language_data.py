def buildCommand(container_name, compiler, file_name, run=''):
    def create_command(cwd):
        command = ["docker", "run", "--rm", "-it", "-v", f"{cwd}:/usr/src/app", "-w", "/usr/src/app", container_name, compiler] 
        command.extend([run, file_name]) if run else command.append(file_name)
        return command
    return create_command

python_container_name = 'python'
python_compiler = 'python'
python_file = 'function.py'
python_data = {
    'setup': ["docker", "run", "--name", python_container_name, "-d", "-it", python_container_name],
    'file_name': python_file,
    'default_code': "print('Hello from within the python container')",
    'command': buildCommand(python_container_name, python_compiler, python_file)
}

javascript_container_name = 'node'
javascript_compiler = 'node'
javascript_file = 'function.js'
javascript_data = {
    'setup': ["docker", "run", "--name", javascript_container_name, "-d", "-it", javascript_container_name],
    'file_name': 'function.js',
    'default_code': "console.log('Hello from within the javascript container')",
    'command': buildCommand(javascript_container_name, javascript_compiler, javascript_file)
}

go_container_name = 'golang'
go_compiler = 'go'
go_exec = 'run'
go_file = 'main.go'
go_data = {
    'setup': ["docker", "run", "--name", go_container_name, "-d", "-it", go_container_name],
    'file_name': 'main.go',
    'default_code': """
package main
import "fmt"

func main() {
    fmt.Println("Hello from within the Golang container")
}
    """,
    'command': buildCommand(go_container_name, go_compiler, go_file, go_exec)
}