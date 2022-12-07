directory_size = {}
directory_list = []
result = 0
part2_values = []

with open("input.txt") as input_data:
    lines = input_data.readlines()
    current_folder = ""
    for line in lines:
        line = line.strip()
        if line[0] == "$":
            if line[2:4] == "cd" and line[-1] != ".":
                #Enter a folder and update the current_folder with full path and directory_list/size as well
                directory_list.append(current_folder)
                current_folder = directory_list[-1] + line[4:]
                if current_folder not in directory_size:
                    directory_size.update({current_folder: 0})
            if line[-1] == ".":
                #cd.. so go up a folder
                current_folder = directory_list.pop()
        elif line[0].isdigit():
            #If a line starts with a number, it is a file with a size so adding that to the directory_size
            size = ""
            for char in line:
                if char.isdigit():
                    size += char
                else:
                    break
            #Update the current folder
            directory_size.update({current_folder: directory_size[current_folder] + int(size)})
            if current_folder != "/":
                #If the current folder is not the root, go through each folder up and add the size of the current file
                for x in reversed(range(1, len(directory_list))):
                    print(f"Updating folder {directory_list[x]}")
                    directory_size.update({directory_list[x]: directory_size[directory_list[x]] + int(size)})
                print("Done")


print(directory_size)
for value in directory_size.values():
    if value <= 100000:
        result += value
print(f"Part 1 result: {result}")

#Part 2
total_space = 70000000
update_size = 30000000
space_needed = (total_space - update_size - directory_size[" /"]) * -1
for value in directory_size.values():
    if value > space_needed:
        part2_values.append(value)
part2_values.sort()
print(f"Part 2 solution: {part2_values[0]}")
