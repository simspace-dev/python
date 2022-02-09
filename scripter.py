from krita import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

dockersList = Krita.instance().dockers()
kalignerDocker = None

for docker in dockersList:
    if docker.objectName() == 'kaligner':
        print(docker.objectName()) #
        kalignerDocker = docker
        
print(kalignerDocker.layout().count())
print("kalignerDocker is a: %s type" %(kalignerDocker.metaObject().className()))
print("kalignerDocker Layout is a: %s type" %(kalignerDocker.layout().metaObject().className()))


widgets = (kalignerDocker.layout().itemAt(i).widget() for i in range(kalignerDocker.layout().count())) 
for widget in widgets:
    print( "Object: %s MetaObj Name: %s" %(widget.objectName(), widget.metaObject().className()  ) )
    if widget.metaObject().className() == "QWidget":
        kalinerLayout = widget
        print("")
        print( "kalinerLayout.layout.count %s" %(kalinerLayout.layout().count()) )
        elems = (kalinerLayout.layout().itemAt(i).widget() for i in range(kalinerLayout.layout().count())) 
        for elem in elems:
           print( elem )
           # if elem.metaObject().className() == "QLabel":
           # print( "Elem: %s Name: %s" %(elem.objectName(), elem.metaObject().className()  ) )

        
#        for i in range(0, kount):
#            widget = docker.layout().itemAt(i)
#            print(widget.__class__.__name__)

#        while docker.layout().count():
#           widget = docker.layout().takeAt(0)
#           widget = docker.layout().itemAt(0)
#           print(widget.layout().metaObject().className())
#           child.widget().deleteLater()
