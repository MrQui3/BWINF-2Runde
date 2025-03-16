import pygame
from main import create_matrix, read_data_from_file

width, height, data = read_data_from_file('labyrinthe2.txt')

matrix_horizontal_1, matrix_vertical_1, gruben_1 = create_matrix(data, height)
matrix_horizontal_2, matrix_vertical_2, gruben_2 = create_matrix(data, height)

block_size = 12


pygame.init()
screen = pygame.display.set_mode([width*block_size*2+100, height*block_size*2+100], pygame.RESIZABLE)
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.KEYUP])


def draw_maze(pos_x, pos_y, horizontal_matrix, vertical_matrix, gruben, is_gruben=True):
    pygame.draw.rect(screen,(192, 192, 192), (pos_x, pos_y, width*block_size, height*block_size))
    # Borders
    pygame.draw.rect(screen, (0, 0, 0), (pos_x, pos_y, width*block_size, 3))
    pygame.draw.rect(screen, (0, 0, 0), (pos_x, pos_y, 3, height*block_size))
    pygame.draw.rect(screen, (0, 0, 0), (pos_x, pos_y+height*block_size, width*block_size+3, 3))
    pygame.draw.rect(screen, (0, 0, 0), (pos_x+width*block_size, pos_y, 3, height*block_size))

    for i in range(len(horizontal_matrix)):
        for j in range(len(horizontal_matrix[i])):
            if horizontal_matrix[i][j] == 1:
                pygame.draw.line(screen, (0, 0, 0), (pos_x+(j*block_size), pos_y+(i*block_size)+block_size), (pos_x+block_size+(j*block_size), pos_y+(i*block_size)+block_size))
    for i in range(len(vertical_matrix)):
        for j in range(len(vertical_matrix[i])):
            if vertical_matrix[i][j] == 1:
                pygame.draw.line(screen, (0, 0, 0), (pos_x+(block_size*j)+block_size, pos_y+(i*block_size)), (pos_x+(block_size*j)+block_size, pos_y+(i*block_size)+block_size))

    if is_gruben:
        for i in range(len(gruben)):
            pygame.draw.rect(screen, (0, 0, 0), (pos_x+(gruben[i][0]*block_size), pos_y+(gruben[i][1]*block_size), block_size, block_size))


screen.fill((255, 255, 255))
draw_maze(25, 25, matrix_horizontal_1, matrix_vertical_1, gruben_1, False)
draw_maze(50 + width*block_size, 25, matrix_horizontal_2, matrix_vertical_2, gruben_2, False)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
