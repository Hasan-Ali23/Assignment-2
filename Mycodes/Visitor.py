#!/usr/bin/env python
# coding: utf-8

# In[1]:


#make class visitor
class Visitor:
    def __init__(self, visitorId, visitorName, visitorAge, emiratesId, visitorCategory):
        self.visitorId = visitorId
        self.visitorName = visitorName
        self.visitorAge = visitorAge
        self.emiratesId = emiratesId
        self.visitorCategory = visitorCategory

    # i would like to craete method to get visitorid
    def getVisitorId(self):
        return self.visitorId

  # i would like to craete method to set visitorId
    def setVisitorId(self, visitorId):
        self.visitorId = visitorId

    # i would like to craete method to get visitorName
    def getVisitorName(self):
        return self.visitorName

    # i would like to craete method to set visitorName
    def setVisitorName(self, visitorName):
        self.visitorName = visitorName

   # i would like to craete method to get visitorAge
    def getVisitorAge(self):
        return self.visitorAge

   # i would like to craete method to set visitorAge
    def setVisitorAge(self, visitorAge):
        self.visitorAge = visitorAge

  # i would like to craete method to get EmiratesId
    def getEmiratesId(self):
        return self.emiratesId

 # i would like to craete method to set EmiratesId
    def setEmiratesId(self, emiratesId):
        self.emiratesId = emiratesId

  # i would like to craete method to get visitorCategory
    def getVisitorCategory(self):
        return self.visitorCategory

 # i would like to craete method to set visitorCategory
    def setVisitorCategory(self, visitorCategory):
        self.visitorCategory = visitorCategory

    #i would like to create Method to buy ticket online
    def buy_ticket_online(self, event_type):
        # Logic to buy ticket online
        print(f"Buying ticket online for {event_type}")

    # i would like to create to buy ticket offline
    def buy_ticket_offline(self, event_type):
        # Logic to buy ticket offline
        print(f"Buying ticket offline for {event_type}")


# In[ ]:




