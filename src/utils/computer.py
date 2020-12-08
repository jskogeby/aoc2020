
class Computer:

    def __init__(self, instructions):
        self.instructions = instructions
        self.acc = 0
        self.current_line = 0
        self.read_instructions = []

    def read_line(self):
        self.read_instructions.append(self.current_line)
        op, arg = self.instructions[self.current_line]
        if op == "acc":
            self.acc += arg
            self.current_line += 1
        elif op == "jmp":
            self.current_line += arg
        elif op == "nop":
            self.current_line += 1
    
    def execute(self):
        while self.current_line not in self.read_instructions:
            if self.current_line >= len(self.instructions):
                return self.acc
            self.read_line()
        return None
        