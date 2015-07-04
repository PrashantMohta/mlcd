import pygame
def init(chars,lines):
    global screen
    global myfont
    pygame.init()
    size = [12*chars,20*lines]
    screen= pygame.display.set_mode(size)
    pygame.display.set_caption("Mock LCD")
    myfont = pygame.font.SysFont("monospace", 20)


def draw(args):
    i=0;
    global screen
    global myfont
    screen.fill((0,0,0))#erase screen contents
    while(i<len(args)):
        line= myfont.render(args[i], 2, (255,255,0))
        screen.blit(line, (0, 20*i))
        i+=1
    pygame.display.flip()
        
