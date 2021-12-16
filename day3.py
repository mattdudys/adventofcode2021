import fileinput
from collections import defaultdict, Counter


bit_counts = Counter()

observations = 0

for line in fileinput.input():
    observations += 1
    bit_counts += Counter(dict((i, int(bit)) for i, bit in enumerate(line.strip()[::-1])))

print(observations, bit_counts)
most_common = ['0'] * (max(bit_counts) + 1)
least_common = ['0'] * (max(bit_counts) + 1)

for i, ones_count in bit_counts.most_common():
    print(i, ones_count)
    zeroes_count = observations - ones_count
    if ones_count > zeroes_count:
        most_common[i] = '1'
        least_common[i] = '0'
    else:
        most_common[i] = '0'
        least_common[i] = '1'

print(int(''.join(reversed(most_common)), 2))
print(int(''.join(reversed(least_common)), 2))
