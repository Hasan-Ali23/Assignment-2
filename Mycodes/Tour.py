#!/usr/bin/env python
# coding: utf-8

# In[3]:


#import guide class and datetime
from datetime import date
from Guide import Guide  

#make class Tour which is a subclass of Guide
class Tour(Guide):
    def __init__(self, date, groupofvisitor, guideName):
        super().__init__(None, guideName)  # Initialize Guide attributes
        self.date = date
        self.groupofvisitor = groupofvisitor
    # i would like to create a method to get date
    def getDate(self):
        return self.date

      # i would like to create a method to set date
    def setDate(self, date):
        self.date = date

      # i would like to create a method to get groupofvisitor
    def getGroupOfVisitor(self):
        return self.groupofvisitor

   # i would like to create a method to set groupofvisitor
    def setGroupOfVisitor(self, groupofvisitor):
        self.groupofvisitor = groupofvisitor
        
# i would like to create a method to get guide name
    def getGuideName(self):
        return self.guideName

# i would like to create a method to set guide name
    def setGuideName(self, guideName):
        self.guideName = guideName


# In[ ]:




