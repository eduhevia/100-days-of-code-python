import random
from art import logo


def deal_card(computer_or_user):
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    computer_or_user.append(random.choice(cards))


def calculate_score(hand):
    """Take a list of cards and return the score calculated from the cards"""
    if 11 in hand and sum(hand) > 21:
        hand[hand.index(11)] = 1

    if sum(hand) == 21 and len(hand) == 2:
        return 0

    return sum(hand)


def compare(computer_total, user_total):
    """Compares the user score u_score against the computer score c_score."""
    if computer_total == user_total:
        return "Draw 🙃"
    elif computer_total == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_total == 0:
        return "Win with a Blackjack 😎"
    elif user_total > 21:
        return "You went over. You lose 😭"
    elif computer_total > 21:
        return "Opponent went over. You win 😁"
    else:
        if user_total > computer_total:
            return "You win 😃"
        else:
            return "You lose 😤"


def play_game():
    print(logo)
    user = []
    computer = []
    game_over = False

    for _ in range(2):
        deal_card(user)
        deal_card(computer)

    user_total = calculate_score(user)
    computer_total = calculate_score(computer)

    while not game_over and user_total < 21 and user_total != 0:
        print(f"    Your hand: {user}, score: {user_total}")
        print(f"    Computer's first card: {computer[0]}")
        want_card = input("Type 'y' to get another card, type 'n' to pass: ").lower().strip()

        if want_card == "y":
            deal_card(user)
            user_total = calculate_score(user)
        else:
            game_over = True

    while computer_total != 0 and computer_total < 17 and user_total <= 21:
        deal_card(computer)
        computer_total = calculate_score(computer)

    print(f"Your final hand: {user}, final score: {user_total}")
    print(f"Computer's final hand: {computer}, final score: {computer_total}")
    print(compare(computer_total, user_total))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower().strip() == "y":
    print("\n" * 20)
    play_game()
