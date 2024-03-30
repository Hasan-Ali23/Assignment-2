#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import datetime
from datetime import date

#make class to buy ticket
class BuyTicket:
    def __init__(self, ticketId, purpose, price, date):
        self.ticketId = ticketId
        self.purpose = purpose
        self.price = price
        self.date = date

    # i would like to create method to get ticketId
    def getTicketId(self):
        return self.ticketId

 # i would like to create method to set ticketId
    def setTicketId(self, ticketId):
        self.ticketId = ticketId

 # i would like to create method to get purpose
    def getPurpose(self):
        return self.purpose

 # i would like to create method to set purpose
    def setPurpose(self, purpose):
        self.purpose = purpose

 # i would like to create method to get price
    def getPrice(self):
        return self.price

  # i would like to create method to set price
    def setPrice(self, price):
        self.price = price

 # i would like to create method to get date
    def getDate(self):
        return self.date

 # i would like to create method to set date
    def setDate(self, date):
        self.date = date
        
        
 # i would like to create Method to calculate total bill with VAT and discount for tours
    def calculate_total_bill(self, quantity):
        total_price = self.price * quantity

        # Apply 5% VAT
        total_price_with_vat = total_price * 1.05

        # Apply discount for tours
        if self.purpose.lower() == "tour":
            total_price_with_vat *= 0.5  # 50% discount for tours

        return total_price_with_vat


# In[ ]:




