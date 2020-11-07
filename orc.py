#from orcz import *

class Orc:
    
    def __init__(self, name, strength, weapon):
        self._name = name 
        self._strength = strength
        self._weapon = weapon
        
        
    def getName(self):
        return self._name
    
    def setName(self, name):
        if type(name) != str:
            print("{} type ERROR".format(name))       #must be a string
        else:
            self._name = name
            
            
    def getStrength(self):
        return self._strength
    
    def setStrength(self, strength):
        if float(strength) > 5:                   
            self._strength = 5
        elif float(strength) < 0:
            self._strength = 0
        elif type(strength) != float:
            print("'{}' type Error".format(strength))    #must be a float
        else:
            self._strength = strength
            
            
    def getWeapon(self):
        return self._weapon
    
    def setWeapon(self,weapon):
        if type(weapon) != bool:
            print("'{}' type ERROR".format(weapon))    #must be a boolean
        else: 
            self._weapon = weapon
            
            
    def fight(self, other):
        if self._weapon and not other._weapon:
            self._strength += 1
            print("{} > {}".format(self._name, other._name))
        elif other._weapon and not self._weapon:
            other._strength += 1
            print("{} > {}".format(other._name, self._name))
        else:
            if self._strength > other._strength:
                self._strength += 1
                print("{} > {}".format(self._name, other._name))
                print(self)
            elif other._strength > self._strength:
                other._strength += 1
                print(other)
                print("{} > {}".format(other._name, self._name))
            else:                                       #if there is no ">" winner, decrement .5
                self._strength -= .5                           
                other._strength -= .5
            
    def __str__(self):
        return ("{}  {}  {}".format(self._name, self._strength, self._weapon))
    
    name = property(getName, setName)
    strength = property(getStrength, setStrength)
    weapon = property(getWeapon, setWeapon)
    
olga = Orc("Olga", 5, False)   
