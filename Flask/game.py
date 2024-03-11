import random
import json
import requests
import matplotlib.pyplot as plt


data = {"rock": 0, "paper": 0, "scissors": 0, "spock": 0, "lizard": 0}
choices = {"rock": 0, "paper": 1, "scissors": 2, "spock": 3, "lizard": 4}

# Game Rules
win = {
    "rock": ["lizard", "scissors"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "spock": ["scissors", "rock"],
    "lizard": ["paper", "spock"]
}


def check_won(choiceU, choiceC):
    if choiceC in win[choiceU]:
        return "user"
    elif choiceU in win[choiceC]:
        return "computer"
    else:
        return "tie"


def get_user_choice():
    print("Choose rock, paper, scissors, spock, or lizard:")

    choice = input().lower()

    if choice in choices:
        data[choice] += 1
        return choice
    else:
        print("Invalid choice. Please try again.")
        return get_user_choice()


def get_computer_choice():
    choice = random.choice(list(choices.keys()))
    return choice


def write_json():
    json_object = json.dumps(choices, indent=4)

    with open("data.json", "w") as outfile:
        outfile.write(json_object)


def graphic(dictionary):
    values = dictionary.values()
    labels = dictionary.keys()

    fig = plt.figure(figsize=(10, 5))

    plt.bar(labels, values, color='maroon',
            width=0.4)

    plt.xlabel("Pick by user")
    plt.ylabel("Number of picks by user")
    plt.title("Choice statistic by user")
    plt.show()


def main():
    print("Welcome to Rock, Paper, Scissors, Spock, Lizard!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"User chose {user_choice} and computer chose {computer_choice}.")
        winner = check_won(user_choice, computer_choice)

        if winner == "user":
            print("User wins!")
        elif winner == "computer":
            print("Computer wins!")
        else:
            print("It's a tie!")

        play_again = input("Do you want to play again? (y/n):").lower()

        if play_again != "y":
            # break Stop the program
            write_json()
            print("Spiel beendet")
            break


if __name__ == '__main__':
    main()
    mydata = json.load(open('data.json', 'r'))
    #headers = {'Content-Type': 'application/json'}
    res = requests.post("http://127.0.0.1:5000/post_json", data=mydata)
    graphic(data)
