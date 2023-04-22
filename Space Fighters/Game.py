from pygame import* 
from random import*
display.set_icon(image.load("Logo.png"))
w = 800 
h = 700 
mixer.init() 
mixer.music.load("06-Robots-Chill-Out.ogg") 
mixer.music.play() 
 
fires = mixer.Sound("LaserGun.ogg")
firm = mixer.Sound("ammo.ogg")
failm = mixer.Sound("Results Death Loop.ogg")
winm = mixer.Sound("Cutscene.ogg")
expl = mixer.Sound("explosion.ogg")
hreschatuk = mixer.Sound("Lublu-Hrechatuk.ogg")


window = display.set_mode((w, h)) 
enemies = sprite.Group()
enemies2 = sprite.Group()
bullets = sprite.Group()


display.set_caption("Space fighters") 
bg = transform.scale(image.load("Space.png"), (800, 700))
bosshp = 15000
lost = 0
herolivesleft = 3
score = 0
uihelp = 0
tx = -200
tx2 = -200
w1x = -40
w2x = -200
FPS = 30
clock = time.Clock() 
class Player(sprite.Sprite): 
    def __init__(self, p_i, p_x, p_y, p_s): 
        super().__init__() 
        self.image = transform.scale(image.load(p_i), (75, 75)) 
        self.speed = p_s  
        self.rect = self.image.get_rect() 
        self.rect.x = p_x  
        self.rect.y = p_y
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Dzidzio(Player):
    def update(self):
        self.rect.y = self.rect.y + self.speed
class Text(sprite.Sprite):
    def __init__ (self, ds_image, ds_x, ds_y): 
        super().__init__() 
        self.image = transform.scale(image.load(ds_image), (800, 700)) 
        self.rect = self.image.get_rect() 
        self.rect.x = ds_x 
        self.rect.y = ds_y
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 


class Boss(Player):
    def __init__(self, b_i, b_x, b_y, b_s):
        self.image = transform.scale(image.load(b_i), (505, 505)) 
        self.speed = b_s  
        self.rect = self.image.get_rect() 
        self.rect.x = b_x  
        self.rect.y = b_y
    def update(self): 
        self.rect.y = self.rect.y + self.speed 
        global lost 
        if self.rect.y > h: 
            lost == 3



class DeathScreen(sprite.Sprite):
    def __init__ (self, ds_image, ds_x, ds_y): 
        super().__init__() 
        self.image = transform.scale(image.load(ds_image), (800, 700)) 
        self.rect = self.image.get_rect() 
        self.rect.x = ds_x 
        self.rect.y = ds_y
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 

class Enemy(Player): 
    def update(self): 
        self.rect.y = self.rect.y + self.speed 
        global lost 
        if self.rect.y > h: 
            self.rect.x = randint(50, 625) 
            self.rect.y = 0 
            lost += 1

class Live(sprite.Sprite):
    def __init__ (self, ls_image, ls_x, ls_y): 
        super().__init__() 
        self.image = transform.scale(image.load(ls_image), (50, 70)) 
        self.rect = self.image.get_rect() 
        self.rect.x = ls_x 
        self.rect.y = ls_y
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y))

class Hero(Player): 
    def update(self): 
        keys = key.get_pressed() 
        if keys[K_a] or keys[K_LEFT] and self.rect.x >= 0: 
            self.rect.x -= self.speed 
        if keys[K_d] or keys[K_RIGHT] and self.rect.x <= 725: 
            self.rect.x += self.speed 
    def fire(self): 
        b = Bullet("Bullet.png", self.rect.centerx, self.rect.top, 5) 
        bullets.add(b)


class Bullet(Player): 
    def update(self): 
        self.rect.y -= self.speed 
        if self.rect.y <= 0: 
            self.kill()

font.init() 
font1 = font.SysFont(None, 150) 
win = font1.render("VICTORY", True, (0, 255, 200)) 
lose = font1.render("FAIL", True, (255, 20, 24)) 
font2 = font.SysFont(None, 45)
scorecount = font2.render("SCORE:" + str(score), True, (255, 255, 255))
help = font2.render("20 000 SCORE TO WIN", True, (255, 20, 45))
help2 = font2.render("SPACE - fire, wasd or arrows - move", True, (50, 255, 50))
record = font2.render("SCORE:" + str(score), True, (255, 0, 0))
liveslefttext = font2.render("LIVES LEFT:" + str(herolivesleft - lost), True, (0, 255, 0))
icecream = font2.render("Дзідзьо підірвав ворожий флот", True, (109, 197, 211))
icecream2 = font2.render("морозивом Хрещатик", True, (109, 197, 211))
icecream3 = font2.render("та взяв вас на екскурсію", True, (109, 197, 211))

warning1 = font2.render("!!!WARNING!!!", True, (255, 0, 0))
warning2 = font2.render("IMPERIAL-CLASS STAR DESTROYER INCOMING", True, (255, 0, 0))
bosshpui = font2.render(str(bosshp), True, (255, 0, 0))


ds = DeathScreen("1343.jpg", 0, 0)
ws = DeathScreen("Win2.jpg", 0, 0)
dzs = DeathScreen("dzidzio screen.jpg",0, 0)
live1 =  Live("Battery.png", 0, 0)
live2 =  Live("Battery.png", 50, 0) 
live3 =  Live("Battery.png", 100, 0) 
hero = Hero("SpaceShip.png", 500, 600, 10)
boss = Boss("kreyser.png", 120, -600, 1)
dzidzio = Dzidzio("dzidzio.png", 725, -100, 30)
text = Text("e.png", 0, 0)
enemies = sprite.Group() 
for i in range (3): 
    monster = Enemy("EnemyShip.png", randint(75, 625), -40, randint(1, 2)) 
    enemies.add(monster) 
for i in range (2): 
    monster2 = Enemy("Star Wars Ship.png", randint(75, 625), -40, randint(2,3 )) 
    enemies2.add(monster2) 
game = True 
finish = False 
while game: 
    for e in event.get(): 
        if e.type == QUIT: 
            game = False 
        elif e.type == KEYDOWN: 
            if e.key == K_SPACE: 
                a = randint(1, 2) 
                if a == 1: 
                    hero.fire()
                    fires.play() 
                if a== 2: 
                    firm.play() 
 
    if finish != True:  
        window.blit(bg,(0,0)) 
        window.blit(scorecount, (0, 100)) 
        enemies.update() 
        enemies2.update() 
        hero.update() 
        hero.reset() 
        enemies.draw(window)
        enemies2.draw(window) 
        bullets.update() 
        bullets.draw(window)
        live1.update()
        live1.reset()
        live2.update()
        live2.reset()
        live3.update()
        live3.reset()
        dzidzio.update()
        dzidzio.reset()
        liveslefttext = font2.render("LIVES LEFT:" + str(herolivesleft - lost), True, (0, 255, 0))
        if score >= 15000:
            w1x += 4
            w2x += 4
            window.blit(warning2, (w2x, 350))
            window.blit(warning1, (w1x, 300))
            boss.update()
            boss.reset()
            window.blit(bosshpui, (280, 0))

    
        window.blit(help, (tx, 300))
        window.blit(help2, (tx2, 350))
        tx += 6
        tx2 += 8

        collides = sprite.groupcollide(enemies, bullets, True, True)  
        collides2 = sprite.groupcollide(enemies2, bullets, True, True)  #create bullets2  amd maybe bulllets3
        for c in collides: 
            score += 250
            expl.play()
            monster = Enemy("EnemyShip.png", randint(75, 625), -40, randint(1, 2))
            liveslefttext = font2.render("LIVES LEFT:" + str(herolivesleft - lost), True, (0, 255, 0))
            if score <= 15000:
                enemies.add(monster) 
            scorecount = font2.render("SCORE:" + str(score), True, (255, 255, 255))
            window.blit(scorecount, (0, 100))
        for c in collides2: 
            score += 250
            expl.play()
            liveslefttext = font2.render("LIVES LEFT:" + str(herolivesleft - lost), True, (0, 255, 0))
            monster2 = Enemy("Star Wars Ship.png", randint(75, 625), -40, randint(3, 4)) 
            if score <= 15000:
                enemies2.add(monster2)
            scorecount = font2.render("SCORE:" + str(score), True, (255, 255, 255))
            window.blit(scorecount, (0, 100))
        
        if sprite.collide_rect(hero, dzidzio):
            mixer.music.stop()
            dzs.update()
            dzs.reset()
            text.update()
            text.reset()
            hreschatuk.play()
           
            finish = True

        if sprite.spritecollide(hero, enemies, False) or lost >= 3:
            mixer.music.stop()
            lost = 3
            expl.play()
            failm.play()
            ds.update()
            ds.reset() 
            window.blit(lose, (265, 300))
            record = font2.render("SCORE:" + str(score), True, (255, 0, 0))
            liveslefttext = font2.render("LIVES LEFT:" + str(herolivesleft - lost), True, (0, 255, 0))
            window.blit(record, (280, 400)) 
            window.blit(liveslefttext, (280, 450))   
            finish = True  
        if sprite.spritecollide(hero, enemies2, False) or lost >= 3:
            lost = 3
            mixer.music.stop()
            expl.play()
            failm.play()
            ds.update()
            ds.reset()
            window.blit(lose, (265, 300))
            record = font2.render("SCORE:" + str(score), True, (255, 0, 0))
            liveslefttext = font2.render("LIVES LEFT:" + str(herolivesleft - lost), True, (0, 255, 0))
            window.blit(liveslefttext, (280, 450))  
            window.blit(record, (280, 400))  
            finish = True
        if sprite.collide_rect(hero, boss):
            liveslefttext = font2.render("LIVES LEFT:" + str(herolivesleft - lost), True, (0, 255, 0))
            record = font2.render("SCORE:" + str(score), True, (255, 0, 0))
            lost = 3
            mixer.music.stop()
            expl.play()
            failm.play( )
            ds.update()
            ds.reset()
            window.blit(liveslefttext, (280, 450))  
            window.blit(record, (280, 400))
            window.blit(lose, (265, 300)) 
            finish = True 
        if sprite.spritecollide(boss, bullets, True) or lost == 3:
            liveslefttext = font2.render("LIVES LEFT:" + str(herolivesleft - lost), True, (0, 255, 0))
            bosshp -= 500
            bosshpui = font2.render(str(bosshp), True, (255, 0, 0))
            expl.play()
            
        if bosshp <= 0:
            liveslefttext = font2.render("LIVES LEFT:" + str(herolivesleft - lost), True, (0, 255, 0))
            score = 20000
            record = font2.render("SCORE:" + str(score), True, (255, 0, 0))
            boss = Boss("kreyser.png", 9999, 9999, 0)
           

        
        if score >= 20000:
            mixer.music.stop()
            winm.play()
            ws.update()
            ws.reset()
            window.blit(win, (165, 300))
            window.blit(liveslefttext, (280, 450))  
            window.blit(record, (280, 400)) 
            finish = True

        if lost == 1:
            liveslefttext = font2.render("LIVES LEFT:" + str(herolivesleft - lost), True, (0, 255, 0))
            live1 =  Live("Battery.png", 0, 0)
            live2 =  Live("Battery.png", 50, 0) 
            live3 =  Live("Battery.png", 0, 0) 
        if lost == 2:
            live1 =  Live("Battery.png", 0, 0)
            live2 =  Live("Battery.png", 0, 0) 
            live3 =  Live("Battery.png", 0, 0) 
            liveslefttext = font2.render("LIVES LEFT:" + str(herolivesleft - lost), True, (0, 255, 0))
        #if score >= 13000:
            

 
 
  
    display.update()  
    clock.tick(FPS)