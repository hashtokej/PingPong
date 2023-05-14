from pygame import *
'''Необходимые классы'''

#класс-родитель для спрайтов 
class GameSprite(sprite.Sprite):
    #конструктор класса
       #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height): # добавить еще два параметра при создании и задавать размер прямоугольгника для картинки самим
        super().__init__()
 
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (wight, height)) # вместе 55,55 - параметры
        self.speed = player_speed
 
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс-наследник для спрайта-игрока (управляется стрелками)
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


#Игровая сцена:
back = (200, 255, 255) # цвет фона (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

#флаги отвечающие за состояние игры
game = True
finish = False
clock = time.Clock()
FPS = 60

#создания мяча и ракетки    
racket1 = Player('racket.png', 30, 200, 4, 50, 150) # при созданни спрайта добавляется еще два параметра
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

speed_x = 3
speed_y = 3

font.init()
font1 = font.Font(None, 35)
lose1 =  font1.render(
    'ты гриб 1', True, (180, 0, 0))

font2 = font.Font(None, 35)
lose2 =  font2.render(
    'ты гриб 2', True, (180, 0, 0))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if ball.rect.y > win_height-40 \
                or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(racket1, ball) \
                or sprite.collide_rect(racket2, ball):
                speed_x *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))

            if ball.rect.y < 0:
                finish = True
                window.blit(lose2, (400, 400))

        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        
        racket1.draw()
        racket2.draw()
        ball.draw()

    display.update()
    clock.tick(FPS)