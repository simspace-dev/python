import os

temp = "~/Library/Application Support/krita/pykrita/kaligner"
tempexpanded = os.path.expanduser(temp)
if not os.path.exists(temp):
    print("Path does not exist")
else:
    print("Path exists")