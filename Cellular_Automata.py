import random
import os
import math


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def display_screen(map_arr, display_text=''):
    print('\n' + display_text)

    for h in map_arr:
        for p in h:
            if p ==0 :
                print('.', end =' ')
            else:
                print(Color.BOLD + Color.GREEN +  '#' + Color.END, end=' ')
        print()

    return 1

def cellurar_automata_iter(map_arr):
    delta = [(-1,-1),(0,-1),(1,-1),(-1,0),(1,0),(-1,1),(0,1),(1,1)]
    height = len(map_arr)
    width = len(map_arr[0])

    next_map_arr = [[0]*width for _ in range(height)]

    for x in range(width):
        for y in range(height):
            wall = 0
            total = 0
            for d in delta:
                x_neighbor = x + d[0]
                y_neighbor = y + d[1]
                if 0<=x_neighbor<width and 0<=y_neighbor<height:
                    total = total + 1
                    if map_arr[y_neighbor][x_neighbor] == 1:
                        wall = wall + 1
            if wall == 0 or wall/total>= 5/8:
                next_map_arr[y][x] = 1
            else:
                next_map_arr[y][x] = 0

    return next_map_arr


def main():
    random.seed(1234)   # 시드 설정
    map_width = 40      # 전체 지도의 가로 크기
    map_height = 30     # 전체 지도의 세로 크기

    map_arr = []   # 지도 생성
    iteration  = 0

    # 랜덤 지도
    for h in range(map_height):
        map_arr.append([0 if random.random()>=0.5 else 1 for w in range(map_width)])


    display_screen(map_arr, 'Number of Iterations = {idx}'.format(idx = iteration))

    for iteration in range(5):
        map_arr = cellurar_automata_iter(map_arr)
        display_screen(map_arr, 'Number of Iterations = {idx}'.format(idx=iteration+1))



if __name__ == '__main__':
    main()
