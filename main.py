import random

player_score = 0
ai_score = 0
pizza_count = 0
turn_count = 1
turn_score = 0

def roll():    
    global turn_count
    global turn_score
    print(f'turn {turn_count}')
    picked_roll = input('Roll?y/n \n')
    if picked_roll == 'y':
        human_roll()
    elif picked_roll == 'n':
        print('no')
        turn_score = 0
        turn_count += 1
        if turn_count < 4:
            roll()
        else: 
            print(f"Game Over! Your score is {player_score}")
    elif picked_roll.lower() == 'pizza':
        global pizza_count
        pizza_count = pizza_count + 1
        print(pizza_count)
        roll()
    elif picked_roll == 'end':
        print(f'your total score is {player_score}, bye!')
    else:
        roll()

def human_roll():
    global player_score
    global turn_score
    global turn_count
    roll_num = random.randint(1, 6)

    if roll_num == 1:
        print('Oh no! You go oinked! Rolled a 1, all points this turn are lost, turn over')
        player_score -= turn_score
        turn_count += 1
        print(f'your score is {player_score}')
        roll()
    else:
        print(f'your roll is {roll_num}')
        player_score += roll_num
        turn_score += roll_num
        print(f'your score is {player_score}')
        roll()

def main():
    roll()

main()
# if __name__ == "__main__":
#     main()