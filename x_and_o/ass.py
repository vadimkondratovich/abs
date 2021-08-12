import pygame as pg
import sys
 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (225, 0, 50)
BLUE = (0, 0, 225)


sc = pg.display.set_mode((1000, 800))
surf = pg.Surface((100, 75))
surf.fill((255, 255, 255))

 
# сначала на главной поверхности
# рисуется зеленый прямоуг
surf = (
sc.blit(surf, (20, 20)),
sc.blit(surf, (125, 20)),
sc.blit(surf, (230, 20)),
sc.blit(surf, (20, 100)),
sc.blit(surf, (125, 100)),
sc.blit(surf, (230, 100)),
sc.blit(surf, (20, 180)),
sc.blit(surf, (125, 180)),
sc.blit(surf, (230, 180)),
)


pg.display.update()
 
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                pg.draw.lines(sc, RED, False, [[20, 20], [120, 95], [120, 20], [20, 95]])
                pg.draw.lines(sc, RED, False, [[125,20], [225, 95], [225, 20], [125, 95]])
                pg.draw.lines(sc, RED, False,[[230, 20], [330, 95], [330, 20], [230, 95]])   
                pg.draw.lines(sc, RED, False,[[20, 100], [120, 175], [120, 100], [20, 175]]) 
                pg.draw.lines(sc, RED, False,[[125, 100], [225, 175], [225, 100], [125, 175]])
                pg.draw.lines(sc, RED, False,[[230, 100], [330, 175], [330, 100], [230, 175]])
                pg.draw.lines(sc, RED, False,[[20, 180], [120, 255], [120, 180], [20, 255]])
                pg.draw.lines(sc, RED, False,[[125, 180], [225, 255], [225, 180], [125, 255]]) 
                pg.draw.lines(sc, RED, False,[[230, 180], [330, 255], [330, 180], [230, 255]])
                pg.display.update()

            elif i.button == 3:
                pg.draw.circle(sc, BLUE, (70, 57), 35, 2)
                pg.draw.circle(sc, BLUE, (175, 57), 35, 2)             
                pg.draw.circle(sc, BLUE, (280, 57), 35, 2)
                pg.draw.circle(sc, BLUE, (70, 137), 35, 2)
                pg.draw.circle(sc, BLUE, (175, 137), 35, 2)
                pg.draw.circle(sc, BLUE, (280, 137), 35, 2)
                pg.draw.circle(sc, BLUE, (70, 217), 35, 2)
                pg.draw.circle(sc, BLUE, (175, 217), 35, 2)
                pg.draw.circle(sc, BLUE, (280, 217), 35, 2)
                pg.display.update()
            elif i.button == 2:
                pass
                pg.display.update()
            
    pg.time.delay(100)
 

