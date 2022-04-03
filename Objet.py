
import json

class Objet(object):
    id=0

    def __init__(self, name, basePrice, description, vendor):
        self._name=name
        self._basePrice=basePrice
        self._description=description
        self._vendor=vendor
        self.__class__.id=self.__class__.id+1



    @property
    def name(self):
        return self._name

    @property
    def basePrice(self):
        return self._basePrice

    @property
    def description(self):
        return self._description

    @property
    def vendor(self):
        return self._vendor


    @name.setter
    def name(self, name):
        self._name=name


    @basePrice.setter
    def basePrice(self, basePrice):
        self._basePrice=basePrice


    @description.setter
    def description(self, description):
        self._description=description


    @vendor.setter
    def vendor(self, vendor):
        self._vendor=vendor


    def __str__(self):
        return json.dumps([self._name, self._basePrice, self._description, self._vendor])


