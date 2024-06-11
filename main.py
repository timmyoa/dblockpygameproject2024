import random
import time
import pygame as pg
from pygame import mixer 


# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE=(0,0,255)
SKY_BLUE = (95, 165, 228)
GREEN = (0, 255, 0)
WIDTH = 1280
HEIGHT = 720
TITLE = "THE 'GAME' :O"
TIMAGE= pg.image.load("./Images/swatter.png")
TIMAGE=pg.transform.scale(#the method
    TIMAGE,
    (TIMAGE.get_width()//2, TIMAGE.get_height()//2) #player image
)
FIMAGE=pg.image.load("Images/fly1.png")
FIMAGE=pg.transform.scale(#the method
    FIMAGE,
    (FIMAGE.get_width()//25, FIMAGE.get_height()//25) #"flying" object image
)

KIMAGE=pg.image.load("Images/pizza.webp")
KIMAGE=pg.transform.scale(#the method
    KIMAGE,
    (KIMAGE.get_width()//1, KIMAGE.get_height()//0.5) #boost object image
)

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=TIMAGE
        self.rect=self.image.get_rect()
        #start at center
        self.rect.bottom=HEIGHT//2
        self.rect.left=WIDTH//2
    def update(self):
        #movement by following the mouse
        self.rect.centerx=pg.mouse.get_pos()[0]
        self.rect.centery=pg.mouse.get_pos()[1]

class Flying_ob(pg.sprite.Sprite):#sprite of fly
    def __init__(self):
        super().__init__()
        self.image = FIMAGE
        self.rect= self.image.get_rect()
        # new properity: velocity of the dvd logo
        self.vel_x=random.randrange(20,50)
        self.vel_y=random.randrange(20,50)#starting speed and direction
        self.rect.centerx = random.randrange(100,1100)
        self.rect.centery = random.randrange(100,620)
    def update(self):
        self.rect.x+=self.vel_x
        self.rect.y+=self.vel_y
        #bounce if reach edge, applies a random speed in a random direction
        if self.rect.bottom > 720:
            self.vel_y=random.randrange(20,50)
            self.vel_y *= -1
            self.vel_x=random.randrange(-50,50)
        elif self.rect.top <0:
            self.vel_y=random.randrange(-50,-20)
            self.vel_y *=-1
            self.vel_x=random.randrange(-50,50)
        if self.rect.right>1280:
            self.vel_x=random.randrange(20,50)
            self.vel_y=random.randrange(-50,50)
            self.vel_x*=-1
        elif self.rect.left<0:
            self.vel_x=random.randrange(-50,-20)
            self.vel_y=random.randrange(-50,50)
            self.vel_x*=-1



def main():
    pg.init()
    pg.mouse.set_visible(False)
    num_fly=5 #number of inital flying obect on screen
    counter_fly=0 #flys on screen counted
    # ----- SCREEN PROPERTIES
    asd=0 # var to see if it is first run or not
    size = (WIDTH, HEIGHT)
    screen = pg.display.set_mode(size)
    pg.display.set_caption(TITLE)
    font=pg.font.SysFont("Papyrus",24)# font for score
    font1=pg.font.SysFont("Papyrus",33)#font for beginning phrase
    mixer.init() #music
    mixer.music.load("./sound/jazz.mp3")
    mixer.music.play() #play the music


    # ----- LOCAL VARIABLES
    insctuct=font1.render(f"Press space to play, hit as many flies as possible in 1 minutes, try to get a high score", True, BLUE)#starting phrase
    bg = KIMAGE#pizza background
    timer=0#timer for main feature run time
    music_timer=0# timer to to detect music run time
    score=0
    done = False
    clock = pg.time.Clock()

    # Create a sprites group with player on it
    player=Player()
    all_sp=pg.sprite.Group()
    all_sp.add(player)
    #create flying objects and put them in all_sp and a new sprite group: fly_sp
    fly_sp=pg.sprite.Group()
    for i in range(num_fly): # create flying objects
        flying=Flying_ob()
        all_sp.add(flying)
        fly_sp.add(flying)
        counter_fly+=1#counter of flying object
    # ----- MAIN LOOP
    wait=1
    while not done:
        # -- Event Handler
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        while wait==1:# starting phrase
            if asd==1:
                screen.blit(hisc,(20,20))
            screen.fill(BLACK)
            screen.blit(bg,(0,0))
            screen.blit(insctuct, (100,350))
            pg.display.flip()
            all_sp.draw(screen)
            if music_timer>=5460:
                mixer.music.play()
            music_timer=0
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                if event.type == pg.KEYDOWN:
                    if event.key==pg.K_SPACE:
                        wait=0

        
        # ----- LOGIC
        timer+=1
        all_sp.update()
        if event.type == pg.MOUSEBUTTONDOWN:
            fly_collide = pg.sprite.spritecollide(player, fly_sp, True) 
            for flying in fly_collide:
                counter_fly-=1#delete counter by one when a fly is gone
                score+=1
        while counter_fly!=5:
            flying=Flying_ob()
            all_sp.add(flying)
            fly_sp.add(flying)
            counter_fly+=1#counter of flying object, add until there is 5 
        music_timer+=1
        if music_timer>=5460:#use frames to count time, 1 sec increase by 60, when reach 1:31 min 
            #replay music and reset timer tp 0
            mixer.music.play()
            music_timer=0



        # ----- RENDER
        screen.fill(BLACK)
        screen.blit(bg,(0,0))
        



        # ----- UPDATE DISPLAY
        all_sp.draw(screen)
        score_image=font.render(f"Score: {score}", True, GREEN)
        screen.blit(score_image, (5,5))
        pg.display.flip()
        clock.tick(60)
        if timer>=7200:# turn to starting phrase when time reach two minutes, time is cacultaed by frames
            hisc=font1.render(f"Final Score: {score}", True, GREEN)
            asd=1
            wait=1
            timer=0
            score=0
        print(timer,asd,wait)

    pg.quit()



if __name__ == "__main__":
    main()