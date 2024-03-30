#!/usr/bin/env python
# coding: utf-8

# In[4]:


from datetime import date
from Exhibition import Exhibition  # Assuming Exhibition class is defined in Exhibition.py


# Create an instance of the Exhibition class with details
new_exhibition = Exhibition(title="Impressionist Art Exhibition", duration=date(2024, 4, 1), location="Exhibition Hall")


# Print confirmation message
print("Exhibition added to the museum catalog successfully:")
print("Title:", new_exhibition.getTitle())
print("Duration:", new_exhibition.getDuration())
print("Location:", new_exhibition.getLocation())


# In[ ]:




