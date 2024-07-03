# Library
import random;
## Guess the number

myNumber = random.randint(0, 9); #using randint (random integer) and fill in the min and max number
print("I have guess the number from 0 - 9. Can you guess it? 😶");

while True:
  userInput = int(input("\n Enter here\n-> ")); # user will put the number
  if userInput == myNumber:
    print("Congrats, you made it!");
    break;
  elif myNumber > userInput:
    print("My number is greater than the number you entered. Try Again! 😏", end="\n\n");
  else:
    print("My number is smaller than the number you entered. Try Again! 😏", end="\n\n");
