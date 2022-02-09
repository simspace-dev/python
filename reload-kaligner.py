from krita import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

sys.path.append(os.path.realpath("~/Library/Application\ Support/krita/pykrita/kaligner"))

try:
    QtCore.qDebug("RELOADING EXTENSION FROM KRITA_MENU")
    from kaligner import (kaligner)
    PLUGIN_EXEC_FROM = 'KRITA_MENU'
except:
    QtCore.qDebug("RELOADING EXTENSION FROM SCRIPTER_PLUGIN")

    if 'kaligner' in sys.modules:
        from importlib import reload
        print("pyKritaLib Reload of kaligner")
        reload(sys.modules['kaligner.kaligner'])
    else:
        print("Import kaligner")
        import kaligner.kaligner

    from kaligner import (Kaligner)
    PLUGIN_EXEC_FROM = 'SCRIPTER_PLUGIN'