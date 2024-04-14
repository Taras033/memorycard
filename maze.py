#создай игру "Лабиринт"!
from pygame import *
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')



win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Maze')
background = transform.scale(image.load('background.jpg'), (win_width, win_height))
clock = time.Clock()
FPS = 60
font.init()
font = font.SysFont('Arial', 70)
win1 = font.render('YOU WIN!', True, (255, 255, 255))
win2 = font.render('YOU LOSE!', True, (255, 0, 0))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
cyborg =  GameSprite('cyborg.png', 580, 280, 10)
treasure = GameSprite('treasure.png', 580, 380, 0)
class Player(GameSprite):
    def update(self):     
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= 10
        if keys_pressed[K_s] and self.rect.y < 395:
            self.rect.y += 10
        if keys_pressed[K_a] and self.rect.x < 595:
            self.rect.x += 10
        if keys_pressed[K_d] and self.rect.x > 5:
            self.rect.x -= 10
player =  Player('hero.png', 0, 0, 10)
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x >= 650:
            self.direction = 'left'
        if self.rect.x <= 475:
            self.direction = 'right'
        if self.direction == 'right':
            self.rect.x += self.speed
        if self.direction == 'left':
            self.rect.x -= self.speed
cyborg =  Enemy('cyborg.png', 580, 280, 5)
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
w1 = Wall(1, 1, 1, 150, 0, 20, 400)
w2 = Wall(1, 1, 1, 275, 200, 20, 400)
w3 = Wall(1, 1, 1, 375, 0, 20, 400)
w4 = Wall(1, 1, 1, 475, 100, 20, 400)


finish = False     
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        if sprite.collide_rect(player, cyborg) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4):
            finish = True
            kick.play()    
        window.blit(background,(0,0))
        keys_pressed = key.get_pressed()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        player.update()
        player.reset()
        cyborg.update()
        cyborg.reset()
        treasure.reset()
        if sprite.collide_rect(player, treasure):
            window.blit(win1, (200, 200))
            finish = True
            money.play()
        if sprite.collide_rect(player, cyborg) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4):
            window.blit(win2, (200, 200))
            finish = True
            kick.play()
    display.update()
    clock.tick(FPS) 

