import random


def roll():
    roll = random.randint(1, 6)
    return roll


while True:
    try:
        players = int(input('Enter the number of players (1-4): '))
        if 2 <= players <= 4:
            break
        else:
            print('Invalid number. Must be between (2-4) players.')
    except ValueError:
        print("Invalid input. Must enter number between (2-4)")

#print(players) so that code runs

max_score = 25
player_scores = [0 for _ in range(players)]

#print(players_scores) to set scores at 0 por each player

while max(player_scores) < max_score:

    for idx in range(players):
        print(f"Player {idx + 1}, turn has just started! ")
        print("Your total score is:", player_scores[idx])
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y/n)?: ").lower()
            if should_roll != 'y':
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done.")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
            print("Your score is:", current_score)

        player_scores[idx] += current_score
        print("Your total score is:", player_scores[idx])

max_score = max(player_scores)
winner_idx = player_scores.index(max_score)
print("PLayer", winner_idx + 1, "is a winner with a score of:", max_score)

