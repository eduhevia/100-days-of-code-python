import random
from game_data import data
from art import logo, vs


def check_answer(guess, compare_a, compare_b):
    if compare_a['follower_count'] > compare_b['follower_count']:
        winner = "a"
    else:
        winner = "b"
    if guess == winner:
        return True
    else:
        return False


def format_data(account):
    return f"{account['name']}, a {account['description']}, from {account['country']}."


def play_game():
    current_score = 0
    game_over = False

    print(logo)
    compare_a = random.choice(data)

    while not game_over:
        compare_b = random.choice(data)

        while compare_a == compare_b:
            compare_b = random.choice(data)

        print(f"\nCompare A: {format_data(compare_a)}.")
        print(vs)
        print(f"Compare B: {format_data(compare_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower().strip()
        correct_answer = check_answer(guess, compare_a, compare_b)

        if correct_answer:
            current_score += 1
            print("\n" * 30, logo)
            print(f"You're right! Current score: {current_score}")
        else:
            print("\n" * 30, logo)
            print(f"Sorry, that's wrong. Final score: {current_score}")
            game_over = True

        compare_a = compare_b


play_game()
