import intcode

part2 = True

program_code = [int(s) for s in open("data/data09.txt", "rt").readline().split(',')]

pipes = intcode.CommPipes()

t = intcode.IntCode(program_code, pipes, mem_size = 2048)
t.start()

pipes.client_put(2 if part2 else 1)

print(pipes.client_get())

t.stop()
t.join()
