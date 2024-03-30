#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import datetime
from datetime import datetime

#make class special event
class Specialevent:
    def __init__(self, purpose, duration, location):
        self.purpose = purpose
        self.duration = duration
        self.location = location

    # i would like to make method to get purpose
    def getPurpose(self):
        return self.purpose

   # i would like to make method to set purpose
    def setPurpose(self, purpose):
        self.purpose = purpose

  # i would like to make method to get duration
    def getDuration(self):
        return self.duration

  # i would like to make method to set duration
    def setDuration(self, duration):
        self.duration = duration

 # i would like to make method to get location
    def getLocation(self):
        return self.location

  # i would like to make method to set location
    def setLocation(self, location):
        self.location = location


# In[ ]:




