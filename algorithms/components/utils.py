try:
    import httplib
except:
    import http.client as httplib
import os
import platform
import pyautogui

from PIL import ImageGrab


def is_online(ping="www.google.com", timeout=5):
    if isinstance(ping, str):

        conn = httplib.HTTPConnection(str(ping), int(timeout))
        try:
            conn.request("HEAD", "/")
            conn.close()
            return True
        except:
            return False
    else:
        raise TypeError(f"Unexpected type {type(ping)} for ping")


def sysinfo():
    # return the system information
    return {
        "name": platform.uname().node,
        "os": platform.system(),
        "processor": platform.processor()
    }


def screenshot(filename=f"{os.getcwd()}/algo.png"):
    image = ImageGrab.grab()
    try:
        image.save(filename)
    except Exception as a:
        return str(a)


def pos():
    return (
        pyautogui.position()[0],
        pyautogui.position()[1]
    )
