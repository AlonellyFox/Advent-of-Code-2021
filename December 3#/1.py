diagnostics_report = []
gamma_rate = ""
epsilon_rate = ""

def flip(input_string):
    out = ""
    for i in input_string:
        out = out + ("1" if i == "0" else "0")
    return out

with open("./input.txt", "r") as f:
    diagnostics_report = f.readlines()

for i in range(len(diagnostics_report[0]) - 1):
    one_count = 0
    for j in range(len(diagnostics_report)):
        current = diagnostics_report[j][i]
        if (current == "1"): one_count += 1
    
    gamma_rate = gamma_rate + ("1" if (one_count > len(diagnostics_report) * 0.5) else "0")
epsilon_rate = flip(gamma_rate)

b10_gamma = int(gamma_rate, 2)
b10_epsilon = int(epsilon_rate, 2)

print(f"Output: {b10_gamma * b10_epsilon}")