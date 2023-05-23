## CRAZY DRIVER ##

# Modules
import random
import pygame
pygame.init()

# Variables
score = 0
level = 0

road_speed = 12
speed = 10

# Display
infoObject = pygame.display.Info()
correction = 90
screen_height = infoObject.current_h-correction
screen_width = int(((infoObject.current_h-correction)*9)/16)

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("CRAZY DRIVER")

carwidth = int((60*screen_width)/((990*9)/16))
carheight = int((120*screen_height)/990)

t1 = int((55*screen_height)/990)
t2 = int((32*screen_height)/990)
t3 = int((22*screen_height)/990)
t4 = int((38*screen_height)/990)
t5 = int((42*screen_height)/990)

big_font = pygame.font.Font("texture/font.ttf", t1)
small_font = pygame.font.Font("texture/font.ttf",t2) #menus and score
credits_font = pygame.font.Font("texture/font.ttf",t3)
bonus_font = pygame.font.Font("texture/font.ttf",t4)
level_font = pygame.font.Font("texture/font.ttf",t5)

level_up_texts = ["FASTER !", "DRIFT !", "FULL SPEED !", "LET'S GOOOOOO !", "SPEED DOESN'T KILL !", "HELL YEAH !", "SPEED OF LIGHT !", "EASY !", "EASY PEASY LEMON SQUEEZY !", "TOO EASY !", "LEVEL UP !", "...", "CRAZY DRIVER !", "SPEED OF LIGHT !", "184 KM/H !", "OH !", "HEY !", "WELL DONE !", "YOU ARE THE BEST !", "SEBASTIEN LOEB ?", "KING OF THE ROAD!", "SUZUKI or CITROEN ?", "HELLO !", "NEXT LEVEL !", "!!!", "WHAT'S UP GUYS ?!", "ROCK'N'ROLL !", "TO THE SKYYYYYY !","3...2...1...GO !", "WELL PLAYED !", "YOU'RE SO SLOW !", "YEAH !", "ALL RIGHT !", "200 DEGREES", "DON'T STOP !", "OUT OF CONTROL !!", "VROUM !", "WTF ?!", "I <3 U !", "CHRICHRIIII !", "YANKEEEE !", "<3 CHRISTOPHE <3", "STAYING ALIVE !", "F*CK YOU !", "631 152 000"]

# Music
musics = ["music/3nuits.mp3","music/aventurier.mp3","music/banlieue.mp3","music/beegees.mp3","music/fcd.mp3","music/gimme.mp3","music/harley.mp3","music/hero.mp3","music/hurricane.mp3","music/idiot.mp3","music/kiss.mp3","music/lossofcontrol.mp3","music/popcorn.mp3","music/queen.mp3","music/renaud.mp3","music/sabotage.mp3","music/show.mp3","music/stop.mp3","music/survive.mp3","music/tiger.mp3"]

menu_musics = ["music/m_hurricane.mp3","music/m_idiot.mp3","music/m_kiss.mp3","music/m_sabotage.mp3"]

# Textures
bg = pygame.image.load("bg/bg.png").convert()
bg = pygame.transform.scale(bg, (screen_width, screen_height))

bg_credits = pygame.image.load("bg/bg_credits.png").convert()
bg_credits = pygame.transform.scale(bg_credits, (screen_width, screen_height))

bg_ds = pygame.image.load("bg/bg_ds.png").convert()
bg_ds = pygame.transform.scale(bg_ds, (screen_width, screen_height))

road = pygame.image.load("texture/road.png").convert()
road = pygame.transform.scale(road, (screen_width, int((screen_width*road.get_height())/road.get_width())))
roads=[i*road.get_height() for i in range(int(screen_height/road.get_height())+2)]

car = pygame.image.load('texture/red.png').convert_alpha()
car.set_colorkey((255,255,255))
car = pygame.transform.scale(car, (carwidth, carheight))

explo = pygame.image.load('texture/explosionn.png').convert_alpha()
explo = pygame.transform.scale(explo, (380, 400))
explo.set_colorkey((255,255,255))

green = pygame.image.load('texture/green.png').convert_alpha()
green.set_colorkey((255,255,255))
green = pygame.transform.scale(green, (carwidth, carheight))

blue = pygame.image.load('texture/blue.png').convert_alpha()
blue.set_colorkey((255,255,255))
blue = pygame.transform.scale(blue, (carwidth, carheight))

orange = pygame.image.load('texture/orange.png').convert_alpha()
orange.set_colorkey((255,255,255))
orange = pygame.transform.scale(orange, (carwidth, carheight))

yellow = pygame.image.load('texture/yellow.png').convert_alpha()
yellow.set_colorkey((255,255,255))
yellow = pygame.transform.scale(yellow, (carwidth, carheight))

grey = pygame.image.load('texture/grey.png').convert_alpha()
grey.set_colorkey((255,255,255))
grey = pygame.transform.scale(grey, (carwidth, carheight))

black = pygame.image.load('texture/black.png').convert_alpha()
black.set_colorkey((255,255,255))
black = pygame.transform.scale(black, (carwidth, carheight))

dblue = pygame.image.load('texture/dblue.png').convert_alpha()
dblue.set_colorkey((255,255,255))
dblue = pygame.transform.scale(dblue, (carwidth, carheight))

obs_color=[green,blue,orange,yellow,grey,black,dblue]

# a = pygame.image.load("bg/1.png").convert()
# a = pygame.transform.scale(a, (screen_width, screen_height))

# b = pygame.image.load("bg/2.png").convert()
# b = pygame.transform.scale(b, (screen_width, screen_height))

# c = pygame.image.load("bg/3.png").convert()
# c = pygame.transform.scale(c, (screen_width, screen_height))

# d = pygame.image.load("bg/4.png").convert()
# d = pygame.transform.scale(d, (screen_width, screen_height))

# e = pygame.image.load("bg/5.png").convert()
# e = pygame.transform.scale(e, (screen_width, screen_height))

# f = pygame.image.load("bg/6.png").convert()
# f = pygame.transform.scale(f, (screen_width, screen_height))

# g = pygame.image.load("bg/7.png").convert()
# g = pygame.transform.scale(g, (screen_width, screen_height))

# h = pygame.image.load("bg/8.png").convert()
# h = pygame.transform.scale(h, (screen_width, screen_height))

# i = pygame.image.load("bg/9.png").convert()
# i = pygame.transform.scale(i, (screen_width, screen_height))

# j = pygame.image.load("bg/10.png").convert()
# j = pygame.transform.scale(j, (screen_width, screen_height))

# k = pygame.image.load("bg/11.png").convert()
# k = pygame.transform.scale(k, (screen_width, screen_height))

# l = pygame.image.load("bg/12.png").convert()
# l = pygame.transform.scale(l, (screen_width, screen_height))

# m = pygame.image.load("bg/13.png").convert()
# m = pygame.transform.scale(m, (screen_width, screen_height))

# n = pygame.image.load("bg/14.png").convert()
# n = pygame.transform.scale(n, (screen_width, screen_height))

# o = pygame.image.load("bg/15.png").convert()
# o = pygame.transform.scale(o, (screen_width, screen_height))

# q = pygame.image.load("bg/16.png").convert()
# q = pygame.transform.scale(q, (screen_width, screen_height))

# r = pygame.image.load("bg/17.png").convert()
# r = pygame.transform.scale(r, (screen_width, screen_height))

# s = pygame.image.load("bg/18.png").convert()
# s = pygame.transform.scale(s, (screen_width, screen_height))

# t = pygame.image.load("bg/19.png").convert()
# t = pygame.transform.scale(t, (screen_width, screen_height))

# u = pygame.image.load("bg/20.png").convert()
# u = pygame.transform.scale(u, (screen_width, screen_height))

# v = pygame.image.load("bg/21.png").convert()
# v = pygame.transform.scale(v, (screen_width, screen_height))

# w = pygame.image.load("bg/22.png").convert()
# w = pygame.transform.scale(w, (screen_width, screen_height))

# x = pygame.image.load("bg/23.png").convert()
# x = pygame.transform.scale(x, (screen_width, screen_height))

# y = pygame.image.load("bg/24.png").convert()
# y = pygame.transform.scale(y, (screen_width, screen_height))

# z = pygame.image.load("bg/25.png").convert()
# z = pygame.transform.scale(z, (screen_width, screen_height))

# aa = pygame.image.load("bg/26.png").convert()
# aa = pygame.transform.scale(aa, (screen_width, screen_height))

# bb = pygame.image.load("bg/27.png").convert()
# bb = pygame.transform.scale(bb, (screen_width, screen_height))

# cc = pygame.image.load("bg/28.png").convert()
# cc = pygame.transform.scale(cc, (screen_width, screen_height))

# dd = pygame.image.load("bg/29.png").convert()
# dd = pygame.transform.scale(dd, (screen_width, screen_height))

# ee = pygame.image.load("bg/30.png").convert()
# ee = pygame.transform.scale(ee, (screen_width, screen_height))

# ff = pygame.image.load("bg/31.png").convert()
# ff = pygame.transform.scale(ff, (screen_width, screen_height))

# gg = pygame.image.load("bg/32.png").convert()
# gg = pygame.transform.scale(gg, (screen_width, screen_height))

# hh = pygame.image.load("bg/33.png").convert()
# hh = pygame.transform.scale(hh, (screen_width, screen_height))

# ii = pygame.image.load("bg/34.png").convert()
# ii = pygame.transform.scale(ii, (screen_width, screen_height))

# jj = pygame.image.load("bg/35.png").convert()
# jj = pygame.transform.scale(jj, (screen_width, screen_height))

# list_bg_bonus=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,q,r,s,t,u,v,w,x,y,z,aa,bb,cc,dd,ee,ff,gg,hh,ii,jj]

# Classes
class Car(object):

    def __init__(self, x, y, vel, color):
        self.x = x
        self.y = y
        self.width = carwidth
        self.height = carheight
        self.vel = vel
        self.color = color
        self.hitbox=(self.x, self.y, self.width, self.height)
        self.accounted=False

    def draw_(self,win):
        if self.__class__.__name__ == "Player":
            win.blit(car,(self.x,self.y))
            # self.hitbox=(self.x, self.y, self.width-1, self.height-1)
            # pygame.draw.rect(win,(255,0,0),self.hitbox,2)
        elif self.__class__.__name__ == "Obstacle":
            win.blit(obs_color[self.color],(self.x,self.y))
            # self.hitbox=(self.x, self.y, self.width-1, self.height-1)
            # pygame.draw.rect(win,(255,0,0),self.hitbox,2)

    def set_y(self,y):
        self.y = y

    def set_vel(self,v):
        self.vel = v

    def get_vel(self):
        return self.vel

class Player(Car):

    def mvt(self):
        klaxon = pygame.mixer.Sound("sound/klaxon.wav")
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and p.x>p.vel:
            p.x -= p.vel
        if keys[pygame.K_RIGHT] and p.x<screen_width-p.width-p.vel:
            p.x += p.vel
        if keys[pygame.K_SPACE]:
            klaxon.play()

class Obstacle(Car):

    def set_color(self):
        self.color = color_()

    def set_x(self):
        self.x = random.randint(0,screen_width-self.width)

    def is_accounted(self):
        self.accounted = True

    def not_accounted(self):
        self.accounted = False

    def mvt(self):
        global speed
        if self.y >= screen_height:
            self.set_x()
            self.set_y(-self.height)
            self.set_color()
            self.set_vel(speed)
            self.not_accounted()
        else:
            self.y += self.vel

class Explosion(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timer = 28

    def mvt(self):
        global speed
        self.timer -= 1
        if self.y < screen_height and self.timer > 0:
            self.y += speed
        else:
            explosions.pop(explosions.index(self))

    def draw_(self,win):
        global explo
        win.blit(explo,(self.x,self.y))

class Level_Text(object):

    def __init__(self, y, ind):
        self.y=y
        self.ind=ind
        self.timer=120

    def draw_(self,win):
        if self.timer>0:
            text_level=level_font.render(level_up_texts[self.ind], 1, (255,0,0))
            win.blit(text_level,(screen_width/2 - text_level.get_width()/2, self.y))
        if self.timer==0:
            level_up_text.pop(level_up_text.index(self))


p=Player((screen_width-carwidth)/2,screen_height-180,5,(255,0,0))
p.set_vel(5)

obstacles=[]

explosions=[]

level_up_text=[]

def color_():
    a=random.randint(0,len(obs_color)-1)
    return(a)

def explosion_(p,o):
    global explosions
    explosion_sound = pygame.mixer.Sound("sound/explosion.wav")
    if p.__class__.__name__=="Player":
        explosion_sound.play()
        x=(p.x+o.x)*0.5-explo.get_width()/2
        y=(max(p.y,o.y)+min(p.y+p.height,o.y+o.height))*0.5-explo.get_height()/2
        explosions.append(Explosion(x,y))
    else:
        explosion_sound.set_volume(0.25)
        explosion_sound.play()
        x=(p.x+o.x)*0.5-explo.get_width()/2
        y=(max(p.y,o.y)+min(p.y+p.height,o.y+o.height))*0.5-explo.get_height()/2
        explosions.append(Explosion(x,y))
        obstacles.pop(obstacles.index(p))
        obstacles.pop(obstacles.index(o))

def obstacle_collision(obstacle,obstacles):
    for o in obstacles:
        if obstacle!=o:
            if obstacle.x + obstacle.width >= o.x and obstacle.x <= o.x + o.width and obstacle.y + obstacle.height >= o.y and obstacle.y< o.y + o.height:
                if o.y==-obstacle.height:
                    o.set_x()
                else:
                    explosion_(obstacle,o)
                    obstacles.append(Obstacle(random.randint(0,screen_width-carwidth), -carheight, speed, color_()))
                    obstacles.append(Obstacle(random.randint(0,screen_width-carwidth), -8*carheight, speed, color_()))


def road_mvt():
    global roads,road_speed
    l=len(roads)
    for i in range(l):
        if roads[i]>screen_height:
            roads[i]=-road.get_height()
            win.blit(road,(0,roads[i]))
        else:
            roads[i]+=road_speed
            win.blit(road,(0,roads[i]))

def redrawGameWindow():
    global d,e
    road_mvt()
    p.draw_(win)
    for obstacle in obstacles:
        obstacle.draw_(win)
    for explosion in explosions:
        explosion.draw_(win)
    for text in level_up_text:
        text.draw_(win)
        text.timer-=1
    text_score=small_font.render("Score: "+str(score), 1, (255,0,0))
    # pygame.draw.rect(win,(0,0,0),(0,0,text_score.get_width()+4,text_score.get_height()+2))
    win.blit(text_score,(screen_width/2 - text_score.get_width()/2,2))

    pygame.display.update()

def credits():
    run=True
    while run:
        pygame.time.delay(100)

        mx,my=pygame.mouse.get_pos()
        click=False
        keys = pygame.key.get_pressed()

        win.blit(bg_credits, (0,0))

        correction=5
        menu_text=small_font.render("Main menu",1,(255,0,0))
        menu_button = pygame.Rect(screen_width/2 - menu_text.get_width()/2,screen_height - menu_text.get_height() - correction,menu_text.get_width(),menu_text.get_height())
        # pygame.draw.rect(win, (255,0,0), menu_button)
        win.blit(menu_text,(screen_width/2 - menu_text.get_width()/2,screen_height-menu_text.get_height()-correction))

        fg=(50+1.75*t1)
        gap=int(((screen_height-menu_text.get_height()-correction)-fg)/14)

        text1=big_font.render("CRAZY DRIVER !", 1, (255,0,0))
        win.blit(text1,(screen_width/2 - text1.get_width()/2, 50))

        text2=credits_font.render("Director: Fabien ALLEMAND", 1, (255,0,0))
        win.blit(text2,(screen_width/2 - text2.get_width()/2, fg))

        text3=credits_font.render("Producer: Fabien ALLEMAND", 1, (255,0,0))
        win.blit(text3,(screen_width/2 - text3.get_width()/2, fg+gap))

        text4=credits_font.render("Animation Director: Fabien ALLEMAND", 1, (255,0,0))
        win.blit(text4,(screen_width/2 - text4.get_width()/2, fg+2*gap))

        text5=credits_font.render("Level Design Director: Fabien ALLEMAND", 1, (255,0,0))
        win.blit(text5,(screen_width/2 - text5.get_width()/2, fg+3*gap))

        text6=credits_font.render("Gameplay Director: Fabien ALLEMAND", 1, (255,0,0))
        win.blit(text6,(screen_width/2 - text6.get_width()/2, fg+4*gap))

        text7=credits_font.render("Audio Director: Fabien ALLEMAND", 1, (255,0,0))
        win.blit(text7,(screen_width/2 - text7.get_width()/2, fg+5*gap))

        text8=credits_font.render("Programming Director: Fabien ALLEMAND", 1, (255,0,0))
        win.blit(text8,(screen_width/2 - text8.get_width()/2, fg+6*gap))

        text9=credits_font.render("Tester: Eva MESSEGUER, Clara VADEZ,", 1, (255,0,0))
        win.blit(text9,(screen_width/2 - text9.get_width()/2, fg+7*gap))

        text9_bis=credits_font.render("Quentin WENGER, Fabien ALLEMAND", 1, (255,0,0))
        win.blit(text9_bis,(screen_width/2 - text9_bis.get_width()/2, fg+8*gap))

        text10=credits_font.render("Special Thanks: Christophe VALENTIN", 1, (255,0,0))
        win.blit(text10,(screen_width/2 - text10.get_width()/2, fg+9*gap))

        text10=credits_font.render("for being such an amazing friend !!", 1, (255,0,0))
        win.blit(text10,(screen_width/2 - text10.get_width()/2, fg+10*gap))

        text11=credits_font.render("Project Started on 2021/05/06", 1, (255,0,0))
        win.blit(text11,(screen_width/2 - text11.get_width()/2, fg+11*gap))

        text12=credits_font.render("Project Ended on 2021/08/28", 1, (255,0,0))
        win.blit(text12,(screen_width/2 - text12.get_width()/2, fg+12*gap))

        text13=credits_font.render("Contact: allemand.fabien@orange.fr", 1, (255,0,0))
        win.blit(text13,(screen_width/2 - text13.get_width()/2, fg+13*gap))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if keys[pygame.K_ESCAPE]:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True
            if menu_button.collidepoint((mx,my)):
                if click:
                    mainMenu()

        pygame.display.update()
    pygame.quit()

# def bonus():

#     y=80
#     timer=10

#     bg_bonus=list_bg_bonus[random.randint(0,len(list_bg_bonus)-1)]
#     text1=bonus_font.render("JOYEUX ANNIVERSAIRE", 1, (255,0,0))
#     text2=bonus_font.render("CHRISTOPHE !!!", 1, (255,0,0))

#     run=True
#     while run:

#         mx,my=pygame.mouse.get_pos()
#         click=False
#         keys = pygame.key.get_pressed()

#         timer-=1

#         if timer>0:
#             win.blit(bg_bonus, (0,0))
#             win.blit(text1,(screen_width/2 - text1.get_width()/2, y))
#             win.blit(text2,(screen_width/2 - text2.get_width()/2, y+38))
#             pygame.time.delay(200)
#         else:
#             timer=10
#             y=random.randint(0,screen_height-120)
#             bg_bonus=list_bg_bonus[random.randint(0,len(list_bg_bonus)-1)]
#             win.blit(bg_bonus, (0,0))
#             win.blit(text1,(screen_width/2 - text1.get_width()/2, y))
#             win.blit(text2,(screen_width/2 - text2.get_width()/2, y+40))
#             pygame.time.delay(200)

#         correction=5
#         menu_text=small_font.render("Main menu",1,(255,0,0))
#         menu_button= pygame.Rect(screen_width/2 - menu_text.get_width()/2,screen_height - menu_text.get_height() - correction,menu_text.get_width(),menu_text.get_height())
#         pygame.draw.rect(win, (255,0,0), menu_button)
#         win.blit(menu_text,(screen_width/2 - menu_text.get_width()/2,screen_height-menu_text.get_height()-correction))

#         for event in pygame.event.get():
#             if event.type==pygame.QUIT:
#                 run=False
#             if keys[pygame.K_ESCAPE]:
#                 run=False
#             if event.type==pygame.MOUSEBUTTONDOWN:
#                 if event.button==1:
#                     click=True
#             if menu_button.collidepoint((mx,my)):
#                 if click:
#                     mainMenu()

#         pygame.display.update()
#     pygame.quit()

def mainMenu():

    b=random.randint(0,len(menu_musics)-1)
    music = pygame.mixer.music.load(menu_musics[b])
    pygame.mixer.music.play(-1)

    win.fill((0,0,0))
    run=True
    i=0
    while run:
        mx,my=pygame.mouse.get_pos()
        click=False
        keys = pygame.key.get_pressed()

        win.blit(bg, (0,0))

        text1=big_font.render("CRAZY DRIVER !", 1, (255,0,0))
        win.blit(text1,(screen_width/2 - text1.get_width()/2, 50))

        if i<100:
            i+=1
            text2=small_font.render("PRESS UP TO START RACING !", 1, (255,0,0))
            win.blit(text2,(screen_width/2 - text2.get_width()/2,120))
            pygame.time.delay(5)
        elif i<200:
            i+=1
            pygame.time.delay(5)
        else:
            i=0

        correction=5
        credits_text=small_font.render("Credits",1,(255,0,0))
        credits_button= pygame.Rect(screen_width/2 - credits_text.get_width()/2,screen_height - credits_text.get_height() - correction,credits_text.get_width(),credits_text.get_height())
        # pygame.draw.rect(win, (255,0,0), credits_button)
        win.blit(credits_text,(screen_width/2 - credits_text.get_width()/2,screen_height - credits_text.get_height() - correction))

        bonus_text=small_font.render("Bonus",1,(255,0,0))
        bonus_button=pygame.Rect(screen_width/2 - bonus_text.get_width()/2,screen_height - bonus_text.get_height() - 8*correction,bonus_text.get_width(),bonus_text.get_height())
        win.blit(bonus_text,(screen_width/2 - bonus_text.get_width()/2,screen_height - bonus_text.get_height() - 8*correction))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if keys[pygame.K_ESCAPE]:
                run=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True
            if keys[pygame.K_UP]:
                run=False
                start = pygame.mixer.Sound("sound/start.wav")
                start.play()
                mainLoop()
            if credits_button.collidepoint((mx,my)):
                if click:
                    credits()
            # if bonus_button.collidepoint((mx,my)):
            #     if click:
            #         bonus()
                    

        pygame.display.update()
    pygame.quit()

def deathScreen():
    pygame.time.delay(1000)
    run=True
    i=0
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            run=False
            mainMenu()
        if keys[pygame.K_UP]:
            run=False
            start = pygame.mixer.Sound("sound/start.wav")
            start.play()
            mainLoop()

        win.blit(bg_ds, (0,0))

        text1=big_font.render("GAME OVER !", 1, (255,0,0))
        win.blit(text1,(screen_width/2 - text1.get_width()/2, 50))

        textscore=big_font.render("Score: "+str(score), 1, (255,0,0))
        win.blit(textscore,(screen_width/2 - textscore.get_width()/2, 110))

        if i<100:
            i+=1
            text2=credits_font.render("PRESS UP TO TRY AGAIN", 1, (255,0,0))
            win.blit(text2,(screen_width/2 - text2.get_width()/2, 180))

            text3=credits_font.render("PRESS DOWN TO GO BACK TO MAIN MENU", 1, (255,0,0))
            win.blit(text3,(screen_width/2 - text3.get_width()/2, 220))
            pygame.time.delay(5)
        elif i<200:
            i+=1
            pygame.time.delay(5)
        else:
            i=0
        pygame.display.update()

def mainLoop():
    global score, speed, road, roads, road_speed, obstacles, explosions
    score=0
    speed=1
    roads=[i*road.get_height() for i in range(int(screen_height/road.get_height())+2)]
    road_speed=3
    obstacles=[]
    obstacles.append(Obstacle(random.randint(0,screen_width-carwidth), -carheight, speed, color_()))
    obstacles.append(Obstacle(random.randint(0,screen_width-carwidth), -4*carheight, speed, color_()))
    obstacles.append(Obstacle(random.randint(0,screen_width-carwidth), -8*carheight, speed, color_()))
    explosions=[]

    level=0
    level_score=[0.4*((i+1)**2) for i in range(1,100)]

    timer=80

    b=random.randint(0,len(musics)-1)
    c=b
    music = pygame.mixer.music.load(musics[b])
    pygame.mixer.music.play(-1)

    level_up = pygame.mixer.Sound("sound/level_up.wav")

    d=random.randint(0,len(level_up_texts)-1)
    e=d

    run = True
    crash = False
    while run and not crash:
        pygame.time.delay(int(100/6)-1)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        for obstacle in obstacles:
            obstacle_collision(obstacle,obstacles)
            if obstacle.x + obstacle.width >= p.x and obstacle.x <= p.x + p.width and obstacle.y + obstacle.height >= p.y and obstacle.y< p.y + p.height:
                crash = True
                explosion_(p,obstacle)
            else:
                obstacle.mvt()
                if obstacle.y>p.y+p.height and not obstacle.accounted:
                    obstacle.is_accounted()
                    score+=1
        for explosion in explosions:
            explosion.mvt()
        if score>=level_score[level]:
            level+=1
            if level%2==0:
                road_speed+=1
                speed=road_speed-2
                p.set_vel(p.get_vel()+0.2)
            else:
                obstacles.append(Obstacle(random.randint(0,screen_width-carwidth), -(2*speed)*carheight, speed, color_()))

            if level%4==0:
                level_up.play()
                b=random.randint(0,len(musics)-1)
                if b==c:
                    b=random.randint(0,len(musics)-1)
                    c=b
                else:
                    c=b
                music = pygame.mixer.music.load(musics[b])
                pygame.mixer.music.play(-1)

            if level%3==0:
                d=random.randint(0,len(level_up_texts)-1)
                if d==e:
                    d=random.randint(0,len(level_up_texts)-1)
                    e=d
                else:
                    e=d
                y_text=random.randint(35,screen_height-180)
                level_up_text.append(Level_Text(y_text,d))

        p.mvt()
        redrawGameWindow()

    while run and crash and timer>0:
        pygame.time.delay(int(100/6))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        timer-=1
        redrawGameWindow()
    deathScreen()
    pygame.quit()

mainMenu()