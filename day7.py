import fileinput
from collections import Counter


def read_input_positions():
    for line in fileinput.input():
        return [int(position) for position in line.split(',')]


def center_of_gravity(position_counts):
    total = sum(position_counts.values())
    sum_position_weight = sum(position * count for position, count in position_counts.most_common())
    print(sum_position_weight, total, sum_position_weight / total)
    return round(sum_position_weight / total)


def constant_cost(position_counts, destination):
    """
    >>> constant_cost(Counter({1: 5, 4: 2}), 2)
    9
    """
    total_cost = 0
    for position, count in position_counts.most_common():
        distance = abs(position - destination)
        cost = count * distance
        #print(position, count, distance, cost)
        total_cost += cost
    return total_cost


def linear_cost(position_counts, destination):
    """
    >>> linear_cost(Counter({5: 1}), 5)
    0
    >>> linear_cost(Counter({5: 1}), 6)
    1
    >>> linear_cost(Counter({5: 1}), 7)
    3
    >>> linear_cost(Counter({5: 1}), 8)
    6
    >>> linear_cost(Counter({1: 5, 6: 2}), 4)
    36
    >>> linear_cost(Counter([16,1,2,0,4,2,7,1,2,14]), 5)
    168
    """
    total_cost = 0
    for position, count in position_counts.most_common():
        distance = abs(position - destination)
        distance_cost = (distance * (distance + 1)) // 2
        cost = distance_cost * count
        #print(position, count, distance, distance_cost, cost)
        total_cost += cost
    return total_cost


def main():
    positions = read_input_positions()
    position_counts = Counter(positions)

    best_position = center_of_gravity(position_counts)

    min_cost = linear_cost(position_counts, 0)
    for position in range(min(positions), max(positions) + 1):
        #cost = constant_cost(position_counts, position)
        cost = linear_cost(position_counts, position)
        print(position, cost)
        if cost < min_cost:
            print('*')
            #print(position, min_cost)
            min_cost = cost


if __name__ == '__main__':
    main()
