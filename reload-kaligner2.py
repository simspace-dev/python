import os, sys
path = os.path.expanduser("~/Library/Application Support/krita/pykrita/kaligner")
from kaligner.kaligner import *

#del sys.modules['kaligner']
#del sys.modules['kaligner.kaligner']
  
if 'kaligner.kaligner' in sys.modules:
    from importlib import reload
    print("Reloading kaligner.kaligner'")
    objkk = reload(sys.modules['kaligner.kaligner'])
    print(objkk)
    docker = objkk.KalignerDocker().clearKalignerLayers()
else:
    print("Importing kaligner.kaligner'")
    from kaligner import (kaligner)

