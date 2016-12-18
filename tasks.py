import string
import random

def run_process(name):
    try:
        subprocess.Popen(["python3","programs/"+name+".py"])
    else:
        return "500"
    return 200
