import pyperclip
import time

def timeCopy(text, timeToKeep=15):
    try:
        pyperclip.copy(text)
        time.sleep(timeToKeep)
        pyperclip.copy('')
        return True
    except:
        return False

def unlimitedCopy(text):
    pyperclip.copy(text)