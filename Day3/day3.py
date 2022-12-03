#1st half of characters 1 compartment, 2nd half 2nd compartment
#Lowercase item types a through z have priorities 1 through 26.
#Uppercase item types A through Z have priorities 27 through 52.
import math

part1_result = 0

def check_letter(letter):
    if letter.isupper():
        return (ord(letter) - 38)
    else:
        return (ord(letter) - 96)


with open("input.txt") as input_data:
    for line in input_data:
        half = math.floor(len(line)/2)
        first_half = line[0:half]
        second_half = line[half:]
        for letter in first_half:
            if letter in second_half:
                part1_result += check_letter(letter)
                break

print(part1_result)

#Part 2
#3 lines are 1 group, 1 letter of priority that exists in all 3
#Sum the priorities for all groups

line_number = 0
group_line = []
part2_result = 0
with open("input.txt") as input_data_2:
    for line in input_data_2:
        if line_number < 3:
            group_line.append(line.strip())
            line_number += 1
        else:
            for letter in group_line[0]:
                if letter in group_line[1]:
                    if letter in group_line[2]:
                        part2_result += check_letter(letter)
                        break
            #Resetting the line to 1 since we have 1 line read already, emptying the list and adding that read line
            line_number = 1
            group_line = []
            group_line.append(line.strip())

print(part2_result)

