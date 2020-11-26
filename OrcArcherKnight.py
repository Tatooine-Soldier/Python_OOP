class Character:
    
    def __init__(self, name, strength):
        self._name = name 
        self._strength = strength
    
    def getName(self):
        return self._name
    
    def setName(self, name):
        if type(name) != str:
            print("type ERROR")       #must be a string
        else:
            self._name = name
            
    def getStrength(self):
        return self._strength
    
    def setStrength(self, strength):
        if type(strength) != float:
            print("type ERROR")    #must be a float
        elif float(strength) > 5:                   
            self._strength = 5.0
        elif float(strength) < 0:
            self._strength = 0.0
        else:
            self._strength = strength
            
    def __str__(self):
        return "{} {} ".format(self._name, self._strength)

    name = property(getName, setName)
    strength = property(getStrength, setStrength)
    
    
    


class Orc(Character):
    
    def __init__(self, name, strength, weapon):
        Character.__init__(self, name, strength)
        self._weapon = weapon
            
            
    def getWeapon(self):
        return self._weapon
    
    def setWeapon(self,weapon):
        if type(weapon) != bool:
            print("type ERROR")    #must be a boolean
        else: 
            self._weapon = weapon
            
            
    def fight(self, other):
        try:
            if self._weapon and not other._weapon:
                if self._strength > 0:
                    if self._strength >= 5:
                        self._strength = 5.0
                    elif self._strength > 0 and self._strength <= 4:
                        self._strength += 1
                    else: 
                        self._strength = 5.0
                else:
                    self._strength = 0.0
                print(self)
            elif other._weapon and not self._weapon:
                if other._strength > 0:
                    if other._strength >= 5:
                        other._strength = 5.0
                    elif other._strength > 0 and other._strength <= 4:
                        other._strength += 1
                    else: 
                        other._strength = 5.0
                else:
                    other._strength = 0.0
                print(other)
            else:
                orc1 = self._strength
                orc2 = other._strength
                if orc1 > orc2:                           #using overload operator funcionality
                    if self._strength <= 4 and self._strength > 0:
                        self._strength += 1
                    elif self._strength < 0:
                        self._strength = 0.0
                    else: 
                        self._strength = 5.0 
                    print(self)                           #using str method
                elif orc2 > orc1:
                    if other._strength > 0 and other._strength <= 4:
                        other._strength += 1
                    elif other._strength < 0:
                        other._strength = 0.0
                    else:
                        other._strength = 5.0
                    print(other)
                else:                                       #if there is no ">" winner, decrement both .5
                    self._strength -= .5                           
                    other._strength -= .5
        except:
            if self._strength > other._strength:
                if self._strength > 0 and self._strength < 4:
                    self._strength += 1
                elif self._strength > 4:
                    self._strength = 5.0
                else:
                    self._strength = 0.0
                print(self)
            elif other._strength > self._strength:
                if other._strength > 0 and other._strength < 4:
                    other._strength += 1
                elif other._strength > 4:
                    other._strength = 5.0
                else:
                    other._strength = 0.0
                print(other)


    def __str__(self):
        return ("{}  {}  {}".format(self._name, self._strength, self._weapon))
    
    weapon = property(getWeapon, setWeapon)
    
    
    



class Archer(Character):
    
    def __init__(self, name, strength, kingdom):
        Character.__init__(self, name, strength)
        self._kingdom = kingdom
       
        
    def getKingdom(self):
        return self._kingdom
    
    def setKingdom(self, kingdom):
        if type(kingdom) != str:
            print("Type ERROR")
        else: 
            self._kingdom = kingdom
            
            
    def fight(self, other):            #Archer fight does not have same exact funcionality as Orc fight
        try:                           #only orcs have coded weapons so this test guarantees knight only fights an orc
            if other.weapon == True or other.weapon == False:
                if self._strength > other._strength:
                    if self._strength > 0:
                        if self._strength >= 5:
                            self._strength = 5.0
                        elif self._strength <= 4 and self._strength > 0:
                            self._strength += 1
                        else:
                            self._strength = 5.0
                    print(self)
                elif other._strength > self._strength:
                    if other._strength > 0:
                        if other._strength >= 5:
                            other._strength = 5.0
                        elif other._strength > 0 and other._strength <= 4:
                            other._strength += 1
                        else: 
                            other._strength = 5.0
                    print(other)
                else:                                      
                    self._strength -= .5                           
                    other._strength -= .5
            else:
                print("Fight ERROR")
        except:
            print("Fight ERROR")
    
    
        
    def __str__(self):
        return ("{} {} {}".format(self._name, self._strength, self._kingdom))
    
    kingdom = property(getKingdom, setKingdom)
    
    


    
    


class Knight(Archer):                              
    
    
    def __init__(self, name, strength, kingdom, archers_list):
        Archer.__init__(self, name, strength, kingdom)
        newlist = []
        self._kingdom = kingdom
        for val in archers_list:
            newlist.append(str(val))
        archers_list = newlist
        self._archers_list = newlist

       
    def getArchers_List(self):
        return self._archers_list
    
    def setArchers_List(self, archers_list):
        if type(archers_list) != list:
            print("type ERROR")
        else:
            return self._archers_list 

    
        
    def __str__(self):
        return "{} {} {} {}".format(self._name, self._strength, self._kingdom, self._archers_list)  
    
    
    archers_list = property(getArchers_List, setArchers_List)