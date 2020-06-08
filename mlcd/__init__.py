import pygame
def init(chars,lines,scalein):
    global screen
    global myfont
    global scale
    scale = scalein
    pygame.init()
    size = [12*chars*scale,20*lines*scale]
    screen= pygame.display.set_mode(size)
    pygame.display.set_caption("Mock LCD")
    myfont = pygame.font.SysFont("monospace", 20*scale)


def draw(args):
    i=0;
    global screen
    global myfont
    global scale
    screen.fill((0,0,0))#erase screen contents
    while(i<len(args)):
        line= myfont.render(args[i], 2*scale, (255,255,0))
        screen.blit(line, (0, 20*i*scale))
        i+=1
    pygame.display.flip()
        
