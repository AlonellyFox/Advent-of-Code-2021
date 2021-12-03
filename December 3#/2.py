def filter(arr, filtering_index, filtering_oxygen):
    fitting_values = []
    ones_count = count_ones(arr, filtering_index)
    more_ones = ones_count >= len(arr) * 0.5
    if filtering_oxygen:
        for i in arr:
            if (more_ones and i[filtering_index] == "1") or (not(more_ones) and i[filtering_index] == "0"):
                fitting_values.append(i)
    else:
        for i in arr:
            if (more_ones and i [filtering_index] == "0") or (not(more_ones) and i [filtering_index] == "1"):
                fitting_values.append(i)
    return fitting_values

def count_ones(arr, index):
    ones_count = 0
    for i in arr:
        if (i[index] == "1"): ones_count += 1
    return ones_count

diagnostics_report = []

with open("./input.txt", "r") as f:
    diagnostics_report = f.readlines()

working_list = diagnostics_report
for i in range(len(diagnostics_report[0])):
    working_list = filter(working_list, i, True)
    if (len(working_list) == 1): break
oxygen_rating = working_list[0]

working_list = diagnostics_report
for i in range(len(diagnostics_report[0])):
    working_list = filter(working_list, i, False)
    if (len(working_list) == 1): break
carbon_rating = working_list[0]

b10_oxygen = int(oxygen_rating, 2)
b10_carbon = int(carbon_rating, 2)

print(f"Output: {b10_oxygen * b10_carbon}")