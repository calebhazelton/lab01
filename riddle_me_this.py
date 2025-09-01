"""A simple riddle game that loads riddles from a JSON file and prompts the user to answer them.
Tracks the player's score and allows exiting the game by typing 'exit'."""

import json

class Riddle:
    """Represents a riddle with its question and answer."""
    def __init__(self, string1, string2):
        """Initialize a Riddle object."""
        self.riddle = string1
        self.answer = string2

    def getRiddle(self):
        """Returns the riddle question (string)."""
        return self.riddle

    def getAnswer(self):
        """Returns the riddle answer (string)."""
        return self.answer
    
# Load riddles from riddles.json
riddleList = []
with open('riddles.json', 'r') as file:
    riddles_data = json.load(file)
    for item in riddles_data:
        riddleList.append(Riddle(item['riddle'], item['answer']))

#Create variable to keep track of the player's score
playerScore = 0

gameLoop = True
while gameLoop == True:

    for i in range(0, len(riddleList)):
        activeRiddle = riddleList[i]
        print("\nHere is a riddle:\n", activeRiddle.getRiddle(), "\ntype exit to quit\n")
        answer = input("Answer: ").lower()

        possible_answers = [ans.strip().lower() for ans in activeRiddle.answer.split(';')]

        if answer in possible_answers:
            playerScore += 1
            print("\n\nCorrect!\nYou've answered ", playerScore, " correct riddles.\n")

        elif answer == "exit":
            gameLoop = False
            break

        else:
            print("\nWrong answer.")
            print("The correct answer was:", activeRiddle.getAnswer().split(';')[0], "\n")

    print("\nGame over! You answered ", playerScore, " riddles correctly.\n")
    print("Thanks for playing!")

    gameLoop


