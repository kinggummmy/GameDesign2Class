import pygame

DIS_WIDTH = 1280
DIS_HEIGHT = 720

FLOOR = 600
SPAWN_X = 700

SKY = (135,206,235)

#The two lists are used to keep track of enemies and obstacles that are present in the current frame of the game
enemiesSpawned = []
obstaclesSpawned = []

class Obstacle:
    def __init__(self, size, screen, loc):
        self.size = size
        self.color = (131,131,131)
        self.screen = screen
        self.loc = loc
        self.velocity = [-5,0]
        
        obstaclesSpawned.append(self) #When an obstacle object is created it is added to the list of obstacles
        
        self.obsRect = pygame.Rect(loc, (size,size))
        pygame.draw.rect(self.screen, self.color, self.obsRect)
        
    def move(self):
        self.obsRect.move_ip(self.velocity)
        
    def update(self):
        pygame.draw.rect(self.screen, self.color, self.obsRect)
        
    def checkCollision(self, player): #check if the obstacle calling the method collides with a Player object
        if self.obsRect.colliderect(player.charRect):
            return player.lose() #Return false if there is a collision in order to exit the main loop
        return True


class Character:
    def __init__(self, size, screen, loc, color):
        self.size = size
        self.screen = screen
        self.loc = loc
        self.color = color
        self.velocity = [0,0]
        
        self.charRect = pygame.Rect(loc, (size,size))
        pygame.draw.rect(self.screen, self.color, self.charRect)
        
    def lose(self):
        print("Character lose(): Wrong lose()")
        return False
    
    def interact(self, hazard):
        print("Character interact(): Wrong interact()")
        return False
    
    def move(self, change):
        print("Character move(): Wrong move()")
        return False
    
    def update(self):
        pygame.draw.rect(self.screen, self.color, self.charRect)
        
        
    
class Player(Character):
    
    def __init__(self, size, screen, loc):
        self.color = (0,255,0)
        super().__init__(size, screen, loc, self.color)
        self.velocity = [0,0] #Change velocity as necessary
        
    def interact(self, hazard):
        for enemy in enemiesSpawned:
            if self.charRect.collidepoint(enemy.charRect):
                self.lose()
                break
        for obs in obstaclesSpawned:
            if self.charRect.collidepoint(obs.obsRect):
                self.lose()
                break
            
    def move(self, change):
        self.velocity[1] = -change
        self.loc[1] += -change
        self.charRect.move_ip(self.velocity[0], self.velocity[1])
        
    
    def lose(self):
        self.screen.fill((255,0,0))
        return False
    
