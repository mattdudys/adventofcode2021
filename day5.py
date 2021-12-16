import fileinput
from pprint import pprint
from collections import Counter


def read_input():
    def parse():
        for line in fileinput.input():
            line = line.rstrip()
            start, end = line.split(' -> ')
            x1, y1 = start.split(',')
            x2, y2 = end.split(',')
            yield ((int(x1), int(y1)), (int(x2), int(y2)))
    return list(parse())


def draw_line(line):
    """
    >>> list(draw_line(((1, 1), (1, 1))))
    [(1, 1)]
    >>> list(draw_line(((0, 0), (0, 2))))
    [(0, 0), (0, 1), (0, 2)]
    >>> list(draw_line(((0, 2), (0, 0))))
    [(0, 2), (0, 1), (0, 0)]
    >>> list(draw_line(((0, 1), (2, 1))))
    [(0, 1), (1, 1), (2, 1)]
    """
    (x1, y1), (x2, y2) = line
    yield x1, y1
    while x1 != x2 or y1 != y2:
        # move x1 closer to x2
        if x1 < x2:
            x1 += 1
        elif x1 > x2:
            x1 -= 1
        # move y1 closer to y2
        if y1 < y2:
            y1 += 1
        elif y1 > y2:
            y1 -= 1
        yield x1, y1


def is_vertical(line):
    return line[0][0] == line[1][0] or line[0][1] == line[1][1]


def draw_lines(lines):
    for line in lines:
        if is_vertical(line):
            yield from draw_line(line)


def count_more_than_one(point_counts):
    return sum(1 for point, count in point_counts.most_common() if count > 1)


def main():
    lines = read_input()
    point_counts = Counter(draw_lines(lines))
    print(count_more_than_one(point_counts))

if __name__ == '__main__':
    main()
