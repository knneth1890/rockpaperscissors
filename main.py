import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

items = [rock, paper, scissors]
userInput = int(
    input("Rock Paper Scissors, 1 = rock, 2 = paper and 3 = scissors\n")
)  #get the input of the user from items 0,1,2 which is rock paper and scissors respectively

if userInput >= 4 or userInput <= 0:
  print("you typed an invalid number"
        )  #this will check if the userchoice is valid
else:
  print("You Choose")
  print(items[userInput - 1])
  print("Computer Selects\n")
  itemposition = len(
      items
  )  # get the number of items inside the items(which is 3 (from 0,1,2))
  random_items = random.randint(0, itemposition - 1)  # randomize it
  print(items[random_items])  # print the item that has been randomize

  #### now time for the comparisons
  ##rock vs scissors and paper

  if userInput == 1 and random_items == 2:
    print("you win,you selected rock vs computer scissors")
  elif userInput == 1 and random_items == 0:
    print("Draw")
  ### paper vs scissor and rock
  elif userInput == 2 and random_items == 0:
    print("you win, you selected paper vs computer rock")
  elif userInput == 2 and random_items == 1:
    print("Draw")
  ### scissors vs paper and rock
  elif userInput == 3 and random_items == 1:
    print("you win, you selected scissors vs computer paper")
  elif userInput == 3 and random_items == 2:
    print("Draw")
  else:
    print("you lose")
