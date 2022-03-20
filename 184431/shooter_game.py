#Создай собственный Шутер!
from random import *
from pygame import *
mixer.init()
#создай окно игры
window = display.set_mode((1600, 900))

display.set_caption('ШУТЕР')
win_width = 1600
win_height = 900
#задай фон сцены
background = transform.scale(image.load('6100860-t9iwxwum-v4.jpg'), (1600,900))
mixer.music.load('Steel Wool STUDIOS - FNAF Security Breach OST Fazer Blast Jam (Fazer Blast Theme).mp3')
mixer.music.play()
game = True
speed = 5
lost = 0
score = 0
max_lost = 10
goal = 30
health = 2
display.toggle_fullscreen() 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (50, 90))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y <= 0:
            self.kill
        
bullets = sprite.Group()

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, hp):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.hp = hp
    def fire(self):
        bull = Bullet('bullet.png', self.rect.centerx - 18, self.rect.top, 5)      
        bullets.add(bull)
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed              

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= win_height:
            self.rect.y = 0
            self.rect.x = randint(0, 1550)
        self.rect.y += self.speed

class Asteroid(GameSprite):
    def update(self):
        self.rect.y += 1
        if self.rect.y >= win_height:
            self.rect.y = 0
            self.rect.x = randint(0, 1550)
        self.rect.y += 1

run = True
finish = False
clock = time.Clock()
FPS = 144
player = Player('GregoryOPRender.png', 300, win_height - 80, 8, 3)
bonus1 = GameSprite('1614551882_2-p-kartinka-serdechko-na-belom-fone-4 (1).png', randint(80, win_height - 80), randint(80, win_width - 80), 0)
bonus2 = GameSprite('1614551882_2-p-kartinka-serdechko-na-belom-fone-4 (1).png', randint(80, win_height - 80), randint(80, win_width - 80), 0)
bonus3 = GameSprite('1614551882_2-p-kartinka-serdechko-na-belom-fone-4 (1).png', randint(80, win_height - 80), randint(80, win_width - 80), 0)
robot1 = Enemy('MapBot.png', randint(0, 660), 0, 2)
robot2 = Enemy('MapBot.png', randint(0, 660), 0, 2)
robot3 = Enemy('MapBot.png', randint(0, 660), 0, 2)
robot4 = Enemy('MapBot.png', randint(0, 660), 0, 2)
robot5 = Enemy('MapBot.png', randint(0, 660), 0, 2)
robot6 = Enemy('MapBot.png', randint(0, 660), 0, 2)
robot7 = Enemy('MapBot.png', randint(0, 660), 0, 2)
robot8 = Enemy('MapBot.png', randint(0, 660), 0, 2)
robot9 = Enemy('MapBot.png', randint(0, 660), 0, 2)
robot10 = Enemy('MapBot.png', randint(0, 660), 0, 2)
robot11 = Enemy('MapBot.png', randint(0, 660), 0, 2)
robot12 = Enemy('MapBot.png', randint(0, 660), 0, 2)
robot13 = Enemy('MapBot.png', randint(0, 660), 0, 2)
robot14 = Enemy('MapBot.png', randint(0, 660), 0, 2)
robot15 = Enemy('MapBot.png', randint(0, 660), 0, 2)
robot16 = Enemy('MapBot.png', randint(0, 660), 0, 2)
robot17 = Enemy('MapBot.png', randint(0, 660), 0, 2)
robot18 = Enemy('MapBot.png', randint(0, 660), 0, 2)
robot19 = Enemy('MapBot.png', randint(0, 660), 0, 2)
robot20 = Enemy('MapBot.png', randint(0, 660), 0, 2)

pizza1 = Asteroid('f996f95e7552376a13e3a643e5cd39ce.png', randint(0,660), 0, 2)
pizza2 = Asteroid('f996f95e7552376a13e3a643e5cd39ce.png', randint(0,660), 0, 2)
pizza3 = Asteroid('f996f95e7552376a13e3a643e5cd39ce.png', randint(0,660), 0, 2)
pizza4 = Asteroid('f996f95e7552376a13e3a643e5cd39ce.png', randint(0,660), 0, 2)
pizza5 = Asteroid('f996f95e7552376a13e3a643e5cd39ce.png', randint(0,660), 0, 2)
font.init()
font = font.Font(None, 70)
Asteroids = sprite.Group()
Asteroids.add(pizza1)
Asteroids.add(pizza2)
Asteroids.add(pizza3)
Asteroids.add(pizza4)
Asteroids.add(pizza5)
Asteroids.update()
monsters = sprite.Group()
monsters.add(robot1)
monsters.add(robot2)
monsters.add(robot3)
monsters.add(robot4)
monsters.add(robot5)
monsters.add(robot6)
monsters.add(robot7)
monsters.add(robot8)
monsters.add(robot9)
monsters.add(robot10)
monsters.add(robot11)
monsters.add(robot12)
monsters.add(robot13)
monsters.add(robot14)
monsters.add(robot15)
monsters.add(robot16)
monsters.add(robot17)
monsters.add(robot18)
monsters.add(robot19)
monsters.add(robot20)
monsters.update()
health = sprite.Group()
health.add(bonus1)
health.add(bonus2)
health.add(bonus3)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 
        elif e.type == KEYDOWN:
            if e.key == K_LCTRL:
                player.fire()    
    lose = font.render('YOU LOSE', 1, (255, 0, 0))
    win = font.render('YOU WIN!', 1, (0, 0, 255))
    if finish != True:
        window.blit(background,(0, 0))
        player.update()
        monsters.update()
        health.update()
        Asteroids.update()
        bullets.update()
        player.reset()
        health.draw(window)
        monsters.draw(window)
        bullets.draw(window)
        Asteroids.draw(window)
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score = score + 1
            robot1 = Enemy('MapBot.png', randint(0, 660), 0, 2)
            monsters.add(robot1)
        
        
        if sprite.spritecollide(player, monsters, True):
            player.hp -= 1
            robot1 = Enemy('MapBot.png', randint(0, 660), 0, 2)
            monsters.add(robot1)
        if player.hp <= 0 or lost >= max_lost:
            finish = True
            window.blit(lose, (600,450))
        
        if sprite.groupcollide(health, bullets, False, True):
            player.hp += 1 

        if sprite.spritecollide(player, Asteroids, True):
            player.hp -= 3
            pizza3 = Asteroid('f996f95e7552376a13e3a643e5cd39ce.png', randint(0,660), 0, 2)

        if score >= goal:   
            finish = True
            window.blit(win, (600, 450))
        text = font.render('Счет' + str(score), 1, (0, 255, 0))
        window.blit(text, (10, 20))
        
        text_hp = font.render('HP' + str(player.hp), 1, (255, 0, 0))
        window.blit(text_hp, (10, 70))
        display.update()
        clock.tick(FPS)