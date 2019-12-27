import intcode
import sys

part2 = True

program_code = [int(s) for s in open("data/data21.txt", "rt").readline().split(',')]

pipes = intcode.CommPipes()

t = intcode.IntCode(program_code, pipes, mem_size = 4096)
t.start()

if part2:
    program = "OR A T\n" + "AND B T\n" + "AND C T\n" + "NOT T J\n" + "AND D J\n" + "NOT H T\n" + "NOT T T\n" + "OR E T\n" + "AND T J\n" + "RUN\n";
else:
    program = "NOT A T\n" + "NOT C J\n" + "OR T J\n" + "AND D J\n" + "WALK\n";

while True:
    c = chr(pipes.client_get())
    sys.stdout.write(c)
    if c == '\n':
        break

for c in program:
    pipes.client_put(ord(c))
    sys.stdout.write(c)

while True:
    c = pipes.client_get()
    if c == None:
        break
    if c < 128:
        sys.stdout.write(chr(c))
    else:
        print(c)

t.stop()
t.join()
