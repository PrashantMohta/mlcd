import mlcd,pygame     #import the module
mlcd.init(16,3) # initialize a 16x3 display
#draw the three lines passed as a list
while True:
    mlcd.draw(["Hello",         
               "     world",
               "Mock LCD !!!"])
    for event in pygame.event.get():
        pass

    

