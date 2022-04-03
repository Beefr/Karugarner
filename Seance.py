
from Objet import Objet

class Seance(object):
    id=0 #TODO: modify it for yymmjj+id

    def __init__(self, objectList):
        self._objectList=objectList
        self.__class__.id=self.__class__.id+1
        self._current=0


    @property
    def objectList(self):
        return self._objectList


    @property  
    def current(self):
        return self._current 

    @objectList.setter
    def objectList(self, objectList):
        self._objectList=objectList
        
        
    def addObject(self, objet):
        self._objectList.append(objet)
        
    def removeObject(self, objectId):
        for i in self._objectList:
            if i.id==objectId:
                self._objectList.remove(i)


    def __str__(self):
        txt=""
        for i in self._objectList:
            txt+=str(i)
        return txt


    def next(self):
        self._current+=1
        try:
            return str(self._objectList[self._current])
        except:
            return "That was the last element to sell"



