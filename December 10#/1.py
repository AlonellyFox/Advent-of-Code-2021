from os import scandir


chunk_starts = ["(", "[", "{", "<"]
chunk_ends = [")", "]", "}", ">"]

illegal_score = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

def is_line_corrupted(line):
    global syntax_score
    chunk_buffer = []
    for c in line:
        if c in chunk_starts:
            chunk_buffer.append(c)
        elif c in chunk_ends:
            if (len(chunk_buffer) > 0):
                expected = chunk_buffer[len(chunk_buffer)-1]
                if chunk_ends.index(c) != chunk_starts.index(expected):
                    syntax_score += illegal_score[c]
                    return True
                else:
                    chunk_buffer.pop(len(chunk_buffer)-1)
            else:
                syntax_score += illegal_score[c]
                return True
    return False

syntax_score = 0

with open("./input.txt", "r") as f:
    line = f.readline()
    while line != "":
        line = line.replace("\n", "")

        is_line_corrupted(line)

        line = f.readline()

print(f"Syntax score: {syntax_score}")