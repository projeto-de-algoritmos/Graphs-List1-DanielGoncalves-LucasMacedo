import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 900
HEIGHT = 900
SCREEN_SIZE = (WIDTH, HEIGHT)

POS_X_INIT = 0
POS_Y_INIT = 0

SIZE = 20

class Node():
    pass

class Maze():
    pass

class Player():
    def __init__(self):
        self.pos_x = POS_X_INIT 
        self.pos_y = POS_Y_INIT
        self.h = SIZE
        self.w = SIZE
        self.color = RED 

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.pos_x > 0:
                    self.pos_x -= SIZE
                if event.key == pygame.K_RIGHT and self.pos_x < WIDTH - SIZE:
                    self.pos_x += SIZE
                if event.key == pygame.K_UP and self.pos_y > 0: 
                    self.pos_y -= SIZE
                if event.key == pygame.K_DOWN and self.pos_y < HEIGHT - SIZE:
                    self.pos_y += SIZE

    def render(self, background):
        pygame.draw.rect(background, self.color, [self.pos_x, self.pos_y, self.w, self.h])


class Game():
    def __init__(self):
        try:
            pygame.init()
        except:
            print('The pygame module did not start successfully')

        self.exit = False

    def load(self):
        self.background = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('Maze')

        self.player = Player()
        
                
    def unLoad(self):
        pass

    def update(self):
        self.player.update()

    def render(self):
        self.background.fill(BLACK)
        self.player.render(self.background)
        pygame.display.update()

    def run(self):
        self.load()

        while not self.exit:
            if pygame.event.get(pygame.QUIT):
                self.exit = True

            self.update()
            self.render()
        
        pygame.quit()
        

if __name__ == '__main__':
    mygame = Game()
    mygame.run()
