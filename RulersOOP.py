class Rulers:
    
    def __init__(self,name,country,years):   #constructor initialises 
        self.name = name                  #param
        self.country = country            #param
        self.years = years                #param
    
    def getName(self):                    #param name getter
        return self._name
    
    def setName(self, name):              #param name setter
        if type(name) != str:               #error check, must be a string
            print("'{}' is a number not a Name".format(name))           #error message
        else:
            self._name = name
        
    def getCountry(self):                 #param country getter
        return self._country
    
    def setCountry(self, country):
        if type(country) != str:          #error check, must be string
            print("'{}' is a number not a country".format(country))       #error message
        else:
            self._country = country
        
    def getYears(self):                   #param years getter
        return self._years
    
    def setYears(self, years):
        if years > 2020:                  #error check for years that didn't happen yet(i.e. the future)
            print("'{}' is a year in the future, INVALID".format(years))
        else:
            self._years = years
        
    def __str__(self):                    #str method to print the object below
        return ("Name = '{}', Country = '{}', Years = '{}'".format(self._name,self._country,self._years))
    
    name = property(getName, setName)              #property, will display error from the setter method and keeps correct inputs
    country = property(getCountry, setCountry)
    years = property(getYears, setYears)
    
genghis = Rulers("Genghis", "Mongolia", 2007)        #sample entries
#     genghis.country = "Mongolia"
#     genghis.years = 2300                           #will throw an error as year is in the future, but the property means that original correct input is kept 
print(genghis)
lenin = Rulers("Lenin", "Russia", 1917)
print(lenin)
caesar = Rulers("Caesar", "Rome", -50)
caesar.country = "Italy"
print(caesar)
