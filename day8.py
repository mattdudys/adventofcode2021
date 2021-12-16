import fileinput
from collections import defaultdict

digit_to_segments = {
    0: frozenset('abcefg'),
    1: frozenset('cf'),
    2: frozenset('acdeg'),
    3: frozenset('acdfg'),
    4: frozenset('bcdf'),
    5: frozenset('abdfg'),
    6: frozenset('abdefg'),
    7: frozenset('acf'),
    8: frozenset('abcdefg'),
    9: frozenset('abcdfg')
}
segments_to_digit = {segments: int_val for int_val, segments in digit_to_segments.items()}

digits_by_segment_size = defaultdict(list)
for digit, segments in digit_to_segments.items():
    digits_by_segment_size[len(segments)].append(digit)


def group_signalss_by_size(signalss):
    grouped = defaultdict(list)
    for signals in signalss:
        grouped[len(signals)].append(signals)
    return grouped


def read_input():
    for line in fileinput.input():
        all_digit_signals, output_signals = line.rstrip().split(' | ')
        all_digit_signals = [frozenset(signals) for signals in all_digit_signals.split(' ')]
        output_signals = [frozenset(signals) for signals in output_signals.split(' ')]
        yield all_digit_signals, output_signals


def count_1478(entries):
    count = 0
    for _, digit_signals in entries:
        for signals in digit_signals:
            signals_size = len(signals)
            if len(digits_by_segment_size[signals_size]) == 1:
                count += 1
    return count


def deduce_signals_to_digits(signalss):
    signalss_of_size = group_signalss_by_size(signalss)
    digit_to_signals = {
        1: signalss_of_size[2][0],
        7: signalss_of_size[3][0],
        4: signalss_of_size[4][0],
        8: signalss_of_size[7][0]
    }
    for signals in signalss_of_size[6]:
        if not digit_to_signals[1].issubset(signals):
            digit_to_signals[6] = signals
        elif digit_to_signals[4].issubset(signals):
            digit_to_signals[9] = signals
        else:
            digit_to_signals[0] = signals
    for signals in signalss_of_size[5]:
        if digit_to_signals[1].issubset(signals):
            digit_to_signals[3] = signals
        elif len(signals & digit_to_signals[4]) == 2:
            digit_to_signals[2] = signals
        else:
            digit_to_signals[5] = signals

    assert len(digit_to_signals) == 10

    signals_to_digits = {signals: digit for digit, signals in digit_to_signals.items()}
    return signals_to_digits


def translate_signals_to_number(signalss, signals_to_digits):
    number = 0
    for signals in signalss:
        number *= 10
        digit = signals_to_digits[signals]
        number += digit
    return number


def part2(entries):
    total = 0
    for entry in entries:
        signals_to_digits = deduce_signals_to_digits(entry[0])
        number = translate_signals_to_number(entry[1], signals_to_digits)
        total += number
    return total


def main():
    entries = list(read_input())
    #print(count_1478(entries))

    print(part2(entries))


if __name__ == '__main__':
    main()
