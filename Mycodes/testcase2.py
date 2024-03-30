#!/usr/bin/env python
# coding: utf-8

# In[9]:


from Catalog import Catalog
from Artwork import Artwork  # Assuming Artwork class is defined in Artwork.py

# Create an instance of the Catalog class
museum_catalog = Catalog()

# Add existing artworks to the catalog (optional)
existing_artwork1 = Artwork(1, "The Bezique Game", "Gustave Caillebotte", "1880", "One of the most famous portraits in the world", "Permanent Galleries")


# Introduce a new artwork to the museum
new_artwork = Artwork(3, "Landscape painting", "Mariam", "2015", "Depicts melting clocks in a dreamlike landscape", "Exhibition Hall")



# Print details of the new artwork
print("Details of the new artwork introduced:")
print("Artwork ID:", new_artwork. getArtworkId())
print("Title:", new_artwork.getArtworkTitle())
print("Artist:", new_artwork.getArtist())
print("Date of Creation:", new_artwork.getDateOfCreation())
print("Historical Significance:", new_artwork.getHistoricalSignificance())
print("Location:", new_artwork.getLocation())

print("New artwork successfully introduced in the museum.")


# In[ ]:




