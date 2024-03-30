#!/usr/bin/env python
# coding: utf-8

# In[1]:


#make class learningprogram
class LearningPrograms:
    def __init__(self, programId, programName, duration, fee, studentCapacity, language):
        self.programId = programId
        self.programName = programName
        self.duration = duration
        self.fee = fee
        self.studentCapacity = studentCapacity
        self.language = language

    # i would like to create method to get programId
    def getProgramId(self):
        return self.programId

   # i would like to create method to set programId
    def setProgramId(self, programId):
        self.programId = programId

  # i would like to create method to get programName
    def getProgramName(self):
        return self.programName

 # i would like to create method to set programName
    def setProgramName(self, programName):
        self.programName = programName

   # i would like to create method to get duration
    def getDuration(self):
        return self.duration

  # i would like to create method to set duration
    def setDuration(self, duration):
        self.duration = duration

  # i would like to create method to get fee
    def getFee(self):
        return self.fee

  # i would like to create method to set fee
    def setFee(self, fee):
        self.fee = fee

  # i would like to create method to get studentCapacity
    def getStudentCapacity(self):
        return self.studentCapacity

  # i would like to create method to set studentCapacity
    def setStudentCapacity(self, studentCapacity):
        self.studentCapacity = studentCapacity

  # i would like to create method to get language
    def getLanguage(self):
        return self.language

 # i would like to create method to set language
    def setLanguage(self, language):
        self.language = language



# In[ ]:




