import intcode
import sys

part2 = True

program_code = [int(s) for s in open("data/data19.txt", "rt").readline().split(',')]

x_init = y_init = 0
step = 100 if part2 else 50

while True:
    count = 0
    x_add = y_add = -20
    for y in range(y_init, y_init + step):
        for x in range(x_init, x_init + step):
            pipes = intcode.CommPipes()
            t = intcode.IntCode(program_code, pipes, mem_size = 512)
            t.start()
            pipes.client_put(x)
            pipes.client_put(y)
            res = pipes.client_get()
            if res == 1:
                count += 1
            if part2:
                if res == 1:
                    if x == x_init and y_add < 0:
                        y_add = 0
                    if y == y_init and x_add < 0:
                        x_add = 0
                else:
                    if y == y_init and y_add == 0:
                        y_add = step + x_init - x
                    if x == x_init and x_add == 0:
                        x_add = step + y_init - y
    if not part2 or count == 10000:
        break
    x_init += x_add
    y_init += y_add

if not part2:
    print(count)
else:
    print(10000 * x_init + y_init)
