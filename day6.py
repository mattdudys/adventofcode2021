from collections import Counter


initial_fish = [5,1,1,1,3,5,1,1,1,1,5,3,1,1,3,1,1,1,4,1,1,1,1,1,2,4,3,4,1,5,3,4,1,1,5,1,2,1,1,2,1,1,2,1,1,4,2,3,2,1,4,1,1,4,2,1,4,5,5,1,1,1,1,1,2,1,1,1,2,1,5,5,1,1,4,4,5,1,1,1,3,1,5,1,2,1,5,1,4,1,3,2,4,2,1,1,4,1,1,1,1,4,1,1,1,1,1,3,5,4,1,1,3,1,1,1,2,1,1,1,1,5,1,1,1,4,1,4,1,1,1,1,1,2,1,1,5,1,2,1,1,2,1,1,2,4,1,1,5,1,3,4,1,2,4,1,1,1,1,1,4,1,1,4,2,2,1,5,1,4,1,1,5,1,1,5,5,1,1,1,1,1,5,2,1,3,3,1,1,1,3,2,4,5,1,2,1,5,1,4,1,5,1,1,1,1,1,1,4,3,1,1,3,3,1,4,5,1,1,4,1,4,3,4,1,1,1,2,2,1,2,5,1,1,3,5,2,1,1,1,1,1,1,1,4,4,1,5,4,1,1,1,1,1,2,1,2,1,5,1,1,3,1,1,1,1,1,1,1,1,1,1,2,1,3,1,5,3,3,1,1,2,4,4,1,1,2,1,1,3,1,1,1,1,2,3,4,1,1,2]

def tick(counts):
    """
    >>> tick(Counter({0: 5, 3: 2}))
    Counter({6: 5, 8: 5, 2: 2})
    """
    new_counts = Counter()
    for timer, count in counts.most_common():
        if timer == 0:
            # the mama fish resets to 6
            new_counts[6] += count
            # the baby fish starts at 8, one baby fish for each mama fish
            new_counts[8] += count
        else:
            new_counts[timer - 1] += count
    return new_counts


fish_by_timer = Counter(initial_fish)
print(fish_by_timer)
for i in range(0, 256):
    fish_by_timer = tick(fish_by_timer)
print(fish_by_timer)
print(sum(fish_by_timer.values()))
