import random

player = {"score": 0, "choice":"", "name":"Player"}
cpu = {"score":0, "choice":'', "name":"CPU"}
match = [player, cpu]
matches_played = 0

def get_player_choice():
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    
    if choice == 'rock':
        print_rock()
    elif choice == 'paper':
        print_paper()
    else:
        print_scissors()

    return choice

def get_cpu_choice():
    choice = random.choice(['rock', 'paper', 'scissors'])

    if choice == 'rock':
        print_rock()
    elif choice == 'paper':
        print_paper()
    else:
        print_scissors()

    return choice

def determine_winner(player_choice, cpu_choice):
    if player_choice == cpu_choice:
        return 'tie'
    elif (player_choice == 'rock' and cpu_choice == 'scissors') or \
         (player_choice == 'paper' and cpu_choice == 'rock') or \
         (player_choice == 'scissors' and cpu_choice == 'paper'):
        return 'player'
    else:
        return 'cpu'

def play_round():
    global matches_played
    match[0]['choice'] = get_player_choice()
    match[1]['choice'] = get_cpu_choice()
    print(f"CPU chose: {match[1]['choice']}")
    
    winner = determine_winner(match[0]['choice'], match[1]['choice'])
    
    if winner == 'player':
        match[0]['score'] += 1
        print("You win this round!")
    elif winner == 'cpu':
        match[1]['score'] += 1
        print("CPU wins this round!")
    else:
        print("This round is a tie!")
    
    matches_played += 1
    print(f"Score - You: {match[0]['score']} | CPU: {match[1]['score']} | Matches Played: {matches_played}")

def print_paper():
    print("""
       _______
    ---'   ___)_____
              ______)
            _________)
          (_________)
    ---.__(_______)

    """)

def print_rock():
    print("""
       _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

def print_scissors():
    print("""
       _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

def main():
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        play_round()
        again = input("Do you want to play another round? (yes/no): ").lower()
        if again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
