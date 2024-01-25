import random
import json
import matplotlib.pyplot as plt

choice = ["rock", "paper", "scissors", "spock", "lizard"]

win = {
    "rock": ["lizard", "scissors"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "spock": ["scissors", "rock"],
    "lizard": ["paper", "spock"]
}


def write_json():
    json_object = json.dumps(data, indent=4)

    with open("data.json", "w") as outfile:
        outfile.write(json_object)


def read_json():
    dictionary = json.load(open('data.json', 'r'))
    print(dictionary)
    return dictionary


data = read_json()


def check_won(choice1, choice2):
    if choice2 in win[choice1]:
        print("Computer won!")
    elif choice1 in win[choice2]:
        print("You won!")
        data[choice2] = data[choice2] + 1
    else:
        print("Nobody won?")


def graphic(dictionary):
    values = dictionary.values()
    labels = dictionary.keys()

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(labels, values, color='maroon',
            width=0.4)

    plt.xlabel("Auswahl")
    plt.ylabel("Number of rounds won")
    plt.title("Statistik der gewonnenen Spiele")
    plt.show()


if __name__ == '__main__':

    while True:
        # print(data)
        print("Do you want to play?")
        if input() == "No":
            graphic(read_json())
            break
        else:
            print("Please enter your choice (rock, paper, scissors, spock or lizard):")
            bot = random.choice(choice)
            player = input()
            if player in choice:
                check_won(bot, player)
                print("The bot chose:")
                print(bot)
                write_json()
            else:
                print("Please enter: rock, paper, scissors, spock or lizard!")
