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
            if p == 0:
                print('.', end=' ')
            else:
                print(Color.BOLD + Color.YELLOW + '#' + Color.END, end=' ')
        print()

    return 1


def generate_room(map_arr):

    while True:
        x_cord = random.randrange(len(map_arr[0])-2)
        y_cord = random.randrange(len(map_arr)-2)
        room_width = random.randrange(3, 10)
        room_height = random.randrange(3, 10)

        if max(max([row[x_cord:x_cord+room_width] for row in map_arr[y_cord:y_cord+room_height]])) == 0: break

    for w in range(room_width):
        for h in range(room_height):
            if x_cord+w < len(map_arr[0]) and y_cord+h < len(map_arr):
                map_arr[y_cord+h][x_cord+w] = map_arr[y_cord+h][x_cord+w] + 1

    return map_arr


def main():
    random.seed()
    map_width = 40
    map_height = 30

    map_arr = [[0]*map_width for _ in range(map_height)]


    for i in range(10):
        generate_room(map_arr)
        display_screen(map_arr,'Room {idx} Generate'.format(idx=i+1))

    return 0


if __name__ == '__main__':
    main()
