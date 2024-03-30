#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Catalog:
    def __init__(self):
        #i would like to Initialize empty lists to store artworks, artifacts, and exhibitions
        self.artworks = []
        self.artifacts = []
        self.exhibitions = []

   #i would like to create Method to add an artwork to the catalog
    def addArtwork(self, artwork):
        self.artworks.append(artwork)

   #i would like to create  Method to remove an artwork from the catalog
    def removeArtwork(self, artwork):
        if artwork in self.artworks:
            self.artworks.remove(artwork)

    #i would like to create Method to add an artifact to the catalog
    def addArtifact(self, artifact):
        self.artifacts.append(artifact)

   #i would like to create  Method to remove an artifact from the catalog
    def removeArtifact(self, artifact):
        if artifact in self.artifacts:
            self.artifacts.remove(artifact)

     #i would like to create  Method to add an exhibition to the catalog
    def addExhibition(self, exhibition):
        self.exhibitions.append(exhibition)

   #i would like to create  Method to remove an exhibition from the catalog
    def removeExhibition(self, exhibition):
        if exhibition in self.exhibitions:
            self.exhibitions.remove(exhibition)



# In[ ]:




