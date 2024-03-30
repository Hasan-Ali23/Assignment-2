#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import datetime
from datetime import date

#make class museum membership
class MuseumMembership:
    def __init__(self, membershipId, membershipType, startdate, endDate, price):
        self.membershipId = membershipId
        self.membershipType = membershipType
        self.startdate = startdate
        self.endDate = endDate
        self.price = price

    # i would like to create method to get membershipId
    def getMembershipId(self):
        return self.membershipId

   # i would like to create method to set membershipId
    def setMembershipId(self, membershipId):
        self.membershipId = membershipId

  # i would like to create method to get membershipType
    def getMembershipType(self):
        return self.membershipType

  # i would like to create method to set membershipType
    def setMembershipType(self, membershipType):
        self.membershipType = membershipType

  # i would like to create method to get startdate
    def getStartdate(self):
        return self.startdate

   # i would like to create method to set startdate
    def setStartdate(self, startdate):
        self.startdate = startdate

 # i would like to create method to get endDate
    def getEndDate(self):
        return self.endDate

 # i would like to create method to set endDate
    def setEndDate(self, endDate):
        self.endDate = endDate

  # i would like to create method to get price
    def getPrice(self):
        return self.price

  # i would like to create method to set price
    def setPrice(self, price):
        self.price = price

    # i would like to create Method to redeem membership
    def RedeemMembership(self):
        # pass
        print("Membership redeemed successfully.")

    # i would like to create Method to renew membership
    def RenewMembership(self):
        # pass
        print("Membership renewed successfully.")

    # i would like to create Method to gift membership
    def GiftMembership(self):
        # pass
        print("Membership gifted successfully.")



