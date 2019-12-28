import itertools
import intcode
import queue

part2 = True

program_code = [int(s) for s in open("data/data07.txt", "rt").readline().split(',')]

if part2:
    values = [5, 6, 7, 8, 9]
else:
    values = [0, 1, 2, 3, 4]

max_output = float('-inf')

for i in itertools.permutations(values):
    output = 0
    vals = list(i)
    if not part2:
        for v in vals:
            pipes = intcode.CommPipes()
            t = intcode.IntCode(program_code, pipes, mem_size = 1024)
            t.start()
            pipes.client_put(v)
            pipes.client_put(output)
            output = pipes.client_get()
            t.join()
    else:
        pipe_list = []
        threads = []
        for idx in range(5):
            q = queue.Queue()
            q.put(vals[idx])
            if idx == 0:
                q.put(0)
            pipe_list.append(q)
        for idx in range(5):
            threads.append(intcode.IntCode(program_code, intcode.CommPipes(pipe_list[idx], pipe_list[(idx + 1)%5]), mem_size = 1024))
            threads[idx].start()
        for t in threads:
            t.join()
        output = pipe_list[0].get()
    max_output = max(max_output, output)

print(max_output)
