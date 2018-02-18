
class Avatar(object):
    def __init__(self,name,hp=100,position=(1,1)):
        self.name=name
        self.hp=hp
        self.position=position
    def getName(self):
        return self._name
    def setName(self,value):
        self._name=value
    def getHP(self):
        return self._hp
    def setHP(self,value):
        self._hp=value
    def getPosition(self):
        return self._position
    def setPosition(self,value):
        self._position=value
    def heal(self,amount=1):
        if amount>0:
            self.hp+=amount
    def attacked(self,amount=-1):
        if amount<0:
            self.hp+=amount
        
    name= property(getName,setName)
    hp= property(getHP,setHP)
    position= property(getPosition,setPosition)


print 'test 1: __init__'
a=Avatar('John')
print (a.name, a.hp, a.position)
print 'test 2: __init__'
a=Avatar('Jane',150,(10,10))
print (a.name, a.hp, a.position)
print 'test 3: getName(), setName()'
a=Avatar('John')
a.setName('Jude')
print a.getName()
print 'test 4: getPosition(), setPosition()'
a=Avatar('John')
a.setPosition((1,3))
print a.getPosition()
print 'test 5: getHP(), setHP()'
a=Avatar('John')
a.setHP(200)
print a.getHP()
print 'test 6: heal()'
a=Avatar('John')
a.heal(5)
print a.getHP()
print 'test 7: attacked()'
a=Avatar('John')
a.attacked(20)
print a.getHP()
print 'test 8: heal()'
a=Avatar('John')
a.heal()
print a.getHP()
print 'test 9: attacked()'
a=Avatar('John')
a.attacked()
print a.getHP()
print 'test 10: heal(), attacked() '
a=Avatar('John')
a.attacked(2)
a.heal(-2)
print a.getHP()