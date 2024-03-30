#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import  catalog
from Catalog import Catalog

# make class Artwork which is subclass of catalog
class Artwork(Catalog):  # Artwork is a subclass of Catalog
    def __init__(self, artworkId, artworkTitle, artist, dateOfCreation, historicalSignificance, location):
        super().__init__()  # Call the constructor of the Catalog class
        self.artworkId = artworkId
        self.artworkTitle = artworkTitle
        self.artist = artist
        self.dateOfCreation = dateOfCreation
        self.historicalSignificance = historicalSignificance
        self.location = location

    # Getter and setter methods for artworkId
    def getArtworkId(self):
        return self.artworkId

    def setArtworkId(self, artworkId):
        self.artworkId = artworkId

    # Getter and setter methods for artworkTitle
    def getArtworkTitle(self):
        return self.artworkTitle

    def setArtworkTitle(self, artworkTitle):
        self.artworkTitle = artworkTitle

    # Getter and setter methods for artist
    def getArtist(self):
        return self.artist

    def setArtist(self, artist):
        self.artist = artist

    # Getter and setter methods for dateOfCreation
    def getDateOfCreation(self):
        return self.dateOfCreation

    def setDateOfCreation(self, dateOfCreation):
        self.dateOfCreation = dateOfCreation

    # Getter and setter methods for historicalSignificance
    def getHistoricalSignificance(self):
        return self.historicalSignificance

    def setHistoricalSignificance(self, historicalSignificance):
        self.historicalSignificance = historicalSignificance

    # Getter and setter methods for location
    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.location = location


# In[ ]:




