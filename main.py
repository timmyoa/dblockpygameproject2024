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
        self.rect.bottom=HEIGHT//2
        self.rect.left=WIDTH//2
    def update(self):
        self.rect.bottom+=10
def main():
    pg.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pg.display.set_mode(size)
    pg.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pg.time.Clock()

    # Create a snow sprites group
    player=Player()
    all_sp=pg.sprite.Group()
    all_sp.add(player)
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