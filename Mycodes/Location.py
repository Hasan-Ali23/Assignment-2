#!/usr/bin/env python
# coding: utf-8

# In[1]:


#make class location
class Location:
    def __init__(self, locationId, locationName):
        self.locationId = locationId
        self.locationName = locationName

    # i would like to create method to get locationId
    def getLocationId(self):
        return self.locationId

   # i would like to create method to set locationId
    def setLocationId(self, locationId):
        self.locationId = locationId

  # i would like to create method to get locationName
    def getLocationName(self):
        return self.locationName

  # i would like to create method to set locationName
    def setLocationName(self, locationName):
        self.locationName = locationName


# In[ ]:




