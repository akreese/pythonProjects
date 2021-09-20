import random 
retry = True
while retry:
  player1 = input("What is your weapon (Rock / Paper / Scissors): ").lower()
  computer = random.choice(["rock", "paper", "scissors"])
  if player1 == 'paper' and computer == 'paper':
    print("It's a tie! You and the computer both chose paper")
  elif player1 == 'rock' and computer == 'rock':
    print("It's a tie! You and the computer both chose rock")
  elif player1 == 'scissors' and computer == 'scissors':
    print("It's a tie! You and the computer both chose scissors")
  elif player1 == 'rock' and computer == 'paper':
    print("Maybe next time! The computer chose paper")
  elif player1 == 'rock' and computer == 'scissors':
    print("YAY! you won! The computer chose scissors")
  elif player1 == 'paper' and computer == 'rock':
    print("YAY! you won! The computer chose rock")
  elif player1 == 'paper' and computer == 'scissors':
    print("Maybe next time! The computer chose scissors")
  elif player1 == 'scissors' and computer == 'rock':
    print("Maybe next time! The computer chose rock")
  elif player1 == 'scissors' and computer == 'paper':
    print("YAY! you won! The computer chose paper")

  new_game = str(input("Do you want to play again? (y/n) "))
  if new_game.lower() == "y":
    continue
  else:
    break
