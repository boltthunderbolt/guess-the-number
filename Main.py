# Library
import random;
## Guess the number

myNumber = random.randint(0, 9); #using randint (random integer) and fill in the min and max number

askList = ["Can you guess it? 😁", "Do you wanna play with me? 🙂", "Lets play and beat me! 😎", "Can you beat me? 😏"];
wrongAnswerRespondList = ["No Problem. Just try again😉", "Oh... Come On 😔", "Its ok, choose the number again", "Try again until you get it!"];
correctAnswerRespondList = ["Yes... you get it 🥳", "Not bad 😉", "Nice 😁", "Congrats... 🎉💯"];

randomAsk = random.choice(askList);
print(f"Hi, what's up? i have a number in my Mind, just guess from 0 - 9. {randomAsk}");

while True:
  # Ditaruh disini supaya dapat kalimat jawaban benar dan salah secara random
  randomWrongAnswer = random.choice(wrongAnswerRespondList);
  randomCorrectAnswer = random.choice(correctAnswerRespondList);

  try:
    print("\n- Press ctrl + C for Quit");
    userInput = int(input("\nEnter here  -> ")); # user will put the number
    if userInput < 0 or userInput > 9:
      print("Please enter between 0 and 9");
    else:
      if userInput == myNumber:
        print(f"{randomCorrectAnswer}");
        break;
      elif myNumber > userInput:
        print(f"My number is greater than the number you entered. {randomWrongAnswer}", end="\n\n");
      else:
        print(f"My number is smaller than the number you entered. {randomWrongAnswer}", end="\n\n");
  except ValueError:
    print("Please enter type number!");
