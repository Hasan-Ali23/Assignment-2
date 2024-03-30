#!/usr/bin/env python
# coding: utf-8

# In[1]:


#make class guide
class Guide:
    def __init__(self, guideId, guideName):
        self.guideId = guideId
        self.guideName = guideName

   # i would like to create method to get guide id
    def getGuideId(self):
        return self.guideId

     # i would like to create method to set guide id
    def setGuideId(self, guideId):
        self.guideId = guideId
        
   # i would like to create method to get guideName
    def getGuideName(self):
        return self.guideName

   # i would like to create method to set guide name
    def setGuideName(self, guideName):
        self.guideName = guideName


# In[ ]:




