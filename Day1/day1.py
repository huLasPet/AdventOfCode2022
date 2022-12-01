current_number = 0
top3 = []

with open('input.txt') as input_data:
    for line in input_data:
        if line == "\n":
            top3.append(current_number)
            current_number = 0
        else:
            current_number += int(line.strip())


top3.sort(reverse=1)
result = top3[0]+top3[1]+top3[2]
print(f"Highest number is {top3[0]} and the Top3 combined is {result}")
