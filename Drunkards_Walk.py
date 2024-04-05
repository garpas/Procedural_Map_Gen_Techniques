import random
import os
import math
from time import sleep


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
    max_idx = max(map(max, map_arr))
    print('\n' + display_text + str(max_idx))

    for h in map_arr:
        for p in h:
            if p ==0 :
                print('.', end =' ')
            elif p == max_idx:
                print(Color.BOLD + Color.RED + '#' + Color.END, end=' ')
            else:
                print(Color.BOLD + Color.GREEN + '#' + Color.END, end=' ')
        print()
    return 1

def drunkard_walk(map_arr, coverage=0.22, walks= 100):
    width = len(map_arr[0])
    height = len(map_arr)

    drunkard = 0

    x_start, y_start  = int(width/2), int(height/2)
    vacancy = [(x_start,y_start)]

    while len(vacancy) < coverage*width*height:
        drunkard = drunkard + 1
        hulk = vacancy[random.randint(0,len(vacancy)-1)]
        map_arr[hulk[1]][hulk[0]] = drunkard

        for _ in range(walks):
            neighbor = []
            if hulk[0] > 0: neighbor.append((-1,0))
            if hulk[0] < width-1: neighbor.append((1, 0))
            if hulk[1] > 0: neighbor.append((0, -1))
            if hulk[1] < height-1: neighbor.append((0, 1))
            delta = neighbor[random.randint(0,len(neighbor)-1)]
            hulk = (hulk[0] + delta[0], hulk[1] + delta[1])
            vacancy.append(hulk)
            map_arr[hulk[1]][hulk[0]] = drunkard
        vacancy = list(set(vacancy))

        display_screen(map_arr, 'Number of Drunkards = ')


    return map_arr


def main():
    random.seed(1234)   # 시드 설정
    map_width = 40      # 전체 지도의 가로 크기
    map_height = 30     # 전체 지도의 세로 크기

    map_arr = [[0]*map_width for _ in range(map_height)]    # 지도 생성
    display_screen(map_arr, 'Number of Drunkards = ')

    drunkard_walk(map_arr)




if __name__ == '__main__':
    main()
