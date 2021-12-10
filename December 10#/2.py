from math import floor

chunk_starts = ["(", "[", "{", "<"]
chunk_ends = [")", "]", "}", ">"]

scoring = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

line_syntax_scores = []
with open("./input.txt", "r") as f:
    line = f.readline()
    while line != "":
        line = line.replace("\n", "")

        chunk_buffer = []
        corrupted_line = False
        for c in line:
            if c in chunk_starts:
                chunk_buffer.append(c)
            elif c in chunk_ends:
                if (len(chunk_buffer) > 0):
                    expected = chunk_buffer[len(chunk_buffer)-1]
                    if chunk_ends.index(c) != chunk_starts.index(expected):
                        corrupted_line = True
                        break
                    else:
                        chunk_buffer.pop(len(chunk_buffer)-1)
                else:
                    corrupted_line = True
                    break
        
        if not corrupted_line:
            missing = []
            for i in range(len(chunk_buffer)-1, -1, -1):
                missing.append(chunk_ends[chunk_starts.index(chunk_buffer[i])])

            line_syntax_score = 0
            for m in missing:
                line_syntax_score *= 5
                line_syntax_score += scoring[m]
            line_syntax_scores.append(line_syntax_score)

        line = f.readline()

line_syntax_scores.sort()
print(line_syntax_scores[floor(len(line_syntax_scores)*0.5)])