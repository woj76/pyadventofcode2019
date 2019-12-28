import threading
import queue

class CommPipes():

    def __init__(self, inQ = queue.Queue(), outQ = queue.Queue()):
        self.inQueue = inQ
        self.outQueue = outQ
        self.finished = False

    def get(self):
        return self.inQueue.get()

    def put(self, e):
        self.outQueue.put(e)

    def client_put(self, e):
        self.inQueue.put(e)

    def client_get(self):
        if self.finished and self.outQueue.empty():
            return None
        else:
            return self.outQueue.get()


class IntCode(threading.Thread):

    def __init__(self, code, pipes, mem_size = 0):
        threading.Thread.__init__(self)
        self._stopflag = threading.Event()
        self.memory = code.copy()
        if mem_size > len(code):
            self.memory.extend([0] * (mem_size - len(code)))
        self.pipes = pipes

    def stop(self):
        self._stopflag.set()

    def stopped(self):
        return self._stopflag.isSet()

    def run(self):
        pc = 0
        rel_base = 0
        while not self.stopped():
            op_code = self.memory[pc]
            op_code_base = op_code % 100
            modes = op_code // 100
            mode0 = modes % 10
            modes //= 10
            mode1 = modes % 10
            modes //= 10
            mode2 = modes % 10
            index0 = pc + 1 if mode0 == 1 else self.memory[pc+1] + (rel_base if mode0 == 2 else 0)
            index1 = pc + 2 if mode1 == 1 else self.memory[pc+2] + (rel_base if mode1 == 2 else 0)
            index2 = pc + 3 if mode2 == 1 else self.memory[pc+3] + (rel_base if mode2 == 2 else 0)

            if op_code_base == 99:
                pc += 1
                self.pipes.finished = True
                break
            elif op_code_base == 3:
                self.memory[index0] = self.pipes.get()
                pc += 2
            elif op_code_base == 4:
                self.pipes.put(self.memory[index0])
                pc += 2
            elif op_code_base == 9:
                rel_base += self.memory[index0]
                pc += 2
            elif op_code_base in [1, 2, 5, 6, 7, 8]:
                data1 = self.memory[index0]
                data2 = self.memory[index1]
                res = None
                if op_code_base == 1:
                    res = data1 + data2
                    pc += 4
                elif op_code_base == 2:
                    res = data1 * data2
                    pc += 4
                elif op_code_base == 5:
                    if data1 != 0:
                        pc = data2
                    else:
                        pc += 3
                elif op_code_base == 6:
                    if data1 == 0:
                        pc = data2
                    else:
                        pc += 3
                elif op_code_base == 7:
                    res = 1 if data1 < data2 else 0
                    pc += 4
                elif op_code_base == 8:
                    res = 1 if data1 == data2 else 0
                    pc += 4
                if op_code_base != 5 and op_code_base != 6:
                    self.memory[index2] = res
