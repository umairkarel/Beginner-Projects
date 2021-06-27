import pygame
pygame.font.init()
fnt = pygame.font.SysFont("comicsans", 60)

# Colors
blue = (0,0,255)

class Board:
    def __init__(self, width, height, screen):
        self.rows = 3
        self.cols = 3
        self.model = [[' ' for i in range(3)] for j in range(3)]
        #  [['X', 'Y', 'Z'], ['A', 'B', 'C'], ['E', 'F', 'G']]
        self.width = width
        self.height = height
        self.player = 'X'
        self.win_line_dim = []
        self.win = False
        self.screen = screen

    def draw(self):
        gap = self.width // 3
        text_pos = gap

        for i in range(1,3):
            pygame.draw.line(self.screen, (0,0,0), (0,i*gap), (self.width,i*gap), 1)
            pygame.draw.line(self.screen, (0,0,0), (i*gap,0), (i*gap,self.height), 1)

        for x in range(self.rows):
            for y in range(self.cols):
                text = fnt.render(str(self.model[x][y]), 1, (0, 0, 0))
                self.screen.blit(text, (y*gap + (gap/2 - text.get_width()/2), x*gap + (gap/2 - text.get_height()/2)))

        if self.win:
            self.draw_winline()

    def place(self, pos):
        self.player = 'X'

        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width // 3
            x = pos[1] // gap
            y = pos[0] // gap

            if self.model[x][y] != ' ':
                return False
            
            self.model[x][y] = self.player
            return True

        return False

    def check_win(self):
        if self.model[0][0] != ' ':
            if (self.model[0][0] == self.model[0][1] == self.model[0][2]):
                self.win_line_dim = [(0,0),(0,2)]
                self.win = True

            elif (self.model[0][0] == self.model[1][0] == self.model[2][0]):
                self.win_line_dim = [(0,0),(2,0)]
                self.win = True

        if self.model[1][1] != ' ':
            if (self.model[1][1] == self.model[1][0] == self.model[1][2]):
                self.win_line_dim = [(1,0), (1,2)]
                self.win = True

            elif (self.model[0][1] == self.model[1][1] == self.model[2][1]):
                self.win_line_dim = [(0,1), (2,1)]
                self.win = True

        if self.model[2][2] != ' ':
            if (self.model[2][2] == self.model[2][0] == self.model[2][1]):
                self.win_line_dim = [(2,0), (2,2)]
                self.win = True

            elif (self.model[0][2] == self.model[1][2] == self.model[2][2]):
                self.win_line_dim = [(0,2), (2,2)]
                self.win = True

        if self.model[0][0] and self.model[0][2]:
            if self.model[0][0] == self.model[1][1] == self.model[2][2] != ' ':
                self.win_line_dim = [(0,0), (2,2)]
                self.win = True
            elif self.model[0][2] == self.model[1][1] == self.model[2][0] != ' ':
                self.win_line_dim = [(0,2), (2,0)]
                self.win = True

        if self.win:
            return self.player
        
        return False

    def draw_winline(self):
        gap = self.width // 3
        x1,y1 = self.win_line_dim[0]
        x2,y2 = self.win_line_dim[1]
        offset = 40

        if x1 == x2:
            y1 = x1*gap + gap//2 - 4
            x1 = offset
            x2 = self.width - x1
            y2 = y1
        elif y1 == y2:
            x1 = y1*gap + gap//2 - 1
            y1 = offset
            y2 = self.height - y1
            x2 = x1
        else:
            x1 = y1*self.width//2 + (-offset if y1 else offset)
            y1 = offset
            x2 = (self.width-offset) if x1 == offset else offset
            y2 = self.height - offset

        pygame.draw.line(self.screen, blue, (x1,y1), (x2,y2), 8)

    def computer_move(self):
        self.player = 'O'

        for i in range(3):
            for j in range(3):
                if self.model[i][j] == ' ':
                    self.model[i][j] = 'O'

                    if self.check_win():
                        return 
                    self.model[i][j] = ' '

        for i in range(3):
            for j in range(3):
                if self.model[i][j] == ' ':
                    self.model[i][j] = 'X'

                    if self.check_win():
                        self.model[i][j] = 'O'
                        self.win = False
                        return 
                    self.model[i][j] = ' '

        for i in range(3):
            for j in range(3):
                if self.model[i][j] == ' ':
                    self.model[i][j] = 'O'
                    return

    def reset(self):
        self.model = [[' ' for i in range(3)] for j in range(3)]
        self.player = 'X'
        self.win = False