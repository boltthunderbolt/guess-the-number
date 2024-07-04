# Library
import random;
import time;

## Game
## Guess the number

levelsOfRandomNumber = { 
  'beginner': (0, 5),
  'easy': (0, 10),
  'normal': (0, 20),
  'hard': (0, 50),
  'impossible': (0, 100)
}

def showLevelList():
  print("Choose the level you want to play:");
  for index, level in enumerate(levelsOfRandomNumber.keys(), start=1):
    print(f"{index}. {level.capitalize()}");

# Ask user to choose level
showLevelList();
while True:
  try:
    userChooseLevel = int(input("=====================\n\nEnter here\n-> "));
    if 1 <= userChooseLevel <= len(levelsOfRandomNumber):
      break;
    else:
      print("Please select the available level, by entering the correct number");
  except ValueError:
    print("Please select the available level, by entering the correct number");

# Takes the number of guessed numbers according to the level selected by the user
selectedLevelByUser = list(levelsOfRandomNumber.keys())[userChooseLevel - 1];
print(f"Level selected : {selectedLevelByUser.capitalize()}")
firstNumber, endNumber = levelsOfRandomNumber[selectedLevelByUser];

# Generate random number within spesific range
randomNumber = random.randint(firstNumber, endNumber); # getting from selected level by user
startTime = time.time();
totalWrongAnswer = 0;

askList = ["Can you guess it? 😁", "Do you wanna play with me? 🙂", "Lets play and beat me! 😎", "Can you beat me? 😏"];
wrongAnswerRespondList = ["No Problem. Just try again😉", "Oh... Come On 😔", "Its ok, choose the number again", "Try again until you get it!"];
correctAnswerRespondList = ["Yes... you get it 🥳", "Not bad 😉", "Nice 😁", "Congrats... 🎉💯", "GG 😎", "Well played..."];
askPlayerToPlayAgainList = ["Wanna play again?", "Wanna try another level?"];

randomAsk = random.choice(askList);
print(f"==============\n\nHi, what's up? i have a number in my Mind, just guess from {firstNumber} - {endNumber}. {randomAsk}");

while True:
  # Random wrong and correct answer responds required to put in while loop
  randomWrongAnswer = random.choice(wrongAnswerRespondList);
  randomCorrectAnswer = random.choice(correctAnswerRespondList);
  askPlayerToPlayAgain = random.choice(askPlayerToPlayAgainList);

  try:
    print(f"Guess the number out of {firstNumber} - {endNumber}");
    userInput = int(input("Enter here  -> ")); # user will put the number here
    if userInput == randomNumber or userInput < firstNumber or userInput > endNumber or userInput == '':
      '''
      - If user successfully guesses the number in one try,
      - If user enters a number outside the range limits
      '''
      totalWrongAnswer; # scores will not be reduced by this mistake
    else:
      totalWrongAnswer += 5; # Every user input the wrong answer
    
    if userInput < firstNumber or userInput > endNumber:
      print(f"Please enter between {firstNumber} and {endNumber}");
    else:
      if userInput == randomNumber:
        print(f"{randomCorrectAnswer}. {askPlayerToPlayAgain}", end="\n\n");
        if userInput == randomNumber:
          timeOver = time.time(); # The time is recorded until the user succeeds in guessing the number correctly
          totalTime = timeOver - startTime;
          score = 100 - totalWrongAnswer; # sThe score results are determined by how many times the user enters wrong answer input
          print(f"Your time : {totalTime: .2f}");
          print(f"Your score : {score: .2f}");
        break;
      elif randomNumber > userInput:
        print(f"My number is greater than the number you entered. {randomWrongAnswer}", end="\n\n");
      else:
        print(f"My number is smaller than the number you entered. {randomWrongAnswer}", end="\n\n");
  except ValueError:
    print("Please enter type number!");