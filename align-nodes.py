#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
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

def alignTopsToTops():
  for layer in layers:
    if layer != anchorLayer:
      layer.alignmentPoints.top = anchorLayer.alignmentPoints.top

def alignBottomsToTops():
  for layer in layers:
    if layer != anchorLayer:
      layer.alignmentPoints.top = anchorLayer.alignmentPoints.top - layer.dimensions.height

def alignBottomsToBottoms():
  for layer in layers:
    if layer != anchorLayer:
      layer.alignmentPoints.top = anchorLayer.alignmentPoints.bottom - layer.dimensions.height

def alignTopsToBottoms():
  for layer in layers:
    if layer != anchorLayer:
      layer.alignmentPoints.top = anchorLayer.alignmentPoints.bottom

def alignLeftsToLefts():
  for layer in layers:
    if layer != anchorLayer:
      layer.alignmentPoints.left = anchorLayer.alignmentPoints.left

def alignLeftsToRights():
  for layer in layers:
    if layer != anchorLayer:
      layer.alignmentPoints.left = anchorLayer.alignmentPoints.left - layer.dimensions.width

def alignRightsToRights():
  for layer in layers:
    if layer != anchorLayer:
      layer.alignmentPoints.left = anchorLayer.alignmentPoints.right - layer.dimensions.width

def alignRightsToLefts():
  for layer in layers:
    if layer != anchorLayer:
      layer.alignmentPoints.left = anchorLayer.alignmentPoints.right

def alignCenters():
  for layer in layers:
    if layer != anchorLayer:
      layer.alignmentPoints.top = anchorLayer.alignmentPoints.center.y - layer.dimensions.height/2
      layer.alignmentPoints.left = anchorLayer.alignmentPoints.center.x - layer.dimensions.width/2

def alignVerticalCenters():
  for layer in layers:
    if layer != anchorLayer:
      layer.alignmentPoints.top = anchorLayer.alignmentPoints.center.y - layer.dimensions.height/2

def alignHorizontalCenters():
  for layer in layers:
    if layer != anchorLayer:
      layer.alignmentPoints.left = anchorLayer.alignmentPoints.center.x - layer.dimensions.width/2

def alignReset():
  for layer in layers:
    layer.alignmentPoints.top = layer.alignmentPoints.resetOrigin.y
    layer.alignmentPoints.left = layer.alignmentPoints.resetOrigin.x

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
    if event.char == "t":   
      alignTopsToTops()
    elif event.char == "y": 
      alignBottomsToTops()
    elif event.char == "b": 
      alignBottomsToBottoms()
    elif event.char == "n": 
      alignTopsToBottoms()
    elif event.char == "f": 
      alignLeftsToLefts()
    elif event.char == "d": 
      alignLeftsToRights()
    elif event.char == "h": 
      alignRightsToRights()
    elif event.char == "j": 
      alignRightsToLefts()
    elif event.char == "g": 
      alignCenters()
    elif event.char == "v": 
      alignVerticalCenters()
    elif event.char == "c": 
      alignHorizontalCenters()
    elif event.char == "r": 
      alignReset()

    for layer in layers:
      if layer != anchorLayer:
        index = layers.index(layer)
        myCanvas.moveto(layerShapes[index], layer.alignmentPoints.left, layer.alignmentPoints.top)

#-------------------------------------------------------------------

# doc = Krita.instance().activeDocument()
doc = knode("document", point(100,100), dimensions(800, 800), "white")

# node = doc.activeNode()
anchorLayer = knode("anchorLayer", point(250,250), dimensions(300, 300), "red")
layer = knode("layer", point(450,50), dimensions(200, 100), "green")
layer3 = knode("layer3", point(50,650), dimensions(400, 50), "blue")

layerShapes = []
layers = [anchorLayer, layer, layer3]
anchorLayer = layers[0]

# init tk
root = Tk()
windowPosition = f'+{doc.alignmentPoints.topLeft.x}+{doc.alignmentPoints.topLeft.y}'
root.geometry(windowPosition)
root.bind("<Key>", keypress)

# create canvas
myCanvas = Canvas(root, bg="white", height=doc.dimensions.height, width=doc.dimensions.width)

# draw arcs
for layer in layers:
  print("%s center point: %s, %s" %(layer.name, layer.alignmentPoints.center.x, layer.alignmentPoints.center.y) )
  layerShape = myCanvas.create_rectangle(layer.alignmentPoints.topLeft.x, layer.alignmentPoints.topLeft.y, layer.alignmentPoints.bottomRight.x, layer.alignmentPoints.bottomRight.y, fill=f'{layer.color}')
  layerShapes.append(layerShape)

# add to window and show
myCanvas.pack()
root.mainloop()
