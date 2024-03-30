#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import datetime and catalog
from datetime import datetime
from Catalog import Catalog

# make class Exhibition which is subclass of catalog
class Exhibition(Catalog):
    def __init__(self, title, duration, location):
        super().__init__()
        self.title = title
        self.duration = duration
        self.location = location

   #i would like to create a method to get title
    def getTitle(self):
        return self.title

   #i would like to create a method to set title
    def setTitle(self, title):
        self.title = title

 #i would like to create a method to get duration
    def getDuration(self):
        return self.duration

#i would like to create a method to set duration
    def setDuration(self, duration):
        self.duration = duration

  #i would like to create a method to get location
    def getLocation(self):
        return self.location

   #i would like to create a method to set location
    def setLocation(self, location):
        self.location = location

