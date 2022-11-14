import pygame
import random

GREEN_DOT = 1

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)


game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Item")
clock = pygame.time.Clock()


class Thing:
    def __init__(self, color):
        self.color = color
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(0, HEIGHT)
        self.size = random.randrange(8, 16)
        
def draw_environment(thing):
    game_display.fill(WHITE)
    pygame.draw.circle(game_display, thing.color, [thing.x, thing.y], thing.size)
    pygame.display.update()
    
    

def move(self):
    self.move_x = random.randrange(-1, 2)
    self.move_y = random.randrange(-1, 2)
    self.x += self.move_x
    self.y += self.move_y
        
    if self.x < 0:
        self.x = 0
    elif self.x > WIDTH:
        self.x = WIDTH
            
    if self.y < 0:
        self.y = 0
    elif self.y > HEIGHT:
        self.y = HEIGHT      
        
def main():
    green_thing = Thing(GREEN)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        draw_environment(green_thing)
        clock.tick(60)
        
        
        
if __name__ == '__main__':
    main()