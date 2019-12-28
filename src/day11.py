import intcode
import sys

part2 = True

program_code = [int(s) for s in open("data/data11.txt", "rt").readline().split(',')]

pipes = intcode.CommPipes()

t = intcode.IntCode(program_code, pipes, mem_size = 2048)
t.start()

dirs = [(0,-1), (1,0), (0,1), (-1,0)]
dir_index = 0
x = y = x_max = y_max = 0
plane = {}

while True:
    color = (1 if part2 else 0) if not (x,y) in plane.keys() else plane[(x,y)]
    pipes.client_put(color)
    color = pipes.client_get()
    if color == None:
        break
    plane[(x,y)] = color
    dir_index = (dir_index + (1 if pipes.client_get() == 1 else -1)) % len(dirs)
    (dx, dy) = dirs[dir_index]
    x += dx
    y += dy
    x_max = max(x_max, x+1)
    y_max = max(y_max, y+1)

if not part2:
    print(len(plane))
else:
    for y in range(y_max):
        for x in range(x_max):
            color = 0 if not (x,y) in plane.keys() else plane[(x,y)]
            sys.stdout.write(' ' if color == 0 else '*')
        sys.stdout.write('\n')
