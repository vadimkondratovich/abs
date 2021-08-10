import pygame as pg
from pygame.mouse import set_visible
from arena import Arena, Direct

class Game(pg.Surface):
    def __init__(self):
        size = (800, 800)
        box_size = 10
        self.fps = 10
        pg.mouse,set_visible(False)
        self.win = pg.display.set_mode(size)
        pg.display.set_caption("SNAKE")
        super().__init__(size)
        self.work = True
        area = (
            size[0] // box_size,
            size[1] // box_size,
        )
        self.arena = Arena(size, self.box_size, area)
        self.timer = pg.time.Clock()
        self.direct = {
            pg.K_UP: Direct.UP,
            pg.K_RIGHT: Direct.RIGHT,
            pg.K_DOWN: Direct.DOWN,
            pg.K_LEFT: Direct.LEFT,
        }


    def _is_work(self):
        keys = pg.key.get_pressed()
        work = not keys[pg.K_ESCAPE]
        if not work:
            events = pg.event.get()
            for event in events:
                if event.type == pg.WINDOWCLOSE:
                    work = False
        return work or not self.arena.is_end

    def run(self):
        pg.display.flip()
        try:
            while self.work:
                self.update()
                self.timer.tick(self.fps)
                pg.display.flip()
                self.work = self._is_work()
        except KeyboardInterrupt:
            self.work = False

    def update(self):
        self.arena.update(self.get_direction())
        self.blit(self.arena, (0, 0))
        self.win.blit(self(0, 0))

    def get_direction(self):
        keys = pg.key.get_pressed()
        for k in self.direct:
            if keys[k]:
                return self.direct[k]
