import time
import numpy as np

def rem_bombs(grid):
    indexes=[]
    for i in range(0,len(grid)):
        for k in range(0,len(grid[0])):
            if(grid[i][k]=='0'):
                indexes.append((i,k))
    return indexes

def plant_bombs(grid,chance=100):
    for i in range(0,len(grid)):
        for k in range(0,len(grid[0])):
            if(np.random.randint(1,101) <= chance):
                grid[i][k]='0'

    return grid

def exp_bomb(grid,indexes):
    
    for i,k in indexes:
        if i<(len(grid)-1):
            grid[i+1][k]='*'
        if i>0:
            grid[i-1][k]='*'
        if k<(len(grid[0])-1):
            grid[i][k+1]='*'
        if k>0:
            grid[i][k-1]='*'
            
        grid[i][k]='*'

    return grid

def show_grid(grid):
    for i in grid:
        print(i)


def bomber_man(seconds):

    cur_seconds=0

    grid=[['*' for i in range(0,5)] for k in range(0,5)]

    plant_bombs(grid,chance=20)

    cur_seconds+=1
    time.sleep(1)
    
    
    show_grid(grid)
    print('\n\n')



    while cur_seconds<seconds:

        bomb_loc=rem_bombs(grid)
        
        grid=plant_bombs(grid)

        cur_seconds+=1
        time.sleep(1)

        show_grid(grid)
        print('\n\n')

        if(cur_seconds==seconds):
            break

        grid=exp_bomb(grid,bomb_loc)

        cur_seconds+=1
        time.sleep(1)

        show_grid(grid)
        print('\n\n')

    return grid


    



    for i in grid:
        print(i)

grid=bomber_man(11)

show_grid(grid)

