# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 12:37:00 2024

@author: chris
"""

#Initialize
import pygame

def main():
    pygame.init()
    
    #Display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Wish upon a shooting star and hoping it doesn't crash into the Earth.")
    
    #Entities
    #yellow background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((18, 22, 41))
    
    #put the cosmos in
    space = pygame.image.load("cosmos.PNG")
    space = space.convert_alpha()
    space = pygame.transform.scale(space, (640, 480))
    
    #make a red 25 x 25 box
    star = pygame.image.load("Wish.PNG")
    star = star.convert_alpha()
    star = pygame.transform.scale(star, (100, 100))
    
    # set up some box variables
    star_x = 0
    star_y = 200
    #ACTION
    
        #Assign
    clock = pygame.time.Clock()
    keepGoing = True
    
        #Loop
    while keepGoing:
    
        #Time
        clock.tick(30)
    
        #Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
    
        #modify box value
        star_x += 5
        star_y += 3
        #check boundaries
        if star_x > screen.get_width():
            star_x = 0
        if star_y > screen.get_height():
            star_y = 0
        #Refresh screen
        screen.blit(background, (0, 0))
        screen.blit(space, (0, 0))
        screen.blit(star, (star_x, star_y))
        #pygame.display.update
        pygame.display.flip()
    
    pygame.quit()
    
if __name__ == "__main__":
    main()