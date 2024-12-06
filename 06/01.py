import os
import time

if __name__ == "__main__":
    with open("input.txt") as f:
        room = [[c for c in line.strip()] for line in f.readlines()]

    pos = [0, 0]

    for y, row in enumerate(room):
        for x, c in enumerate(row):
            if c == '^':
                pos = [x, y]
    
    x,y = pos

    dimension = len(room)*len(room[0])
    runs = 0

    while True:

        runs += 1
        os.system('cls')
        print(f"Run: {runs}/{dimension}")

        if dimension < runs:
            pass
            #print("aborting!")
            #raise IndexError
            for line in room:
                print("".join(line))
            print(f"pos: ({x}, {y})")
            time.sleep(1)
        


        if room[y][x] == '^':
            if y-1 < 0:
                break
            if not room[y-1][x] == '#':
                room[y][x] = 'X'
                y -= 1
                room[y][x] = '^'
                continue
            room[y][x] = '>'
            continue
        
        if room[y][x] == '>':
            if x+1 >= len(room[0]):
                break
            if not room[y][x+1] == '#':
                room[y][x] = 'X'
                x += 1
                room[y][x] = '>'
                continue
            room[y][x] = 'v'
            continue

        if room[y][x] == 'v':
            if y+1 >= len(room):
                break
            if not room[y+1][x] == '#':
                room[y][x] = 'X'
                y += 1
                room[y][x] = 'v'
                continue
            room[y][x] = '<'
            continue

        if room[y][x] == '<':
            if x-1 < 0:
                break
            if not room[y][x-1] == '#':
                room[y][x] = 'X'
                x -= 1
                room[y][x] = '<'
                continue
            room[y][x] = '^'
            continue

        break


    num = 0
    for line in room:
        for c in line:
            if c == 'X':
                num += 1
    print(num+1)
