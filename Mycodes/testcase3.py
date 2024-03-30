#!/usr/bin/env python
# coding: utf-8

# In[8]:


from datetime import date
from Tour import Tour  # Assuming Tour class is defined in Tour.py
from Buyticket import BuyTicket  # Assuming BuyTicket class is defined in BuyTicket.py
from Guide import Guide

# Create an instance of the Tour class
tour = Tour(date=date(2024, 3, 25), groupofvisitor=20, guideName="Abdullah")

# Create an instance of the BuyTicket class for the tour
ticket = BuyTicket(ticketId=1, purpose="Tour", price=63.0, date=date(2024, 3, 25))

# Calculate total bill for the tour
quantity = 20  # Assuming there are 20 visitors in the tour group
total_bill = ticket.calculate_total_bill(quantity)

# Print payment receipt
print("Payment Receipt for Tour:")
print("Date:", tour.getDate())
print("Tour Guide:", tour.getGuideName())
print("Number of Visitors:", tour.getGroupOfVisitor())
print("Purpose:", ticket.purpose)
print("Ticket Price per Person:", ticket.price)
print("Total Price (including 5% VAT and 50% discount for tours):", total_bill)


# In[ ]:




