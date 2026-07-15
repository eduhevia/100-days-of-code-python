from art import logo
print(logo)

def find_highest_bid(bids_dictionary):
    highest_bid_amount = 0.0
    winner = ""

    for bidder in bids_dictionary:
        current_bid_price = bids_dictionary[bidder]
        if current_bid_price > highest_bid_amount:
            winner = bidder
            highest_bid_amount = current_bid_price

    print(f"The winner is {winner} with a bid of ${highest_bid_amount:.2f}.")


bids = {}
continue_bidding = True

while continue_bidding:
    name = input("What is your name?: ")
    price = float(input("What is your bid?: $"))
    bids[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower().strip()

    if should_continue == "no":
        continue_bidding = False
    elif should_continue == "yes":
        print("\n" * 100)


find_highest_bid(bids_dictionary=bids)
