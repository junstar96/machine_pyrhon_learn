import sys

check_x_pos = [1, 0, -1, 0]
check_y_pos = [0, 1, 0, -1]

global PATHWAY_COL
global WALL_COL
global BLOCK_COL
global PATH_COL
global maze

PATHWAY_COL = 0
WALL_COL = 1
BLOCK_COL = 2
PATH_COL = 3

maze = [[0,1,1],[0,0,1],[0,0,0]]

def print_maze():
    for i in maze:
        print(i)

def findpath(x, y, n):
    global PATHWAY_COL
    global WALL_COL
    global BLOCK_COL
    global PATH_COL
    global maze

    print_maze()
    print(x, y)

    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    elif maze[x][y] != PATHWAY_COL:
        return False
    elif x == n-1 and y == n-1: #visual 버전은 1칸씩 빼자, n-1로
        print("hello")
        maze[x][y] = PATH_COL
        return True
    else:
        maze[x][y] = PATH_COL
        print("현재 위치")
        if findpath(x-1, y, n) or findpath(x, y+1, n) or findpath(x+1, y, n) or findpath(x, y-1, n):
                return True
        else:
            maze[x][y] = BLOCK_COL
            return False

findpath(0,0,3)

print_maze()

