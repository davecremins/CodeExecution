import os, sys
from subprocess import call
from utilities.timer import TimeCommand as TC
from commands.language_data import get_language_details

def execute_cmd(command=["ls", "-a"]):
    call(command)

def write_file(*, lang_data):
    f = open(os.path.join(os.getcwd(), lang_data.get('file_name')), 'w')
    f.write(lang_data.get('default_code'))
    f.close()

if(__name__ == '__main__'):
    language = sys.argv[1] if len(sys.argv) > 1 else 'python'
    try:
        lang_data = get_language_details(language)
        write_file(lang_data=lang_data)

        with TC():
            execute_cmd(lang_data.get('command')(os.getcwd()))
    except:
        print(f"The {language} language is not supported right now")