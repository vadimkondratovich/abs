import pygame
import sys

W = 350
H = 280

sc = pygame.display.set_mode((W, H))


WHITE = (255, 255, 255)
BLUE = (0, 0, 225)
RED = (225, 0, 50)
clock = pygame.time.Clock()


class Surf():
    one = pygame.draw.rect(sc, WHITE, (20, 20, 100, 75))
    two = pygame.draw.rect(sc, WHITE, (125, 20, 100, 75))
    three = pygame.draw.rect(sc, WHITE, (230, 20, 100, 75))
    four = pygame.draw.rect(sc, WHITE, (20, 100, 100, 75))
    five = pygame.draw.rect(sc, WHITE, (125, 100, 100, 75))
    six = pygame.draw.rect(sc, WHITE, (230, 100, 100, 75))
    seven = pygame.draw.rect(sc, WHITE, (20, 180, 100, 75))
    eight = pygame.draw.rect(sc, WHITE, (125, 180, 100, 75))
    nine = pygame.draw.rect(sc, WHITE, (230, 180, 100, 75))


pygame.display.update()


class Cross():
    cross1 = pygame.draw.lines(sc, RED, False,
                [[20, 20], [120, 95], 
                [120, 20], [20, 95]])
    cross2 = pygame.draw.lines(sc, RED, False,
                [[125,20], [225, 95], 
                [225, 20], [125, 95]])
    cross3 = pygame.draw.lines(sc, RED, False,
                [[230, 20], [330, 95], 
                [330, 20], [230, 95]])   
    cross4 = pygame.draw.lines(sc, RED, False,
                [[20, 100], [120, 175], 
                [120, 100], [20, 175]]) 
    cross5 = pygame.draw.lines(sc, RED, False,
                [[125, 100], [225, 175], 
                [225, 100], [125, 175]])
    cross6 = pygame.draw.lines(sc, RED, False,
                [[230, 100], [330, 175], 
                [330, 100], [230, 175]])
    cross7 = pygame.draw.lines(sc, RED, False,
                [[20, 180], [120, 255], 
                [120, 180], [20, 255]])
    cross8 = pygame.draw.lines(sc, RED, False,
                [[125, 180], [225, 255], 
                [225, 180], [125, 255]]) 
    cross9 =  pygame.draw.lines(sc, RED, False,
                [[230, 180], [330, 255], 
                [330, 180], [230, 255]])
pygame.display.update()              

class Zero():
    zero1 = pygame.draw.circle(sc, BLUE, 
                   (70, 57), 35, 2)
    zero2 = pygame.draw.circle(sc, BLUE, 
                   (175, 57), 35, 2)             
    zero3 = pygame.draw.circle(sc, BLUE, 
                   (280, 57), 35, 2)
    zero4 = pygame.draw.circle(sc, BLUE, 
                   (70, 137), 35, 2)
    zero5 = pygame.draw.circle(sc, BLUE, 
                   (175, 137), 35, 2)
    zero6 = pygame.draw.circle(sc, BLUE, 
                   (280, 137), 35, 2)
    zero7 = pygame.draw.circle(sc, BLUE, 
                   (70, 217), 35, 2)
    zero8 = pygame.draw.circle(sc, BLUE, 
                   (175, 217), 35, 2)
    zero9 = pygame.draw.circle(sc, BLUE, 
                   (280, 217), 35, 2)
pygame.display.update()


while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                
                
                pygame.display.update()
            elif i.button == 3:
                
                pygame.display.update()
            elif i.button == 2:
                pass
                pygame.display.update()
    pygame.display.update()

   
    clock.tick(60)

if __name__ == "__main()__":
    main()

