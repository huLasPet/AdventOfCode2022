#A for Rock, B for Paper, and C for Scissors - enemy
#X for Rock, Y for Paper, and Z for Scissors - own
#Scores are 1 for Rock, 2 for Paper, and 3 for Scissors
#plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won

score = 0
rock = 1
paper = 2
scissors = 3
win = 6
draw = 3
loss = 0

with open('input.txt') as input_data:
    for line in input_data:
        match line[0]:
            #Rock by the enemy
            case "A":
                match line[2]:
                    case "X":
                        score += draw + rock
                    case "Y":
                        score += win + paper
                    case "Z":
                        score += loss + scissors
            #Paper by the enemy
            case "B":
                match line[2]:
                    case "X":
                        score += loss + rock
                    case "Y":
                        score += draw + paper
                    case "Z":
                        score += win + scissors
            #Scissors by the enemy
            case "C":
                match line[2]:
                    case "X":
                        score += win + rock
                    case "Y":
                        score += loss + paper
                    case "Z":
                        score += draw + scissors

print(f"The score is {score} for part 1")

#Part 2
#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win

score = 0

with open('input.txt') as input_data:
    for line in input_data:
        match line[0]:
            #Rock by the enemy
            case "A":
                match line[2]:
                    case "X":
                        score += loss + scissors
                    case "Y":
                        score += draw + rock
                    case "Z":
                        score += win + paper
            #Paper by the enemy
            case "B":
                match line[2]:
                    case "X":
                        score += loss + rock
                    case "Y":
                        score += draw + paper
                    case "Z":
                        score += win + scissors
            #Scissors by the enemy
            case "C":
                match line[2]:
                    case "X":
                        score += loss + paper
                    case "Y":
                        score += draw + scissors
                    case "Z":
                        score += win + rock

print(f"The score is {score} for part 2")

