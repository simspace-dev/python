import os, sys 
from importlib import reload
from kaligner import kaligner

sys.path.append(os.path.realpath("~/Library/Application Support/krita/pykrita/kaligner"))

print("Reload pyKritaLib")

#reload(sys.modules['kaligner'])
#reload(sys.modules['kaligner.kaligner'])

reload(kaligner)
