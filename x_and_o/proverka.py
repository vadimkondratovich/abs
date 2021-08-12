import pygame as pg
import sys
 

W = 300
H = 200


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)


sc = pg.display.set_mode((300, 200))

pg.draw.rect(sc, (255, 255, 255), 
                 (20, 20, 100, 75))
pg.draw.rect(sc, (64, 128, 255), 
                 (150, 20, 100, 75), 8)


pg.draw.circle(sc, YELLOW, 
                   (100, 100), 50)
pg.draw.circle(sc, PINK, 
                   (200, 100), 50, 10)



pg.display.update()



while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
    pg.display.update()

   
    pg.time.delay(100)

if __name__ == "__main()__":
    main()
