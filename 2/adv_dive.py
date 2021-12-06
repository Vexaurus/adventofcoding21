
class Submarine():
    
    def __init__(self, pos, depth, aim) -> None:
        self.pos = pos
        self.depth = depth
        self.aim = aim

        self.instructions = {
            'forward': lambda x: self.move(int(x)),
            'down': lambda x: self.change_aim(int(x)),
            'up': lambda x: self.change_aim(int(x) * -1) 
        }

    def change_depth(self, change) -> None:
        self.depth += self.aim * change

    def change_aim(self, change) -> None:
        self.aim += change

    def move(self, change) -> None:
        self.pos += change
        self.change_depth(change)

    def get_res(self) -> int:
        return self.pos * self.depth


if __name__ == '__main__':
    with open('./sub_input.txt', 'r') as raw:
        instrs =  raw.readlines()

    sub = Submarine(0, 0, 0)

    for instruction in instrs:
        cmd, chg = instruction.split()
        sub.instructions[cmd](chg)
    
    print(sub.get_res())

