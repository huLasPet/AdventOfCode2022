import re

# Part 1
# How many groups contain their pair group fully

# Part 2
# How many groups contain any part of their pair group


def range_overlap(range1, range2):
    # Copied from https://stackoverflow.com/a/70622860/17890536
    """Whether range1 and range2 overlap."""
    x1, x2 = range1.start, range1.stop
    y1, y2 = range2.start, range2.stop
    return x1 <= y2 and y1 <= x2


def count_overlap(part, end_range_modifier):
    """Part 1 should have 1 end_range_modifier and Part 2 should have 0"""
    count = 0
    with open("input.txt") as data:
        for line in data:
            line = re.split(',|-', line)
            group1_list = range(int(line[0]), int(line[1]) + end_range_modifier)
            group2_list = range(int(line[2]), int(line[3]) + end_range_modifier)

            if part == 1:
                result = group1_list[0] in group2_list and group1_list[-1] in group2_list
                result2 = group2_list[0] in group1_list and group2_list[-1] in group1_list
                if result or result2:
                    count += 1

            elif part == 2:
                if range_overlap(group1_list, group2_list):
                    count += 1
                    
            else:
                return "Invalid part selection"
    return count


print(f"Part 1 count is {count_overlap(1, 1)} and Part 2 count is {count_overlap(2, 0)}")
