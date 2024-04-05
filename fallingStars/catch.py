# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:31:23 2024

@author: chris
"""
import pygame, random, simpleGE

#The boxes
class Cage(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("border.png")
        self.setSize(600, 350)
        self.position = (320, 235)

class ScoreBox(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("textBox.png")
        self.setSize(475, 70)
        self.position = (320, 50)

class PlayBox(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("textBox.png")
        self.setSize(200, 60)
        self.position = (100, 450)

class QuitBox(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("textBox.png")
        self.setSize(200, 60)
        self.position = (540, 450)

#text boxes for the game
class GameScore(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("textBox.png")
        self.setSize(200, 60)
        self.position = (100, 30)

class TimeBox(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("textBox.png")
        self.setSize(200, 60)
        self.position = (500, 30)

#The things falling from the sky
class Wish(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("wishyStar.png")
        self.setSize(50, 50)
        self.reset()
    
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(3, 8)
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

class Comet(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("comet.png")
        self.setSize(50, 50)
        self.reset()
    
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(12, 14)
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

class Entropy(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("entropy.png")
        self.setSize(75, 75)
        self.reset()
    
    def reset(self):
        self.y = 10
        self.x = random.randint(0, self.screenWidth)
        self.dy = random.randint(2, 4)
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()

#The lil guy you move
class Bunny(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        #self.images = {
            #"left": self.setImage("seaBunny.png"),
            #"right": self.setImage("rightBunny.png")}
        #self.copyImage(self.images["right"])
        #self.setSize(100, 100)
        #self.images_x = 320
        #self.images_y = 430
        
        
        self.setImage("seaBunny.png")   
        self.setSize(100, 100)
        self.position = (320, 430)
        self.moveSpeed = 7
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
            #self.copyImage(self.images["left"])
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed
            #self.copyImage(self.images["right"])

class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.clearBack = True
        self.fgColor = "white"
        self.text = "Score: 0"
        self.center = (100, 30)

class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.clearBack = True
        self.fgColor = "white"
        self.text = "Time Left: 10"
        self.center = (500, 30)

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.background.fill((18, 22, 41))
        self.setImage("night.PNG")
        
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.score = 0
        
        numEntropy = 3
        numWish = 12
        numTimeUp = 2
        
        self.gameScore = GameScore(self)
        self.timeBox = TimeBox(self)
        
        
        self.bunny = Bunny(self)
        self.wishes = []
        for i in range(numWish):
            self.wishes.append(Wish(self))
        
        self.comets = []
        for i in range(numTimeUp):
            self.comets.append(Comet(self))
        
        self.voids = []
        for i in range(numEntropy):
            self.voids.append(Entropy(self))
        
        self.lblScore = LblScore()
        self.lblTime = LblTime()
        
        
        self.sprites = [self.bunny, self.wishes, self.comets, self.voids, self.gameScore, self.timeBox, self.lblScore, self.lblTime]
    
    def process(self):
        for wish in self.wishes:
            if self.bunny.collidesWith(wish):
                wish.reset()
                self.score += 1
                self.lblScore.text = f"Score: {self.score}"

        for comet in self.comets:
            if self.bunny.collidesWith(comet):
                comet.reset()
                self.score += 1
                self.timer.totalTime += 1
                self.lblScore.text = f"Score: {self.score}"
        
        for void in self.voids:
            if self.bunny.collidesWith(void):
                void.reset()
                self.score -= 1
                self.timer.totalTime -= 2
                self.lblScore.text = f"Score: {self.score}"
                
        self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() <= 0:
            print(f"final Score: {self.score}")
            self.stop()



class Instructions(simpleGE.Scene):
    def __init__(self, score = 0):
        super().__init__()
        self.setImage("night.PNG")
        
        self.status = "quit"
        self.score = score
        
        self.cage = Cage(self)
        self.playBG = PlayBox(self)
        self.quitBG = QuitBox(self)
        self.scoreBox = ScoreBox(self)
        
        self.Instructions = simpleGE.MultiLabel()
        self.Instructions.clearBack = True
        self.Instructions.fgColor = "black"
        self.Instructions.textLines = [
            "Collect the falling stars",
            "Attain the comets for more time",
            "Dodge the voids or you lose your limited time",
            "Now, bring about endless miracles."
            ]
        
        self.Instructions.center = (320, 240)
        self.Instructions.size = (450, 200)
        
        self.lblScore = simpleGE.Label()
        self.lblScore.clearBack = True
        self.lblScore.fgColor = "white"
        self.lblScore.center = (320, 50)
        self.lblScore.size = (400, 30)
        self.lblScore.text = f"Previous Stars Collected: {self.score}"
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.clearBack = True
        self.btnPlay.fgColor = "white"
        self.btnPlay.center = (100, 450)
        self.btnPlay.text = "Play (up)"
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.clearBack = True
        self.btnQuit.fgColor = "white"
        self.btnQuit.center = (540, 450)
        self.btnQuit.text = "Quit (down)"
        
        self.sprites = [self.scoreBox, self.cage, self.playBG, self.quitBG, self.lblScore, self.Instructions, self.btnPlay, self.btnQuit]
        
        
    def process(self):
        if self.btnPlay.clicked:
            self.status = "play"
            self.stop()
        if self.btnQuit.clicked:
            self.status = "quit"
            self.stop()
            
        if self.isKeyPressed(pygame.K_UP):
            self.status = "play"
            self.stop()
        if self.isKeyPressed(pygame.K_DOWN):
            self.status = "quit"
            self.stop()
            
def main():
    pygame.display.set_caption("Collect the falling stars and make these ethereal wishes a reality.")

    
    keepGoing = True
    score = 0
    while keepGoing:
        instructions = Instructions(score)
        instructions.start()
        
        if instructions.status == "play":
            game = Game()
            game.start()
            score = game.score
        else:
            keepGoing = False

if __name__ == "__main__":
    main()