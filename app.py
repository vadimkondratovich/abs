import pygame as pg
from play.colors import Color

timer = pg.time.Clock()
fps = 120

pg.init() #обязательное условие

game_screen = pg.display.set_mode(
    (800, 600), pg.OPENGL,
)
pg.display.set_caption("Snake")
game_screen.fill(Color.BLUE)
work = True
while work:
    keys = pg.key.get_pressed() #список нажатых кнопок
    work = not keys[pg.K_ESCAPE]
    timer.tick(fps)
    events = pg.event.get()
    for ev in events:
        print(ev) 
        if ev.type ==pg.WINDOWCLOSE:
            work = False

pg.quit()
