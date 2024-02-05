import os
import re

#HINT: You can call clear() to clear the output in the console.

# from art import logo


# print(logo)


def get_bid():
    bidder_name = input("What is your name?: ").capitalize()
    bid_amount = input("What is your bid?: ")
    filtered_bid = re.sub(r'[^\d.]', '', bid_amount)
    bid_amount = filtered_bid
    return bidder_name, bid_amount

bidder_name, bid_amount = get_bid()



biders = {}

biders[bidder_name] = bid_amount

new_bider = input("Is there any other bidders? (yes/no) ")

while new_bider == "yes":
    os.system('clear')
    bidder_name, bid_amount = get_bid()
    biders[bidder_name] = bid_amount
    new_bider = input("Is there any other bidders? (yes/no) ")

max_bid = 0
max_biders_name = ""

for bider in biders:
  if int(biders[bider]) > max_bid:
    max_bid = int(biders[bider])
    max_biders_name = bider

print(f"The winner is {max_biders_name} with a bid of {max_bid}")