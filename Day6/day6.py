#Part1 - start of signal if last 4 characters are all different
#Part2 - start of message if last 14 characters are all different
#Need the position of where that starts

def count_characters(part):
    datastream = []
    char_count = 0
    if part == 1:
        length = 3
        list_length = -4
    else:
        length = 13
        list_length = -14

    with open("input.txt") as input_data:
        letters = input_data.readlines()
        for letter in letters[0]:
            datastream.append(letter)
            if char_count >= length:
                #If the set length and list length are the same it has no duplicates
                if len(set(datastream[list_length:])) == len(datastream[list_length:]):
                    print(f"Marker found: {datastream[list_length:]} at {len(datastream)}")
                    break
            else:
                char_count += 1


count_characters(1)
count_characters(2)
