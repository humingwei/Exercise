class Hero(object):
    def __init__(self, name, hp,att=10,def_1=10, weight=100, lv=1):
        self.lv= lv
        self.name = name
        self.hp = hp
        self.att = att
        self.def_1 = def_1
        self.weight= weight
        

    def attack(self,enemy):
      #  enemy.hp-=1
        damage=(self.weight/enemy.weight)*(self.att-enemy.def_2)
        if damage>0: 
            enemy.hp-=damage

    def zhuangbei(self,zb):
        if self.lv >= zb.zblv:
            self.hp+=zb.hp
            self.att+=zb.att
            self.def_1+=zb.def_1
        
    def lvup(self):
        self.hp+=10
        self.att+=2
        self.def_1+=1
        self.lv+=1

class Enemy(object):

    def __init__(self, name, hp, weight, att=100, def_2=100,mp =100):
        self.name = name
        self.hp = hp
        self.weight = weight
        self.att= att
        self.def_2= def_2
        self.mp = mp

class Magic(object):
    def __init__(self,title,category):
        self.title = title
        self.category =  category

    def effect(self,enemy):
        if enemy.mp >=20:
            enemy.hp +=50
            enemy.mp -=20
        
class ZhuangBei(object): 
    def __init__(self,name,zblv,hp=0,att=0,def_1=0):
        self.name=name
        self.zblv=zblv
        self.hp=hp
        self.att=att
        self.def_1=def_1
    

