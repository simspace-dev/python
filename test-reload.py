import sys
import textwrap
import sys, importlib

names = sorted(sys.modules.keys())
name_text = ', '.join(names)
#print(textwrap.fill(name_text))

importlib.reload(sys.modules['kaligner.kaligner'])
