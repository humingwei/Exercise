import unittest

from player import Hero
from player import Enemy,Magic
from player import ZhuangBei

class TestHero(unittest.TestCase):
    def test_init_hero(self):
        hero = Hero(name='hmw', hp=100)
        self.assertEqual(hero.name, 'hmw')
        self.assertEqual(hero.hp, 100)

    def test_hero_zengjia_shuxing(self):
        hero=Hero(name='Team1', hp=100, att=10, def_1=10)
        self.assertEqual(hero.name, 'Team1')
        self.assertEqual(hero.hp, 100)
        self.assertEqual(hero.att, 10)
        self.assertEqual(hero.def_1, 10)

    def test_init_enemy(self):
        enemy = Enemy(name ='goblin1',hp =100,weight=70)
        self.assertEqual(enemy.name, 'goblin1')
        self.assertEqual(enemy.hp, 100)
        self.assertEqual(enemy.weight, 70)

    def test_ini_attack(self):
        hero=Hero(name='casper',hp=100)
        enemy=Enemy(name='sp',hp=100,weight=100)
        hero.attack(enemy)
        self.assertEqual(enemy.hp, 100)

    def test_ini_gongji(self):
        hero=Hero(name='lilei',hp=100,weight=100,att=100)
        enemy=Enemy(name='elong',hp=1000,weight=20,att=150,def_2=50)
        hero.attack(enemy)
        self.assertEqual(enemy.hp,750)
 
    def test_init_magic(self):
        magic = Magic(title="recover", category="big")
        self.assertEqual(magic.title, "recover")
        self.assertEqual(magic.category, "big")
        enemy = Enemy(name="yangshuai", weight=100, hp=50, mp=100)
        magic.effect(enemy)
        self.assertEqual(enemy.hp,100)
        self.assertEqual(enemy.mp,80)

    def test_zhuangbei(self):
        hero=Hero(name='casper',hp=100,lv=25,weight=100,att=15,def_1=10)
        baoshi=ZhuangBei(name='baoshi1',zblv=6,hp=1000)
        dao=ZhuangBei(name='dao1',zblv=6,att=10)
        dun=ZhuangBei(name='dun1',zblv=6,def_1=5)
        hero.zhuangbei(baoshi)
        hero.zhuangbei(dao)
        hero.zhuangbei(dun)
        self.assertEqual(hero.hp,1100)
        self.assertEqual(hero.att,25)
        self.assertEqual(hero.def_1,15)

    def test_lvup(self):
        hero=Hero(name='lilei',hp=100,att=10,def_1=10,weight=100,lv=1)
        for i in range(1,11):
            hero.lvup()
            self.assertEqual(hero.hp,100+i*10)
            self.assertEqual(hero.att,10+i*2)
            self.assertEqual(hero.def_1,10+i)
            self.assertEqual(hero.lv,1+i)
 


if __name__ == '__main__':
    unittest.main()
