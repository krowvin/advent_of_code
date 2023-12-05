# 12/04/2023
# Start: 8:28PM -06:00
# End  :  9:05PM -06:00
# /u/krowvin
# https://adventofcode.com/2023/day/4

import sys

# Enable extra output
DEBUG = False
INPUT_FILE = "input.txt"

# Run test_input.txt and see if you get the expected 13
# PASS


# Import the file data
def readInputFile(filename):
    print(f"Reading {filename}...")
    with open(filename) as input_file:
        lines = input_file.readlines()
        print(f"\nFound {len(lines)} cards!")
        return lines

def readCard(row):
    # parse the table into a usable object
    card = {}
    line = " ".join(row.split())
    card_num, numbers = line.split(": ")
    try:
        card["number"] = int(card_num.lower().split("card ")[1])
    except ValueError:
        print("Invalid Card Number:\nLine:", line)
        sys.exit()
    card["winning"], card["have"] = numbers.split(" | ")
    card["winning"] = list(map(int, card["winning"].split(" ")))
    card["have"] = list(map(int, card["have"].split(" ")))
    return card

def calculateCard(card_data):
    if DEBUG: print("="*11)
    multi = 0
    card_count = 0
    for num in card_data["have"]:
        if num in card_data["winning"]:
            # Each match after the first 
            #   doubles the point value of that card.
            multi = 1 if not card_count else multi*2
            if DEBUG: print(f"num: {num}, mult: {multi}")
            card_count += 1
    card_data["score"] = multi
    if DEBUG: print(f"Card {card_data['number']}: {multi}")
    return card_data

# calculate the final score
# Start
def run():
    cards = readInputFile(INPUT_FILE)
    total_score = 0
    total_cards = 0
    total_have  = 0
    if DEBUG: print(cards)
    for card in cards:
        card_data = calculateCard(readCard(card))
        total_score += card_data["score"]
        total_cards += len(card_data["have"])
        total_have += len(card_data["winning"])
    print(f"""
    Out of ({total_cards}) scores across ({len(cards)}) cards, 
        ({total_have}) were winners!\n
    \nFinal Score: {total_score}\n
    """)
    
if __name__ == "__main__":
    run()
