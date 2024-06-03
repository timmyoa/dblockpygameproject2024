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
num_fly=0
TIMAGE= pg.image.load("./Images/Mario.png")
TIMAGE=pg.transform.scale(#the method
    TIMAGE,
    (TIMAGE.get_width()//2, TIMAGE.get_height()//2)
)

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pg.image.load("./Images/Mario.png")
        self.rect=self.image.get_rect()
        #start at center
        self.rect.bottom=HEIGHT//2
        self.rect.left=WIDTH//2
    def update(self):
        #movement by following the mouse
        self.rect.centerx=pg.mouse.get_pos()[0]
        self.rect.centery=pg.mouse.get_pos()[1]

class Flying_ob(pg.sprite.Sprite):
    pass


def main():
    pg.init()

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
    for i in range():
        flying=fly_sp
        all_sp.add(flying)
        fly_sp.add(flying)
        num_fly+=1
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