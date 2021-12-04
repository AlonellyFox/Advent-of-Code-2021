class Board:
    def __init__(self, numbers):
        self.board = numbers
        self.marked = [[False for _ in range(5)] for _ in range(5)]

    def mark(self, drawn):
        for y in range(5):
            for x in range(5):
                if self.board[y][x] == drawn:
                    self.marked[y][x] = True
    
    def check_for_win(self):
        for y in range(5):
            full_line = True
            for x in range(5):
                if self.marked[y][x] == False:
                    full_line = False
                    break
            
            if full_line: return True
        
        for x in range(5):
            full_line = True
            for y in range(5):
                if self.marked[y][x] == False:
                    full_line = False
                    break
            
            if full_line: return True
        return False

    def get_remaining(self):
        remaining = []
        for y in range(5):
            for x in range(5):
                if self.marked[y][x] == False:
                    remaining.append(int(self.board[y][x]))
        return remaining

def board_input_to_arr(board_input):
    arr = []
    for l in board_input:
        buffer = []
        split = l.split(" ")
        # Units have an extra space, so split()
        # also returns empty values
        for v in split:
            if v != "":
                buffer.append(v)
        arr.append(buffer)
    return arr

number_pool = []
board_numbers = []
with open("./input.txt", "r") as f:
    # The first line of the input is the pool
    # from which we will draw numbers
    number_pool = f.readline().split(",")

    line = f.readline()
    board_buffer = []
    first_pass = True
    while line != "":
        if line == "\n":
            # First line would otherwise add 
            # an empty array to the board buffer
            if first_pass:
                first_pass = False
            else:
                board_numbers.append(board_buffer)
            board_buffer = []
        else:
            board_buffer.append(line.replace("\n", ""))
        
        line = f.readline()
    else:
        board_numbers.append(board_buffer)

boards = []
for i in board_numbers:
    boards.append(Board(board_input_to_arr(i)))

for i in number_pool:
    win = False
    for b in boards:
        b.mark(i)
        if b.check_for_win():
            print(sum(b.get_remaining()) * int(i))
            win = True
            break
    if win: break