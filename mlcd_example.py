import mlcd     #import the module
mlcd.init(16,3) # initialize a 16x3 display
#draw the three lines passed as a list
mlcd.draw(["Hello",         
           "     world",
           "Mock LCD !!!"])

