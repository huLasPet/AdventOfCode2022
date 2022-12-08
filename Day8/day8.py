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


with open("input.txt") as input_data:
    line = input_data.readlines()
    for item in line:
        trees.append(item.strip())

height = len(trees)
width = len(trees[0])

#Create a dict with the coordinates of the trees and their height
for row_number, row_value in enumerate(trees):
    for column_number, column_value in enumerate(row_value):
        trees_dict[(column_number, row_number)] = int(column_value)

tallest_tree = max(trees_dict.values())

#Check the 4 directions
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

direction = {"up": (1,0), "down": (-1, 0), "left": (0, -1), "right": (0, 1)}
best_match = 0
for row in range(1, width - 1):
    for column in range(1, height - 1):
        start_height = trees_dict[(row, column)]
        scores = []
        #Grab the values to use when moving the rows and columns
        for up_down, left_right in direction.values():
            #Set score for current tree to 0 and set starting columns to use when moving
            current_score = 0
            row_move, column_move = row, column
            while True:
                #Move to the next row or column up/down or left/right, if not edge or tree too high increase score
                row_move, column_move = row_move + up_down, column_move + left_right
                #Reached the edge
                if row_move < 0 or column_move < 0 or row_move >= width or column_move >= height:
                    break
                current_score += 1
                #Found a tree too high
                if trees_dict[(row_move, column_move)] >= start_height:
                    break
            scores.append(current_score)
        #Checking and setting a new best_match if needed
        final_score = scores[0] * scores[1] * scores[2] * scores[3]
        if final_score > best_match:
            best_match = final_score

print(f"Part 2 answer: {best_match}")
