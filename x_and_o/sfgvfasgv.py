import pygame
import sys

W = 350
H = 280

sc = pygame.display.set_mode((W, H))


WHITE = (255, 255, 255)
BLUE = (0, 0, 225)
RED = (225, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0) 
clock = pygame.time.Clock()



one = pygame.draw.rect(sc, WHITE, (20, 20, 100, 75))
two = pygame.draw.rect(sc, WHITE, (125, 20, 100, 75))
three = pygame.draw.rect(sc, WHITE, (230, 20, 100, 75))
four = pygame.draw.rect(sc, WHITE, (20, 100, 100, 75))
five = pygame.draw.rect(sc, WHITE, (125, 100, 100, 75))
six = pygame.draw.rect(sc, WHITE, (230, 100, 100, 75))
seven = pygame.draw.rect(sc, WHITE, (20, 180, 100, 75))
eight = pygame.draw.rect(sc, WHITE, (125, 180, 100, 75))
nine = pygame.draw.rect(sc, WHITE, (230, 180, 100, 75))

# sc.blit(one, (50, 20))
pygame.display.update()


while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                pygame.draw.lines(sc, RED, False,
                [[230, 180], [330, 255], 
                [330, 180], [230, 255]])
                
                pygame.display.update()
            elif i.button == 3:
                zero1 = pygame.draw.circle(sc, BLUE, 
                   (70, 57), 35, 2)


                pygame.display.update()
            elif i.button == 2:
                pass
                pygame.display.update()
    pygame.display.update()

   
    clock.tick(60)

if __name__ == "__main()__":
    main()

