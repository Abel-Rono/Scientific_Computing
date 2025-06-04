# Generate arithmetic sequence: start=5, difference=3, terms=8

sequence = []
start = 5
diff = 3

for i in range(8):
    term = start + i * diff
    sequence.append(term)

print(sequence)