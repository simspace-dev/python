#!/usr/bin/python
# -*- coding: UTF-8 -*-

## TODO: Create kaligner docker with:
#        List of layers to align
#        11 alignment buttons
#        11 assignable keystokes?

from tkinter import *
from textwrap import fill
# from krita import *

#-------------------------------------------------------------------
class dimensions():
  def __init__(self, width, height):
    self.width = width
    self.height = height 
#-------------------------------------------------------------------
class point():
 def __init__(self, a, b):
     self.x = a
     self.y = b 
 def translateXY(self, other):
     return point(self.x + other.x, self.y + other.y)
 def translateX(self, other):
     return point(self.x + other.x, self.y)
 def translateY(self, other):
     return point(self.x, self.y + other.x)
#-------------------------------------------------------------------
class alignmentPoints():
  def __init__(self, origin, dimensions):
      self.resetOrigin = origin
      self.center = point(dimensions.width/2+origin.x, dimensions.height/2+origin.y)
      self.topLeft = origin
      self.topRight = point(origin.x+dimensions.width, origin.y)
      self.topCenter = point(self.center.x, origin.y)
      self.bottomLeft = point(origin.x, origin.y+dimensions.height)
      self.bottomRight = point(origin.x+dimensions.width, origin.y+dimensions.height)
      self.bottomCenter = point(self.center.x, origin.y+dimensions.height)
      self.top = self.topLeft.y
      self.bottom = self.bottomLeft.y
      self.left = self.topLeft.x
      self.right = self.topRight.x
#-------------------------------------------------------------------
class knode():
  def __init__(self, name, origin, dimensions, color):
    self.name = name
    self.dimensions = dimensions
    self.alignmentPoints = alignmentPoints(origin, dimensions)
    self.color = color
##-------------------------------------------------------------------
def distrubuteHorizontally():
  print("need to implement")

def distrubuteVertically():
  print("need to implement")

def alignTopsToTops(layerToAlign):
  layerToAlign.alignmentPoints.top = anchorLayer.alignmentPoints.top

def alignBottomsToTops(layerToAlign):
  layerToAlign.alignmentPoints.top = anchorLayer.alignmentPoints.top - layerToAlign.dimensions.height

def alignBottomsToBottoms(layerToAlign):
  layerToAlign.alignmentPoints.top = anchorLayer.alignmentPoints.bottom - layerToAlign.dimensions.height

def alignTopsToBottoms(layerToAlign):
  layerToAlign.alignmentPoints.top = anchorLayer.alignmentPoints.bottom

def alignLeftsToLefts(layerToAlign):
  layerToAlign.alignmentPoints.left = anchorLayer.alignmentPoints.left

def alignLeftsToRights(layerToAlign):
  layerToAlign.alignmentPoints.left = anchorLayer.alignmentPoints.left - layerToAlign.dimensions.width

def alignRightsToRights(layerToAlign):
  layerToAlign.alignmentPoints.left = anchorLayer.alignmentPoints.right - layerToAlign.dimensions.width

def alignRightsToLefts(layerToAlign):
  layerToAlign.alignmentPoints.left = anchorLayer.alignmentPoints.right

def alignCenters(layerToAlign):
  layerToAlign.alignmentPoints.top = anchorLayer.alignmentPoints.center.y - layerToAlign.dimensions.height/2
  layerToAlign.alignmentPoints.left = anchorLayer.alignmentPoints.center.x - layerToAlign.dimensions.width/2

def alignVerticalCenters(layerToAlign):
  layerToAlign.alignmentPoints.top = anchorLayer.alignmentPoints.center.y - layerToAlign.dimensions.height/2

def alignHorizontalCenters(layerToAlign):
  layerToAlign.alignmentPoints.left = anchorLayer.alignmentPoints.center.x - layerToAlign.dimensions.width/2

def alignReset(layerToAlign):
  layerToAlign.alignmentPoints.top = layerToAlign.alignmentPoints.resetOrigin.y
  layerToAlign.alignmentPoints.left = layerToAlign.alignmentPoints.resetOrigin.x

##-------------------------------------------------------------------
##         y
##         t
##  
##  d f   vgc   j h
##
##         b
##         n
##-------------------------------------------------------------------
def keypress(event):
  for layer in layers:
    if layer != anchorLayer:
      if event.char == "t":   
        alignTopsToTops(layer)
      elif event.char == "y": 
        alignBottomsToTops(layer)
      elif event.char == "b": 
        alignBottomsToBottoms(layer)
      elif event.char == "n": 
        alignTopsToBottoms(layer)
      elif event.char == "f": 
        alignLeftsToLefts(layer)
      elif event.char == "d": 
        alignLeftsToRights(layer)
      elif event.char == "h": 
        alignRightsToRights(layer)
      elif event.char == "j": 
        alignRightsToLefts(layer)
      elif event.char == "g": 
        alignCenters(layer)
      elif event.char == "v": 
        alignVerticalCenters(layer)
      elif event.char == "c": 
        alignHorizontalCenters(layer)
      elif event.char == "r": 
        alignReset(layer)

  for layer in layers:
    if layer != anchorLayer:
      index = layers.index(layer)
      myCanvas.moveto(layerShapes[index], layer.alignmentPoints.left, layer.alignmentPoints.top)

#-------------------------------------------------------------------

# doc = Krita.instance().activeDocument()
doc = knode("document", point(100,100), dimensions(800, 800), "white")

# node = doc.activeNode()
layers = [
  knode("layer1", point(250,250), dimensions(300, 300), "pink"), 
  knode("layer2", point(450,50), dimensions(200, 100), "orange"), 
  knode("layer3", point(50,650), dimensions(400, 50), "yellow")
]
anchorLayer = layers[0]
layerShapes = []

# init tk
root = Tk()
windowPosition = f'+{doc.alignmentPoints.topLeft.x}+{doc.alignmentPoints.topLeft.y}'
root.geometry(windowPosition)
root.bind("<Key>", keypress)

# create canvas
myCanvas = Canvas(root, bg="white", height=doc.dimensions.height, width=doc.dimensions.width)

# draw arcs
for layer in layers:
  layerShape = myCanvas.create_rectangle(layer.alignmentPoints.topLeft.x, layer.alignmentPoints.topLeft.y, layer.alignmentPoints.bottomRight.x, layer.alignmentPoints.bottomRight.y, fill=f'{layer.color}')
  layerShapes.append(layerShape)

# add to window and show
myCanvas.pack()
root.mainloop()
