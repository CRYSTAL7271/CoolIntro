import os
from tqdm import tqdm
import sys
import json
import time

def start():
    def animated_text():
        if data["animated_text"]==True:
            message = data["animation_text"]
            for char in message:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            print("\n")
        else:
            sys.exit(0)
    try:
        f=open("CoolIntro/.assets/scripts/data.json", "r")
        data=json.loads(f.read())
        f.close()
        if data["big_text_show"]==True:
            os.system("termimage" + data["img_path"])
            animated_text()
        else:
            animated_text()
    except Exception as e:
        print(e)
        sys.exit(0)
start()
