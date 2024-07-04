# Library
import random;
import time;
## Guess the number

randomNumber = random.randint(0, 9); #using randint (random integer) and fill in the min and max number
startTime = time.time();
totalAnswer = 0;

askList = ["Can you guess it? 😁", "Do you wanna play with me? 🙂", "Lets play and beat me! 😎", "Can you beat me? 😏"];
wrongAnswerRespondList = ["No Problem. Just try again😉", "Oh... Come On 😔", "Its ok, choose the number again", "Try again until you get it!", "GG 😎"];
correctAnswerRespondList = ["Yes... you get it 🥳", "Not bad 😉", "Nice 😁", "Congrats... 🎉💯"];

randomAsk = random.choice(askList);
print(f"Hi, what's up? i have a number in my Mind, just guess from 0 - 9. {randomAsk}");

while True:
  # Ditaruh disini supaya dapat kalimat jawaban benar dan salah secara random
  randomWrongAnswer = random.choice(wrongAnswerRespondList);
  randomCorrectAnswer = random.choice(correctAnswerRespondList);

  try:
    print("\n- Press ctrl + C for Quit");
    userInput = int(input("Enter here  -> ")); # user will put the number
    totalAnswer += 1;
    if userInput < 0 or userInput > 9:
      print("Please enter between 0 and 9");
    else:
      if userInput == randomNumber:
        print(f"{randomCorrectAnswer}");
        if userInput == randomNumber:
          timeOver = time.time(); # catat waktu selesai menebak
          totalTime = timeOver - startTime;
          score = 10 - totalAnswer;
          print(f"Your time : {totalTime: .2f}");
          print(f"Your score : {score: .2f}");
        break;
      elif randomNumber > userInput:
        print(f"My number is greater than the number you entered. {randomWrongAnswer}", end="\n\n");
      else:
        print(f"My number is smaller than the number you entered. {randomWrongAnswer}", end="\n\n");
  except ValueError:
    print("Please enter type number!");
