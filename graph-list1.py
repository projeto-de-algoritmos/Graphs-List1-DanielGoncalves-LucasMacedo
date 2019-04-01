import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BORDER_THICKNESS = 1.0

WIDTH = 600
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT)

POS_X_INIT = 0
POS_Y_INIT = 0

SIZE = 20

class NodeBorder():
    def __init__(self):
        self.color = WHITE
        self.thickness = BORDER_THICKNESS
        self.pos_x = 0.0
        self.pos_y = 0.0

    def render(self, pos_x, pos_y, width, height, background):
        self.pos_x = pos_x
        self.pos_y = pos_y

        pygame.draw.rect(background, self.color, [self.pos_x, self.pos_y, width, height])


class Node():
    def __init__(self):
        self.rect = None

        self.top_border = NodeBorder()
        self.bottom_border = NodeBorder()
        self.right_border = NodeBorder()
        self.left_border = NodeBorder()

        self.color = BLUE

        self.pos_x = 0.0
        self.pos_y = 0.0
        self.width = SIZE
        self.height = SIZE

        self.neighbors = []

    def render(self, pos_x, pos_y, background):
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.rect = pygame.draw.rect(background, self.color, [self.pos_x, self.pos_y, self.width, self.height])

        self.left_border.render(self.pos_x, self.pos_y, BORDER_THICKNESS, SIZE, background)
        self.right_border.render(self.pos_x + SIZE - BORDER_THICKNESS, self.pos_y, BORDER_THICKNESS, SIZE, background)
        self.top_border.render(self.pos_x, self.pos_y, SIZE, BORDER_THICKNESS, background)
        self.bottom_border.render(self.pos_x, self.pos_y + SIZE - BORDER_THICKNESS, SIZE, BORDER_THICKNESS, background)

class Maze():
    def __init__(self):
        self.maze = Node()
        #self.maze = [[0 for x in range(int(WIDTH / SIZE))] for y in range(int(HEIGHT / SIZE))]
    def render(self, background):
        for i in range(0, WIDTH, SIZE):
            for j in range(0, HEIGHT, SIZE):
                self.maze.render(i, j, background)
    # stack - pop push

class Player():
    def __init__(self):
        self.pos_x = POS_X_INIT + 1.0
        self.pos_y = POS_Y_INIT + 1.0
        self.width = SIZE - 2.0
        self.height = SIZE - 2.0
        self.color = RED 

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.pos_x > BORDER_THICKNESS:
                    self.pos_x -= SIZE
                if event.key == pygame.K_RIGHT and self.pos_x + BORDER_THICKNESS < WIDTH - SIZE:
                    self.pos_x += SIZE
                if event.key == pygame.K_UP and self.pos_y > BORDER_THICKNESS: 
                    self.pos_y -= SIZE
                if event.key == pygame.K_DOWN and self.pos_y + BORDER_THICKNESS < HEIGHT - SIZE:
                    self.pos_y += SIZE

    def render(self, background):
        pygame.draw.rect(background, self.color, [self.pos_x, self.pos_y, self.width, self.height])

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
        self.maze = Maze()
        self.player = Player()
        
                
    def unLoad(self):
        pass

    def update(self):
        self.player.update()

    def render(self):
        self.background.fill(BLACK)
        
        self.maze.render(self.background)

        self.player.render(self.background)
        pygame.display.update()

    def run(self):
        self.load()

        while not self.exit:
            if pygame.event.get(pygame.QUIT) or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self.exit = True

            self.update()
            self.render()
        
        pygame.quit()
        

if __name__ == '__main__':
    mygame = Game()
    mygame.run()
