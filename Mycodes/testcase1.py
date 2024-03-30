#!/usr/bin/env python
# coding: utf-8

# In[13]:


from datetime import date
from Buyticket import BuyTicket
from Visitor import Visitor

# Define visitor details
visitor_details = Visitor(visitorId=123, visitorName='Hassan', visitorAge=20, emiratesId=123456789, visitorCategory='Adult')

# Define event details
event_details = {'name': 'Concert', 'date': date(2024, 5, 15), 'location': 'Outdoor Spaces'}

# Create an instance of the BuyTicket class with visitor details
ticket = BuyTicket(1, "Concert", 63.0, date(2024, 5, 15))

# Calculate total bill
quantity = 1
total_bill = ticket.calculate_total_bill(quantity)

# Print visitor details, event details, and total bill
print("Visitor Details:")
print("Visitor Name:", visitor_details.visitorName)
print("Visitor Age:", visitor_details.visitorAge)
print("Emirates ID:", visitor_details.emiratesId)
print("Visitor Category:", visitor_details.visitorCategory)
print()
print("Event Details:")
print("Event Name:", event_details['name'])
print("Event Date:", event_details['date'])
print("Event Location:", event_details['location'])
print()
print("Total Bill (including 5% VAT):", total_bill)


# In[ ]:




