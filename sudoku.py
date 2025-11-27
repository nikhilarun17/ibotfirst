fh=[[3, 0, 6, 5, 0, 8, 4, 0, 0],[5, 2, 0, 0, 0, 0, 0, 0, 0],[0, 8, 7, 0, 0, 0, 0, 3, 1],[0, 0, 3, 0, 1, 0, 0, 8, 0],[9, 0, 0, 8, 6, 3, 0, 0, 5],[0, 5, 0, 0, 9, 0, 6, 0, 0], [1, 3, 0, 0, 0, 0, 2, 5, 0],[0, 0, 0, 0, 0, 0, 0, 7, 4],[0, 0, 5, 2, 0, 6, 3, 0, 0]]
import pygame
import pickle
from sys import exit
pygame.init()
sudoku_list=[]

print(sudoku_list)
edit_mode=False
font_=pygame.font.Font(None,50)
font_Amatic=pygame.font.Font("amatic/Amatic-Bold.ttf",150)

def check(grid,row,col,number):
    for i in range(9):
        if grid[row][i]==number:
            return False
    for i in range(9):
        if grid[i][col]==number:
            return False
    for i in range(3*(row//3),3*(row//3)+3):
        for j in range(3*(col//3),3*(col//3)+3):
            if grid[i][j]==number:
                return False
    return True
def next_spot(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                return i,j
    else:
        return None,None
def solve(grid):
    row,col=next_spot(grid)
    if row is None:
        return True
    for i in range(1,10):
        if check(grid,row,col,i):
            grid[row][col]=i
            (temp_list[row][col]).update_display(zero_elimintor(i))
            pygame.display.update()
            if solve(grid):
                return True
            grid[row][col]=0
    grid=[[0 for i in range(9)] for j in range(9)]
l=[[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6], [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]]
Box_width=50
Spx=150
Spy=300

class Button():
    def __init__(self,text,font,size,rect,color="black"):
        self.font=pygame.font.Font(font,size)
        self.color=color
        self.text=text
        self.safe=True
        self.font_text=self.font.render(self.text,True,self.color)
        self.text_rect=self.font_text.get_rect(center=rect)
        screen.blit(self.font_text,self.text_rect)
        pygame.draw.rect(screen,"black",self.text_rect.inflate(20,20),6,1)
    def button_update(self):
        self.safe=not self.safe
        self.color=(0,0,[0,255][0 if self.safe else 1])
        self.font_text=self.font.render(self.text,True,self.color)
        screen.blit(self.font_text,self.text_rect)

class dipla():
    def __init__(self,x,y):
        self.rect=pygame.Rect(x,y,Box_width,Box_width)
        self.rect2=pygame.Rect(x-17,y-10,Box_width,Box_width)
        self.safe=True
    def update_display(self,text,colour=0):
        self.colour=colour
        self.font=font_.render(text,True,"Black")
        screen.blit(colour_list[colour],(self.rect[0]-17,self.rect[1]-10))
        screen.blit(self.font,self.rect)
        grid_()

temp_list=[[i for i in range(9)] for j in range(9)]

def zero_elimintor(x):
    return "" if x==0 else str(x)
def grid_():
    for i in range(-1,9):
        width = 5 if (i+1)%3>0 else 10
        pygame.draw.line(screen,"Black",pygame.Vector2(Spx+Box_width*i,Spy),pygame.Vector2(Spx+Box_width*i,Spy+Box_width*9),width)
        pygame.draw.line(screen,"Black",pygame.Vector2(Spx-Box_width,Spy+Box_width*(i+1)),pygame.Vector2(Spx+Box_width*8,Spy+Box_width+Box_width*i),width)
def disp():
    for i in range(9):
        for j in range(9):
            rect=dipla(Spx+Box_width*(i-1)+17,Spy+Box_width*(j)+10)
            temp_list[i][j]=rect
            temp_list[i][j].update_display(zero_elimintor(fh[i][j]))

clock=pygame.time.Clock()
screen=pygame.display.set_mode((1200,1000))
surface_1=pygame.Surface((1200,1000))
surface_1.fill("White")
surface_2=pygame.Surface((Box_width,Box_width))
surface_2.fill("White")
surface_3=pygame.Surface((Box_width,Box_width))
surface_3.fill("Green")
colour_list=[surface_2,surface_3]
title_text=font_Amatic.render("Sudoku Solver",True,"Black")
screen.blit(surface_1,(0,0))
screen.blit(title_text,title_text.get_rect(center=(600,100)))
button_1=Button("Edit Mode","great-vibes/GreatVibes-Regular.otf",45,(900,400))
button_2=Button("Solve","great-vibes/GreatVibes-Regular.otf",45,(900,500))
button_3=Button("Load","great-vibes/GreatVibes-Regular.otf",45,(900,600))
disp()


while True:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        if button_1.text_rect.collidepoint(pygame.mouse.get_pos()) and event.type==pygame.MOUSEBUTTONDOWN:
            button_1.button_update()
        if button_2.text_rect.collidepoint(pygame.mouse.get_pos()) and event.type==pygame.MOUSEBUTTONDOWN and button_1.safe:
            button_2.button_update()
        if button_3.text_rect.collidepoint(pygame.mouse.get_pos()) and button_1.safe and pygame.MOUSEBUTTONDOWN:
            button_3.button_update()
            fh=sudoku_list[0] if len(sudoku_list)>0 else fh
            disp()
            button_3.button_update()
            
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                edit_mode=not edit_mode
            if event.key==pygame.K_RETURN and edit_mode:
                screen.blit(surface_1,(0,0))
                screen.blit(title_text,title_text.get_rect(center=(600,100)))
                disp()
        if not button_1.safe:
            for i in range(9):
                for j in range(9):
                    if temp_list[i][j].rect2.collidepoint(pygame.mouse.get_pos()):
                        keys=pygame.key.get_pressed()
                        for k in range(10):
                            if keys[getattr(pygame, f'K_{k}')]:
                                fh[i][j] = k
                                temp_list[i][j].update_display(zero_elimintor(k),1)
                
    if not button_2.safe and button_1.safe:
        disp()
        solve(fh)
        button_2.button_update()

    pygame.display.update()
    clock.tick(60)
