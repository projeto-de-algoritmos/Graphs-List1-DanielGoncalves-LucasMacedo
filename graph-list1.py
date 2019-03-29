import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 810
HEIGHT = 810

SIZE = 15



class Player():



    for event in pygame.event.get():
        if event.type == pygame.QUIT: # altf4 ou x
            sair = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pos_x -= SIZE
            if event.key == pygame.K_RIGHT:
                pos_x += SIZE
            if event.key == pygame.K_UP: 
                pos_y -= SIZE
            if event.key == pygame.K_DOWN:
                pos_y += SIZE

class Game():
    def load(self):
        try:
            pygame.init()
        except:
            print("The pygame module did not start successfully")

        background = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption("Maze")
        
    def unLoad(self):
        
    def update(self):
    
    def render(self):

    def run(self):

        while exit:
           python.display.update()

        python.quit()

    
if __name__ == '__main__':
    Game()