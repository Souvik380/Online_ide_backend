import  uuid
import os
import subprocess


def create_code_file(code,language):
    file_name=str(uuid.uuid4())+"."+language
    with open("ONLINE_IDE/Code/"+file_name,"w") as f:
        f.write(code)
    return file_name

def execute_code_file(file_name,language):
    print(file_name)
    if language == "cpp":
        result=subprocess.run(["g++", "ONLINE_IDE/Code/"+file_name],stdout=subprocess.PIPE)
        if result.returncode!=0:
            return
        result=subprocess.run(["a.exe"],stdout=subprocess.PIPE)
        if result.returncode != 0:
            return
        return result.stdout.decode(("utf-8"))


