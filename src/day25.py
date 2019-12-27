import intcode
import sys

program_code = [int(s) for s in open("data/data25.txt", "rt").readline().split(',')]

commands = {}

commands["mouse"] = "north\ntake mouse\nsouth\n"
commands["pointer"] = "north\nnorth\ntake pointer\nsouth\nsouth\n"
commands["monolith"] = "west\ntake monolith\neast\n"
commands["food ration"] = "west\nnorth\nwest\ntake food ration\neast\nsouth\neast\n"
commands["space law space brochure"] = "west\nnorth\nwest\nsouth\ntake space law space brochure\nnorth\neast\nsouth\neast\n"
commands["mutex"] = "west\nsouth\nsouth\nwest\nsouth\ntake mutex\nnorth\n\neast\nnorth\nnorth\neast\n"
commands["asterisk"] = "west\nsouth\nsouth\nwest\ntake asterisk\neast\nnorth\nnorth\neast\n"
commands["sand"] = "west\nsouth\ntake sand\nnorth\neast\n"
commands["switch"] = "south\nsouth\nwest\nsouth\ninv\neast\n"
commands["solution"] = commands["mutex"] + commands["asterisk"] + commands["space law space brochure"] + commands["food ration"] + commands["switch"]

pipes = intcode.CommPipes()

t = intcode.IntCode(program_code, pipes, mem_size = 8192)
t.start()

last_line = ""
skip_input = 1

while True:
    c = chr(pipes.client_get())
    last_line += c

    if c == '\n':
        print(last_line)
        if last_line == "Command?\n":
            skip_input -= 1
        elif last_line.find("Oh, hello!") != -1:
            break
        last_line = ""

        if skip_input == 0:
            cmd = sys.stdin.readline()
            if cmd[:-1] in commands.keys():
                cmd = commands[cmd[:-1]]
                skip_input = len([x for x in cmd if x == '\n'])
            else:
                skip_input = 1
            for c in cmd:
                pipes.client_put(ord(c))

t.stop()
t.join()
