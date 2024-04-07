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
            if p == 0 :
                print('.', end =' ')
            elif p == 2:
                print(Color.BOLD + Color.RED + 'O' + Color.END, end=' ')
            elif p == 3:
                print(Color.BOLD + Color.BLUE + '*' + Color.END, end=' ')
            elif p == 4:
                print(Color.BOLD + Color.RED + '#' + Color.END, end=' ')
            else:
                print(Color.BOLD + Color.GREEN + '#' + Color.END, end=' ')
        print()

    return 1

def beam_reset(map_arr):
    for h in range(len(map_arr)):
        for w in range(len(map_arr[0])):
            map_arr[h][w] = 1 if map_arr[h][w] == 1 or map_arr[h][w] == 4 else 0

def dla(map_arr, coverage=0.10, d = 0.2):
    width = len(map_arr[0])
    height = len(map_arr)

    iteration = 0

    while sum(map(sum,map_arr)) <= coverage * width * height:
        iteration = iteration + 1
        while True:
            start_block = (random.randint(0,width-1),random.randint(0,height-1))
            if map_arr[start_block[1]][start_block[0]] == 0:
                break

        valid = False

        while not valid:
            angle = random.random()*2*math.pi
            delta_y = max(min(math.tan(angle), 40), -40)
            dirrection = 1 if math.cos(angle)>=0 else -1

            beam = [start_block[0],start_block[1]]
            while 0<=beam[0]<width and 0<=beam[1]<height:
                beam[0] = beam[0] + d * dirrection
                beam[1] = beam[1] + d * delta_y
                if 0<=beam[0]<width and 0<=beam[1]<height:
                    if map_arr[math.floor(beam[1])][math.floor(beam[0])]  == 1 :
                        valid = True

        beam = [start_block[0], start_block[1]]
        while 0 <= beam[0] < width and 0 <= beam[1] < height:
            beam[0] = beam[0] + d * dirrection
            beam[1] = beam[1] + d * delta_y
            if 0 <= beam[0] < width and 0 <= beam[1] < height:
                if map_arr[math.floor(beam[1])][math.floor(beam[0])] == 1:
                    map_arr[math.floor(beam[1] - d * delta_y)][math.floor(beam[0] - d * dirrection)] = 4
                    break
                map_arr[math.floor(beam[1])][math.floor(beam[0])] = 3

        map_arr[start_block[1]][start_block[0]] = 2

        display_screen(map_arr, display_text="Iteration = {idx}".format(idx = iteration))
        beam_reset(map_arr)

    return map_arr


def main():
    random.seed(1234)   # 시드 설정
    map_width = 40      # 전체 지도의 가로 크기
    map_height = 30     # 전체 지도의 세로 크기

    map_arr = [[0]*map_width for _ in range(map_height)]    # 지도 생성
    map_arr[int(map_height/2)][int(map_width/2)] = 1
    display_screen(map_arr, 'Init map')

    dla(map_arr)

    display_screen(map_arr, display_text="Final Map")



if __name__ == '__main__':
    main()
