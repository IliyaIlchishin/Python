

import sys
import time

def loading():
    loading= "LOADING\n"
    bar = "[==========]"
    print(loading)
    for c in bar:
        time.sleep(0.1)
        sys.stdout.write(c)
        sys.stdout.flush()
    print()
    print('Completed. 100%')
