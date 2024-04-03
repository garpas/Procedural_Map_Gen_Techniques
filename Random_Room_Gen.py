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

    max_idx = max(max(map_arr))
    for h in map_arr:
        for p in h:
            if p == 0:
                print('.', end=' ')
            elif p == max_idx:
                print(Color.BOLD + Color.RED + '#' + Color.END, end=' ')
            else:
                print(Color.BOLD + Color.YELLOW + '#' + Color.END, end=' ')
        print()

    return 1


def generate_room(map_arr, idx=1):
    # 방의 위치와 크기를 랜덤하게 구함
    while True:
        x_cord = random.randrange(len(map_arr[0])-2)
        y_cord = random.randrange(len(map_arr)-2)
        room_width = random.randrange(3, 10)
        room_height = random.randrange(3, 10)

        # 구한 방과 기존방이 겹치는지 판단
        if max(max([row[max(0,x_cord-1):min(x_cord+room_width+1,len(map_arr[0])-1)] for row in map_arr[max(y_cord-1,0):min(y_cord+room_height+1,len(map_arr[0])-1)]])) == 0: break

    # 방을 map_arr에 표시
    for w in range(room_width):
        for h in range(room_height):
            if x_cord+w < len(map_arr[0]) and y_cord+h < len(map_arr):
                map_arr[y_cord+h][x_cord+w] = idx

    return map_arr


def main():
    random.seed(1234)   # 시드 설정
    map_width = 40      # 전체 지도의 가로 크기
    map_height = 30     # 전체 지도의 세로 크기

    map_arr = [[0]*map_width for _ in range(map_height)]    # 지도 생성


    for i in range(10): # 방 10개 생성
        generate_room(map_arr, i+1)
        display_screen(map_arr,'Room {idx} Generate'.format(idx=i+1))  # 생성한 방을 출력

    return 0


if __name__ == '__main__':
    main()
