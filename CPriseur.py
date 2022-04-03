
from Seance import Seance
from Objet import Objet

class CPriseur(object):
    id=0

    def __init__(self, name, mail):
        self._name=name
        self._mail=mail
        self.__class__.id=self.__class__.id+1
        self._seanceInProgress=None


    @property
    def name(self):
        return self._name


    @property
    def mail(self):
        return self._mail 
        
    @property
    def seanceInProgress(self):
        return self._seanceInProgress

    @name.setter
    def name(self, name):
        self._name=name
        
        
    @mail.setter
    def mail(self, mail):
        self._mail=mail
        
    @seanceInProgress.setter
    def seanceInProgress(self, seanceInProgress):
        self._seanceInProgress=seanceInProgress
               
        
    def launchSeance(self, seance):
        self._seanceInProgress= seance
        return self._seanceInProgress.objectList[0]
        
    def nextObject(self):
        return self._seanceInProgress.next()
        
    

    
marion= CPriseur('Marion', 'marion@orange.fr')             

obj1= Objet('buste de napoleon', 10, 'c tre moch', 'napoleon')
obj2= Objet('tableau de picasso', 100, 'c tre bo', 'picasso')
obj3= Objet('bd de lanfeust', 1000, 'c tre rigolo', 'lanfeust')
obj4= Objet('sandale d usain bolt', 1000, 'c tre rapide', 'usain bolt')

seance= Seance([obj1, obj2, obj3])
seance.addObject(obj4)

print(marion.launchSeance(seance))
print(marion.nextObject())
print(marion.nextObject())
print(marion.nextObject())
print(marion.nextObject())




