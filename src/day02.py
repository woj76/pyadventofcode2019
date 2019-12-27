def runProgram(code):
    pc = 0
    while True:
        opcode = code[pc]
        if opcode == 99:
            break
        if opcode == 1 or opcode == 2:
            data1 = code[code[pc+1]]
            data2 = code[code[pc+2]]
            code[code[pc+3]] = data1 + data2 if opcode == 1 else data1 * data2
        pc += 4

part2 = True

program_code = [int(s) for s in open("data/data02.txt", "rt").readline().split(',')]

if part2:
    target = 19690720
    for (p1, p2) in [(p,q) for p in range(100) for q in range(100)]:
        code = program_code.copy()
        code[1:3] = [p1, p2]
        runProgram(code)
        if code[0] == target:
            print(100*p1 + p2)
            break
else:
    program_code[1] = 12
    program_code[2] = 2
    runProgram(program_code)
    print(program_code[0])
