#Part 1

def create_crates():
    """Get the crates data from the crates.txt"""
    crate_1 = []
    crate_2 = []
    crate_3 = []
    crate_4 = []
    crate_5 = []
    crate_6 = []
    crate_7 = []
    crate_8 = []
    crate_9 = []
    with open('crates.txt') as part1_crates:
        lines = part1_crates.readlines()
        for line in lines:
            for x in range(1, len(line)):
                if line[x].isalpha():
                    match x:
                        case 1: crate_1.append(line[x])
                        case 5: crate_2.append(line[x])
                        case 9: crate_3.append(line[x])
                        case 13: crate_4.append(line[x])
                        case 17: crate_5.append(line[x])
                        case 21: crate_6.append(line[x])
                        case 25: crate_7.append(line[x])
                        case 29: crate_8.append(line[x])
                        case 33: crate_9.append(line[x])
    return crate_1, crate_2, crate_3, crate_4, crate_5, crate_6, crate_7, crate_8, crate_9


def movement_steps(part):
    """Go through the input steps and move the crates"""
    crate_1, crate_2, crate_3, crate_4, crate_5, crate_6, crate_7, crate_8, crate_9 = create_crates()
    with open("input.txt") as movement_data:
        lines = movement_data.readlines()
        for line in lines:
            line = line.split(" ")
            from_crate = int(line[3])
            to_crate = int(line[5].strip())
            amount = int(line[1])
            print(f"Need to move {amount} crates from crate {from_crate} to crate {to_crate}")

            if part == 1:
                for x in range(amount):
                    match from_crate:
                        case 1: result = crate_1.pop(0)
                        case 2: result = crate_2.pop(0)
                        case 3: result = crate_3.pop(0)
                        case 4: result = crate_4.pop(0)
                        case 5: result = crate_5.pop(0)
                        case 6: result = crate_6.pop(0)
                        case 7: result = crate_7.pop(0)
                        case 8: result = crate_8.pop(0)
                        case 9: result = crate_9.pop(0)
                    match to_crate:
                        case 1: crate_1.insert(0, result)
                        case 2: crate_2.insert(0, result)
                        case 3: crate_3.insert(0, result)
                        case 4: crate_4.insert(0, result)
                        case 5: crate_5.insert(0, result)
                        case 6: crate_6.insert(0, result)
                        case 7: crate_7.insert(0, result)
                        case 8: crate_8.insert(0, result)
                        case 9: crate_9.insert(0, result)

            elif part == 2:
                match from_crate:
                    case 1:
                        result = crate_1[0:amount]
                        del crate_1[0:amount]
                    case 2:
                        result = crate_2[0:amount]
                        del crate_2[0:amount]
                    case 3:
                        result = crate_3[0:amount]
                        del crate_3[0:amount]
                    case 4:
                        result = crate_4[0:amount]
                        del crate_4[0:amount]
                    case 5:
                        result = crate_5[0:amount]
                        del crate_5[0:amount]
                    case 6:
                        result = crate_6[0:amount]
                        del crate_6[0:amount]
                    case 7:
                        result = crate_7[0:amount]
                        del crate_7[0:amount]
                    case 8:
                        result = crate_8[0:amount]
                        del crate_8[0:amount]
                    case 9:
                        result = crate_9[0:amount]
                        del crate_9[0:amount]

                for x in reversed(range(len(result))):
                    match to_crate:
                        case 1: crate_1.insert(0, result[x])
                        case 2: crate_2.insert(0, result[x])
                        case 3: crate_3.insert(0, result[x])
                        case 4: crate_4.insert(0, result[x])
                        case 5: crate_5.insert(0, result[x])
                        case 6: crate_6.insert(0, result[x])
                        case 7: crate_7.insert(0, result[x])
                        case 8: crate_8.insert(0, result[x])
                        case 9: crate_9.insert(0, result[x])

            else:
                print("Invalid part")

    print(crate_1[0] + crate_2[0] + crate_3[0] + crate_4[0] + crate_5[0] + crate_6[0] + crate_7[0] + crate_8[0] + crate_9[0])


movement_steps(part=1)

#Part 2
#Crates are moved in batches now

movement_steps(part=2)



