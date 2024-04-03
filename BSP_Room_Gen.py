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
    max_idx = max(max(map_arr))
    print('\n' + display_text + str(max_idx+1))


    for h in map_arr:
        for p in h:
            if p % 8==0:
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


def create_new_section(map_arr, section_info):
    max_idx = max(section_info)

    while True:
        selected_section = random.randrange(max_idx+1)
        selected_section_info = section_info[selected_section]
        if selected_section_info[2]>=8 or selected_section_info[3]>=8 : break

    if random.random()>=0.5 and selected_section_info[2]>=8 or selected_section_info[3]<8:
        # 가로 분할
        new_section_width = random.randint(max(math.ceil(selected_section_info[2]*0.4),4),min(math.floor(selected_section_info[2]*0.6)+1,selected_section_info[2]-3))
        for w in range(new_section_width):
            for h in range(selected_section_info[3]):
                map_arr[h+selected_section_info[1]][w+selected_section_info[0]] = max_idx+1

        section_info[selected_section] = (selected_section_info[0]+new_section_width,selected_section_info[1], selected_section_info[2]-new_section_width, selected_section_info[3])
        section_info[max_idx+1] = (selected_section_info[0], selected_section_info[1], new_section_width, selected_section_info[3])
    else:
        # 세로 분할
        new_section_height = random.randint(max(math.ceil(selected_section_info[3] * 0.4),4),
                                           min(math.floor(selected_section_info[3] * 0.6) + 1,selected_section_info[3]-3))
        for w in range(selected_section_info[2]):
            for h in range(new_section_height):
                map_arr[h+selected_section_info[1]][w + selected_section_info[0]]= max_idx+1

        section_info[selected_section] = (selected_section_info[0], selected_section_info[1]+new_section_height,
                                          selected_section_info[2], selected_section_info[3]-new_section_height)
        section_info[max_idx+1] = (
        selected_section_info[0], selected_section_info[1], selected_section_info[2], new_section_height)

    return map_arr


def main():
    random.seed(1234)   # 시드 설정
    map_width = 40      # 전체 지도의 가로 크기
    map_height = 30     # 전체 지도의 세로 크기

    map_arr = [[0]*map_width for _ in range(map_height)]    # 지도 생성
    section_info = dict()
    section_info[0]= (0,0,map_width,map_height) # (start x, start y, width, height)

    display_screen(map_arr, 'Number of Sections = ')

    for _ in range(15):
        create_new_section(map_arr, section_info)
        display_screen(map_arr, 'Number of Sections = ')



if __name__ == '__main__':
    main()
