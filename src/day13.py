import intcode
import sys

part2 = True

program_code = [int(s) for s in open("data/data13.txt", "rt").readline().split(',')]

pipes = intcode.CommPipes()

t = intcode.IntCode(program_code, pipes, mem_size = 4096)
t.start()

tile_count = 0
total_score = 0

while True:
    x = pipes.client_get()
    y = pipes.client_get()
    t = pipes.client_get()
    if t == None:
        break
    if t == 2:
        tile_count += 1
        total_score += program_code[1647 + ((24*x + y) * program_code[613] + program_code[616]) % (24 * 42 * 64) % (24 * 42 * 8) % (24 * 42)]

print(total_score if part2 else tile_count)
