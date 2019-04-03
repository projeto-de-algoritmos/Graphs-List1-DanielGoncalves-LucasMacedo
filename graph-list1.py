import sys
import pygame
import random
import time

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGRAY = (169, 169, 169)
YELLOW = (222, 178, 0)
PINK = (225, 96, 253)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
ORANGE = (255, 99, 71)
GRAY = (119, 136, 153)
LIGHTORANGE = (255, 176, 56)
INTERMEDIARYORANGE = (255, 154, 0) 
LIGHTBLUE = (60, 170, 255)
DARKBLUE = (0, 101, 178)
BEIGE = (178, 168, 152)

BORDER_THICKNESS = 1.0

HEIGHT_TOTAL = 680
WIDTH = 600
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT_TOTAL)

FONTSIZE_START = 50
FONTSIZE_COMMANDS_INTIAL = 25
FONTSIZE_MAZE = 20

SIZE = 25

CLOCK = pygame.time.Clock()

def text(background, message, color, size, coordinate_x, coordinate_y):
    font = pygame.font.SysFont("comicsansms", size)
    text = font.render(message, True, color)
    background.blit(text, [coordinate_x, coordinate_y])

class NodeBorder():
    def __init__(self, pos_x, pos_y, width, height):
        self.color = BLACK
        self.thickness = BORDER_THICKNESS
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height

    def render(self, background):
        pygame.draw.rect(background, self.color, [self.pos_x, self.pos_y, self.width, self.height])


class Node():
    def __init__(self, pos_x, pos_y):
        self.color = DARKGRAY

        self.visited = False
        self.explored = False

        self.matrix_pos_x = 0
        self.matrix_pos_y = 0

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = SIZE
        self.height = SIZE

        self.top_border = NodeBorder(self.pos_x, self.pos_y, SIZE, BORDER_THICKNESS)
        self.bottom_border = NodeBorder(self.pos_x, self.pos_y + SIZE - BORDER_THICKNESS, SIZE, BORDER_THICKNESS)
        self.right_border = NodeBorder(self.pos_x + SIZE - BORDER_THICKNESS, self.pos_y, BORDER_THICKNESS, SIZE)
        self.left_border = NodeBorder(self.pos_x, self.pos_y, BORDER_THICKNESS, SIZE)

        self.neighbors = []
        self.neighbors_connected = []
        self.parent = None

    def render(self, background):
        pygame.draw.rect(background, self.color, [self.pos_x, self.pos_y, self.width, self.height])

        self.top_border.render(background)
        self.bottom_border.render(background)
        self.right_border.render(background)
        self.left_border.render(background)

class Maze():
    def __init__(self, background, initial_x, initial_y, final_x, final_y):
        self.maze = []
        self.total_nodes = 0
        self.maze_created = False
        self.initial_coordinate_x = initial_x
        self.initial_coordinate_y = initial_y
        self.final_coordinate_x = final_x
        self.final_coordinate_y = final_y

        x = 0
        y = 0
        for i in range(0, WIDTH, SIZE):
            self.maze.append([])
            for j in range(0, HEIGHT, SIZE):
                self.maze[x].append(Node(i , j))
                self.total_nodes += 1
                y += 1
            x += 1

        self.define_neighbors()

    def add_edge(self, node, neighbor):
        neighbor.neighbors_connected.append(node)
        node.neighbors_connected.append(neighbor)

    def remove_neighbors_visited(self, node):
        node.neighbors = [x for x in node.neighbors if not x.visited]
 
    def define_neighbors(self):
        for i in range(0, int(HEIGHT / SIZE)):
            for j in range(0, int(WIDTH / SIZE)):
                self.maze[i][j].matrix_pos_x = i
                self.maze[i][j].matrix_pos_y = j
                if i > 0 and j > 0 and i < int(HEIGHT / SIZE) - 1 and j < int(HEIGHT / SIZE) - 1:
                    self.maze[i][j].neighbors.append(self.maze[i + 1][j]) # bot
                    self.maze[i][j].neighbors.append(self.maze[i - 1][j]) # top
                    self.maze[i][j].neighbors.append(self.maze[i][j + 1]) # right
                    self.maze[i][j].neighbors.append(self.maze[i][j - 1]) # left
                elif i == 0 and j == 0:
                    self.maze[i][j].neighbors.append(self.maze[i][j + 1]) # right
                    self.maze[i][j].neighbors.append(self.maze[i + 1][j]) # bot
                elif i == int(HEIGHT / SIZE) - 1 and j == 0:
                    self.maze[i][j].neighbors.append(self.maze[i - 1][j]) # top
                    self.maze[i][j].neighbors.append(self.maze[i][j + 1]) # right
                elif i == 0 and j == int(WIDTH / SIZE) - 1:
                    self.maze[i][j].neighbors.append(self.maze[i][j - 1]) # left
                    self.maze[i][j].neighbors.append(self.maze[i + 1][j]) # bot
                elif i == int(HEIGHT / SIZE) - 1 and j == int(WIDTH / SIZE) - 1:
                    self.maze[i][j].neighbors.append(self.maze[i][j - 1]) # left
                    self.maze[i][j].neighbors.append(self.maze[i - 1][j]) # top
                elif j == 0:
                    self.maze[i][j].neighbors.append(self.maze[i - 1][j]) # top
                    self.maze[i][j].neighbors.append(self.maze[i][j + 1]) # right
                    self.maze[i][j].neighbors.append(self.maze[i + 1][j]) # bot
                elif i == 0:
                    self.maze[i][j].neighbors.append(self.maze[i + 1][j]) # bot
                    self.maze[i][j].neighbors.append(self.maze[i][j + 1]) # right
                    self.maze[i][j].neighbors.append(self.maze[i][j - 1]) # left
                elif i == int(HEIGHT / SIZE) - 1:
                    self.maze[i][j].neighbors.append(self.maze[i - 1][j]) # top
                    self.maze[i][j].neighbors.append(self.maze[i][j + 1]) # right
                    self.maze[i][j].neighbors.append(self.maze[i][j - 1]) # left
                elif j == int(WIDTH / SIZE) - 1:
                    self.maze[i][j].neighbors.append(self.maze[i + 1][j]) # bot
                    self.maze[i][j].neighbors.append(self.maze[i - 1][j]) # top
                    self.maze[i][j].neighbors.append(self.maze[i][j - 1]) # left

    def break_border(self, node, neightbor, color):
        # right
        if (neightbor.matrix_pos_x == node.matrix_pos_x + 1) and (neightbor.matrix_pos_y == node.matrix_pos_y):
            node.right_border.color = color
            neightbor.left_border.color = color
        # left
        elif (neightbor.matrix_pos_x == node.matrix_pos_x - 1) and (neightbor.matrix_pos_y == node.matrix_pos_y):
            node.left_border.color = color
            neightbor.right_border.color = color
        # bot
        elif (neightbor.matrix_pos_x == node.matrix_pos_x) and (neightbor.matrix_pos_y == node.matrix_pos_y + 1):
            node.bottom_border.color = color
            neightbor.top_border.color = color
        # top
        elif (neightbor.matrix_pos_x == node.matrix_pos_x) and (neightbor.matrix_pos_y == node.matrix_pos_y - 1):
            node.top_border.color = color
            neightbor.bottom_border.color = color
    
    def dfs(self, background):
        current_cell = random.choice(random.choice(self.maze))
        current_cell.visited = True
        current_cell.color = GREEN
        stack = [current_cell]
        visited_cells = 1
        
        while visited_cells != self.total_nodes or len(stack) != 0:
            self.remove_neighbors_visited(current_cell)
            if len(current_cell.neighbors) > 0:
                random_neighbor = random.choice(current_cell.neighbors)

                self.break_border(current_cell, random_neighbor, GREEN)

                self.add_edge(current_cell, random_neighbor)
                current_cell = random_neighbor
                stack.append(current_cell)
                current_cell.visited = True
                current_cell.color = GREEN
                visited_cells += 1
            else:
                current_cell.color = YELLOW

                if current_cell.top_border.color == GREEN:
                    current_cell.top_border.color = YELLOW
                if current_cell.bottom_border.color == GREEN:
                    current_cell.bottom_border.color = YELLOW
                if current_cell.right_border.color == GREEN:
                    current_cell.right_border.color = YELLOW
                if current_cell.left_border.color == GREEN:
                    current_cell.left_border.color = YELLOW
                    
                if len(stack) == 1:
                    stack.pop()
                else:
                    stack.pop()
                    current_cell = stack[-1]
            self.render(background)
            text(background, "GENERATING MAZE", WHITE, FONTSIZE_COMMANDS_INTIAL, 215, 620)
            pygame.display.update()
        self.maze_created = True
    
    def bfs(self, background, player):
        initial_node = self.maze[player.matrix_pos_x][player.matrix_pos_y]
        initial_node.explored = True
        find = False
        queue = [initial_node]
        while len(queue) > 0 and not find:
            queue[0].color = PINK

            if queue[0].top_border.color == YELLOW:
                queue[0].top_border.color = PINK
            if queue[0].bottom_border.color == YELLOW:
                queue[0].bottom_border.color = PINK
            if queue[0].right_border.color == YELLOW:
                queue[0].right_border.color = PINK
            if queue[0].left_border.color == YELLOW:
                queue[0].left_border.color = PINK

            u = queue.pop(0)
            for i in u.neighbors_connected:
                if i.explored == False:
                    i.parent = u
                    i.explored = True
                    queue.append(i)
                    if i.matrix_pos_x == self.final_coordinate_x and i.matrix_pos_y == self.final_coordinate_y:
                        find = True
            self.render(background)
            text(background, "SOLVING MAZE", WHITE, FONTSIZE_COMMANDS_INTIAL, 218, 620)
            player.render(background)
            pygame.display.update()
        
        current = self.maze[self.final_coordinate_x][self.final_coordinate_y]
        while (current.parent).parent != None:
            current = current.parent
            current.color = ORANGE

            if current.top_border.color == PINK:
                current.top_border.color = ORANGE
            if current.bottom_border.color == PINK:
                current.bottom_border.color = ORANGE
            if current.right_border.color == PINK:
                current.right_border.color = ORANGE
            if current.left_border.color == PINK:
                current.left_border.color = ORANGE

            self.render(background)
            player.render(background)
            pygame.display.update()
    
    def render(self, background):
        for i in range(0, int(HEIGHT / SIZE)):
            for j in range(0, int(WIDTH / SIZE)):
                self.maze[i][j].render(background)
        if self.maze_created:
            self.maze[self.initial_coordinate_x][self.initial_coordinate_y].color = BROWN
            self.maze[self.final_coordinate_x][self.final_coordinate_y].color = BLUE

class Player():
    def __init__(self, initial_x, initial_y):
        self.pos_x = initial_x * SIZE + BORDER_THICKNESS
        self.pos_y = initial_y * SIZE + BORDER_THICKNESS
        self.matrix_pos_x = initial_x
        self.matrix_pos_y = initial_y
        self.width = SIZE - 2 * BORDER_THICKNESS
        self.height = SIZE - 2 * BORDER_THICKNESS
        self.color = RED

    def update(self, maze, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.pos_x > BORDER_THICKNESS and (maze[self.matrix_pos_x][self.matrix_pos_y].left_border.color != BLACK):
                    self.pos_x -= SIZE
                    self.matrix_pos_x -= 1
                if event.key == pygame.K_RIGHT and self.pos_x + BORDER_THICKNESS < WIDTH - SIZE and (maze[self.matrix_pos_x][self.matrix_pos_y].right_border.color != BLACK):
                    self.pos_x += SIZE
                    self.matrix_pos_x += 1
                if event.key == pygame.K_UP and self.pos_y > BORDER_THICKNESS and (maze[self.matrix_pos_x][self.matrix_pos_y].top_border.color != BLACK): 
                    self.pos_y -= SIZE
                    self.matrix_pos_y -= 1
                if event.key == pygame.K_DOWN and self.pos_y + BORDER_THICKNESS < HEIGHT - SIZE and (maze[self.matrix_pos_x][self.matrix_pos_y].bottom_border.color != BLACK):
                    self.pos_y += SIZE
                    self.matrix_pos_y += 1

    def render(self, background):
        pygame.draw.rect(background, self.color, [self.pos_x, self.pos_y, self.width, self.height])

class Game():
    def __init__(self):
        try:
            pygame.init()
        except:
            print('The pygame module did not start successfully')

        self.initial_coordinate_x = 0
        self.initial_coordinate_y = 0
        self.final_coordinate_x = 0
        self.final_coordinate_y = 0
        self.start = False
        self.solved = False
        self.winner = False
        self.exit = False

    def load(self):
        self.background = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('Maze Game')
        self.initial_coordinate_x = random.randint(0, int(HEIGHT / SIZE) - 1)
        self.initial_coordinate_y = random.randint(0, int(WIDTH / SIZE) - 1)
        self.final_coordinate_x = random.randint(0, int(HEIGHT / SIZE) - 1)
        self.final_coordinate_y = random.randint(0, int(WIDTH / SIZE) - 1)
        while self.final_coordinate_x == self.initial_coordinate_x or self.final_coordinate_y == self.initial_coordinate_y:
            self.final_coordinate_x = random.randint(0, int(HEIGHT / SIZE) - 1)
            self.final_coordinate_y = random.randint(0, int(WIDTH / SIZE) - 1)
        self.maze = Maze(self.background, self.initial_coordinate_x, self.initial_coordinate_y, self.final_coordinate_x, self.final_coordinate_y)
        self.player = Player(self.initial_coordinate_x, self.initial_coordinate_y)

    def update(self, event):
        if not self.solved and not self.winner:
            self.player.update(self.maze.maze, event)
        if self.player.matrix_pos_x == self.final_coordinate_x and self.player.matrix_pos_y == self.final_coordinate_y:
            self.winner = True

    def initial_game(self):
        self.background.fill(DARKBLUE)
        pygame.draw.rect(self.background, BEIGE, [40, 40, 530, 580])
        pygame.draw.rect(self.background, LIGHTBLUE, [40, 100, 530, 450])
        pygame.draw.rect(self.background, BLACK, [110, 150, 380, 350])
        pygame.draw.rect(self.background, DARKBLUE, [110, 150, 380, 100])
        text(self.background, "MAZE ADVENTURES", LIGHTORANGE, FONTSIZE_START, 125, 185)
        text(self.background, "PRESS (ESC) TO CLOSE GAME", INTERMEDIARYORANGE, FONTSIZE_COMMANDS_INTIAL + 5, 150, 375)
        pygame.display.update()
        pygame.time.wait(180)
        text(self.background, "PRESS (S) TO START GAME", INTERMEDIARYORANGE, FONTSIZE_COMMANDS_INTIAL + 5, 160, 350)
        pygame.display.update()
        pygame.time.wait(180)

    def end_of_game(self):
        self.maze.bfs(self.background, self.player)

    def render(self):
        self.background.fill(BLACK)
        
        self.maze.render(self.background)

        self.player.render(self.background)

        if not self.solved and not self.winner:
            text(self.background, "PRESS (R) TO RETRY GAME", WHITE, FONTSIZE_MAZE, 220, 610)
            text(self.background, "PRESS (Q) TO GIVE UP", WHITE, FONTSIZE_MAZE, 226, 630)
            text(self.background, "PRESS (ESC) TO CLOSE GAME", WHITE, FONTSIZE_MAZE, 212, 650)
        elif self.winner:
            text(self.background, "YOU WIN", WHITE, FONTSIZE_MAZE + 3, 255, 610)
            text(self.background, "PRESS (R) TO RETRY GAME", WHITE, FONTSIZE_MAZE, 215, 630)
            text(self.background, "PRESS (ESC) TO CLOSE GAME", WHITE, FONTSIZE_MAZE, 210, 650)
        else:
            text(self.background, "YOU LOSE", WHITE, FONTSIZE_MAZE + 3, 255, 610)
            text(self.background, "PRESS (R) TO RETRY GAME", WHITE, FONTSIZE_MAZE, 215, 630)
            text(self.background, "PRESS (ESC) TO CLOSE GAME", WHITE, FONTSIZE_MAZE, 210, 650)

        pygame.display.update()

    def run(self):
        self.load()
        while not self.start:
            self.initial_game()
            pygame.display.update()
            if pygame.event.get(pygame.QUIT) or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit(0)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                    self.start = True
        pygame.display.update()

        self.background.fill(BLACK)
        self.maze.dfs(self.background)

        while not self.exit:
            if pygame.event.get(pygame.QUIT) or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self.exit = True
            e = pygame.event.get()
            if self.winner:
                self.background.fill(BLACK)
            for event in e:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.solved = False
                        self.winner = False
                        self.run()
                    if not self.solved and event.key == pygame.K_q and not self.winner:
                        self.background.fill(BLACK)
                        self.end_of_game()
                        self.solved = True
            self.update(e)
            self.render()

        pygame.quit()
        sys.exit(0)
        
def main():
    mygame = Game()
    mygame.run()

if __name__ == '__main__':
    main()