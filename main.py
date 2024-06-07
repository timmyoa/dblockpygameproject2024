import random
import pygame as pg


# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
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
IIMAGE=pg.image.load("Images/boost.png")
IIMAGE=pg.transform.scale(#the method
    IIMAGE,
    (IIMAGE.get_width()//5, IIMAGE.get_height()//5) #boost object image
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

class items(pg.sprite.Sprite):
    def __init__(self,frame_spawm,spawn_loc):#frame-based spawn, spawn_loc decide where item comes from
        super().__init__()
        self.image=IIMAGE
        self.rect=self.image.get_rect()
        if spawn_loc==1:#spawm top left corner
            self.rect.centerx=-20
            self.rect.centery=-20
        if spawn_loc==2:#spawm bottom right corner
            self.rect.centerx=1300
            self.rect.centery=740

    def update():
        pass

def main():
    pg.init()
    pg.mouse.set_visible(False)
    num_fly=5 #number of inital flying obect on screen
    counter_fly=0 #flys on screen counted
    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pg.display.set_mode(size)
    pg.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pg.time.Clock()

    # Create a sprites group with player on it
    player=Player()
    all_sp=pg.sprite.Group()
    all_sp.add(player)
    #create flying objects and put them in all_sp and a new sprite group: fly_sp
    fly_sp=pg.sprite.Group
    for i in range(num_fly): # create flying objects
        flying=Flying_ob()
        all_sp.add(flying)
        fly_sp.add(flying)
        counter_fly+=1#counter of flying object
    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        # ----- LOGIC
        all_sp.update()

        # ----- RENDER
        screen.fill(BLACK)



        # ----- UPDATE DISPLAY
        all_sp.draw(screen)
        pg.display.flip()
        clock.tick(60)

    pg.quit()



if __name__ == "__main__":
    main()