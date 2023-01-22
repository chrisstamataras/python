import random
from replit import clear
def deal_card():
  """Returns a random card from the deck."""
  cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  r_card=cards[random.randint(0, 12)]
  return r_card

def calculate_score(cards):
  
  if sum(cards) == 21 and len(cards) == 2 :
    return 0
  if 11 in cards and sum(cards) > 21 :
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score :
    return "it's a draw"
  elif computer_score == 0 :
    return "Lose, opponent has Blackjack"
  elif user_score == 0 :
    return "Win with a blackjack"
  elif user_score > 21 :
    return "You went over 21. You lose"
  elif computer_score > 21 :
    return "Opponent went over 21. You win"
  elif user_score > computer_score:
    return "You win"
  else :
    return "You lose"
def play_game() :
  user_cards=[]
  computer_cards=[]
  is_game_over = False
  user_cards.append(deal_card())
  user_cards.append(deal_card())
  computer_cards.append(deal_card())
  computer_cards.append(deal_card())
  while is_game_over == False :
    user_score =calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")
    if user_score == 0 or computer_score == 0 or user_score > 21 :
      is_game_over = True
    else: 
      anser=input("Do you want to draw another card? Tipe 'y' or 'n' ")
      if anser == "y":
        user_cards.append(deal_card())  
      else:
        is_game_over = True
  while computer_score < 17 and computer_score != 0:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  print(f"   You'r final hand: {user_cards}, final score: {user_score}")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play_game()