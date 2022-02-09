from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from krita import *

dockersList = Krita.instance().dockers()
kalignerDocker = None

for docker in dockersList:
    if docker.objectName() == 'kaligner':
        kalignerDocker = docker
 
widgets = (kalignerDocker.layout().itemAt(i).widget() for i in range(kalignerDocker.layout().count())) 
for widget in widgets:
    print( "Object: %s MetaObj Name: %s" %(widget.objectName(), widget.metaObject().className()  ) )
    if widget.metaObject().className() == "QWidget":
        kalinerLayout = widget
        hLayout = QHBoxLayout()
        hLayout.addWidget(QPushButton("Button One"))
        hLayout.addWidget(QPushButton("Button Two"))
        kalinerLayout.layout().addLayout(hLayout)
