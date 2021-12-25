#the code below is largely taken from Patrick Shyu's youtube channel Tech Lead
#https://www.youtube.com/watch?v=QGVCnjXmrNg

class node:
 def __init__(self, children, isword):
  self.children = children
  self.isword = isword

class solution():
  def __init__(self):
   self.trie = None

  def build(self, words):
