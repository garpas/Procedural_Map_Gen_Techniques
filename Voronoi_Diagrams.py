import random
import os
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
    print('\n' + display_text)

    for h in map_arr:
        for p in h:
            if p <0 :
                print('.', end =' ')
            elif p % 8==0:
                print(Color.BOLD + Color.RED + '#' + Color.END, end=' ')
            elif p % 8==1:
                print(Color.BOLD + Color.YELLOW + '#' + Color.END, end=' ')
            elif p % 8==2:
                print(Color.BOLD + Color.GREEN + '#' + Color.END, end=' ')
            elif p % 8==3:
                print(Color.BOLD + Color.BLUE + '#' + Color.END, end=' ')
            elif p % 8==4:
                print(Color.BOLD + Color.DARKCYAN + '#' + Color.END, end=' ')
            elif p % 8==5:
                print(Color.BOLD + Color.CYAN + '#' + Color.END, end=' ')
            elif p % 8==6:
                print(Color.BOLD + Color.PURPLE + '#' + Color.END, end=' ')
            else:
                print(Color.BOLD +  '#' + Color.END, end=' ')
        print()

    return 1


def voronoi_diagram(map_arr, seednum, distance_method = 'Pythagoras'):
    map_width = len(map_arr[0])
    map_height = len(map_arr)

    seed = []
    for idx in range(seednum):
        while True:
            x = random.randint(0,map_width-1)
            y = random.randint(0,map_height-1)
            if not(x, y) in seed: break
        seed.append((x,y))
        map_arr[y][x] = idx

    if distance_method == 'Pythagoras':
        print("Distance Method : Pythagroas")
        dist_mehtod = lambda x, y , seed: pow(seed[0]-x, 2) + pow(seed[1]-y, 2)
    elif distance_method == 'Manhattan':
        print("Distance Method : Manhattan")
        dist_mehtod = lambda x, y, seed: abs(seed[0] - x) + abs(seed[1] - y)
    elif distance_method == 'Chebyshev':
        print("Distance Method : Chebyshev")
        dist_mehtod = lambda x, y, seed: max(abs(seed[0] - x), abs(seed[1] - y))
    else:
        print("Unknown distance method {}. Using defult Pythagoras".format(distance_method))
        dist_mehtod = lambda x, y, seed: pow(seed[0] - x, 2) + pow(seed[1] - y, 2)


    for w in range(map_width):
        for h in range(map_height):
            dist = []
            for s in seed:
                dist.append(dist_mehtod(w,h,s))
            map_arr[h][w] = dist.index(min(dist))

    return map_arr



def main():
    random.seed(1234)   # 시드 설정
    map_width = 40      # 전체 지도의 가로 크기
    map_height = 30     # 전체 지도의 세로 크기

    map_arr = [[-1]*map_width for _ in range(map_height)]    # 지도 생성

    distance_mehtod = 'Chebyshev'
    map_arr = voronoi_diagram(map_arr, 8,distance_mehtod)
    display_screen(map_arr, distance_mehtod)


if __name__ == '__main__':
    main()
