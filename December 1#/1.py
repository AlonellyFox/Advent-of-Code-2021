values = []
inc_count = 0
last_buffer = None


with open("./input.txt", "r") as f:
    read = f.readline()
    while read != "":
        value = int(read)
        values.append(value)

        if last_buffer is not None:
            if value > last_buffer:
                inc_count += 1

        last_buffer = value

        read = f.readline()

print(inc_count)