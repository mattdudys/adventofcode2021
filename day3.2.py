import fileinput
from collections import defaultdict, Counter

data = [line.rstrip() for line in fileinput.input()]

def most_common_in_position(data, position):
    counts = Counter(d[position] for d in data)
    return '1' if counts['1'] >= counts['0'] else '0'

def least_common_in_position(data, position):
    counts = Counter(d[position] for d in data)
    return '0' if counts['0'] <= counts['1'] else '1'

def filter_by_digit(data, bit_criteria, position):
    return [d for d in data if d[position] == bit_criteria]

def filter_until_one_left(data, criteria_function):
    for position in range(0, len(data[0])):
        bit_criteria = criteria_function(data, position)
        data = filter_by_digit(data, bit_criteria, position)
        print(position, bit_criteria, len(data))
        if len(data) == 1:
            break
    return data[0]

# oxygen generator rating, most common
oxygen_generator_rating = filter_until_one_left(data, most_common_in_position)
print(oxygen_generator_rating)
oxygen_generator_rating = int(oxygen_generator_rating, 2)

co2_scrubber_rating = filter_until_one_left(data, least_common_in_position)
print(co2_scrubber_rating)
co2_scrubber_rating = int(co2_scrubber_rating, 2)

life_support_rating = oxygen_generator_rating * co2_scrubber_rating

print('life_support_rating =', oxygen_generator_rating, '*', co2_scrubber_rating, '=', life_support_rating)
