import intcode

part2 = True

program_code = [int(s) for s in open("data/data05.txt", "rt").readline().split(',')]

pipes = intcode.CommPipes()

t = intcode.IntCode(program_code, pipes, mem_size = 1024)
t.start()

pipes.client_put(5 if part2 else 1)

while True:
    r = pipes.client_get()
    if r != 0:
        print(r)
        break

t.stop()
t.join()
