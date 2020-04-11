# this is a failed attempt at a gui with pygame

import pygame

pygame.init()
width, height = 800,  600
backgroundColor = 65,  0,  27
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont("DejaVu Sans Mono",20)
textcolour = 255,  255,  255
boottext = ["Found memory (256mb)","Found OS","Finsihed loading OS","Starting BitOS 1.0","----------------------------------------","Welcome to BitOS! FOr help on how to operate the device please","read the documents included with your hardware or type the","command 'help'for a list of usefull commands","","","root@bitminer:~$"]
while True:
  screen.fill(backgroundColor)
  texty = 5
  for x in range(len(boottext)):
    text = font.render(boottext[x],1,textcolour)
    screen.blit(text,(10,texty))
    texty += 25
  pygame.display.flip()
