import webbrowser

from .components import polygon
from .components.array import *
from .components.numbers import *
from .components.strings import *
from .components.utils import *
from .components.convert import *


def github():
    webbrowser.open("https://github.com/pranavbaburaj")


def credits():
    return "Created by Pranav Baburaj"


def explorer(location=os.getcwd()):
    try:
        os.listdir(location)
        webbrowser.open(location)
        return None
    except:
        return None
