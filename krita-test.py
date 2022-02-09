from krita import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

QtCore.qDebug("RELOADING EXTENSION FROM KRITA_MENU")
# keys = '\n'.join(sys.modules.keys())
# QtCore.qDebug(f'keys: {keys}')

try:
    # Execution from Krita menu
    sys.path.append(os.path.realpath("~/Library/Application Support/krita/pykrita/kaligner"))

    if 'kaligner' in sys.modules:
        from importlib import reload
        print("Reload pyKritaLib")
        reload(sys.modules['kaligner'])
    elif 'kaligner.kaligner' in sys.modules:
        from importlib import reload
        print("Reload pyKritaLib")
        reload(sys.modules['kaligner.kaligner'])
    else:
        print("Import kaligner")
        import kaligner
    
    from kaligner import (Kaligner, KalignerExtension)
    PLUGIN_EXEC_FROM = 'KRITA_MENU'
except:
    # Execution from 'Scripter' plugin
    # In this case add current plugin in path to let 
    # python being able to find and import files
    #
    # Fix path for your environment
    sys.path.append(os.path.realpath("~/Library/Application Support/krita/pykrita/kaligner"))

    if 'kaligner' in sys.modules:
        from importlib import reload
        print("Reload pyKritaLib")
        reload(sys.modules['kaligner'])
    elif 'kaligner.kaligner' in sys.modules:
        from importlib import reload
        print("Reload pyKritaLib")
        reload(sys.modules['kaligner.kaligner'])
    else:
        print("Import kaligner")
        import kaligner

    from kaligner import (Kaligner, KalignerExtension)
    PLUGIN_EXEC_FROM = 'SCRIPTER_PLUGIN'