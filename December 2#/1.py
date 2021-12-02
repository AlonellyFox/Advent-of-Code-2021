class Submarine:
    def __init__(self):
        self.x = 0
        self.depth = 0

    def submerge(self, amount):
        self.depth += amount

    def move(self, amount):
        self.x += amount

submarine = Submarine()

with open("input.txt", "r") as f:
    line = f.readline()
    while line != "":
        inputs = line.split(" ")
        cmd = inputs[0]
        value = int(inputs[1])

        match cmd:
            case "forward":
                submarine.move(value)
            case "down":
                submarine.submerge(value)
            case "up":
                submarine.submerge(-value)

        line = f.readline()

print(f"Output: {submarine.x * submarine.depth}")