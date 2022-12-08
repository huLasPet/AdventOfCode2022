trees = []
trees_dict = {}
visible_trees = set()


def count_tree(def_row, def_column, def_min_height):
    """Count the visible trees in 4 direction. Direction is set by the input row and column."""
    if trees_dict[(def_row, def_column)] > def_min_height:
        visible_trees.add((def_row, def_column))
        return trees_dict[(def_row, def_column)]
    else:
        return def_min_height


with open("example.txt") as input_data:
    line = input_data.readlines()
    for item in line:
        trees.append(item.strip())

height = len(trees)
width = len(trees[0])

for row_number, row_value in enumerate(trees):
    for column_number, column_value in enumerate(row_value):
        trees_dict[(column_number, row_number)] = int(column_value)

tallest_tree = max(trees_dict.values())


for row in range(width):
    min_height = -1
    for column in range(height):
        min_height = count_tree(row, column, min_height)


for column in range(height):
    min_height = -1
    for row in range(width):
        min_height = count_tree(row, column, min_height)

for row in range(width):
    min_height = -1
    for column in reversed(range(height)):
        min_height = count_tree(row, column, min_height)

for column in range(height):
    min_height = -1
    for row in reversed(range(width)):
        min_height = count_tree(row, column, min_height)


print(f"Part 1 answer: {len(visible_trees)}")

#Part 2

for row in range(width):
    for column in range(height):
        print(trees_dict[(row, column)], end=" ")
    print()
