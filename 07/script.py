import re
import functools

def is_n_of_a_kind(n, hand):
	uniques = set(hand)
	for c in uniques:
		if len(re.findall(c, hand)) == n:
			return True
	return False

def is_full_house(hand):
	uniques = set(hand)
	if len(uniques) != 2:
		return False
	count = len("".join(hand.split(hand[0])))
	if count == 2 or count == 3:
		return True
	else:
		return False

def is_two_pair(hand):
	uniques = set(hand)
	if len(uniques) == 3 and not is_n_of_a_kind(3, hand):
		return True
	return False

def evaluate_hand(hand):
	if is_n_of_a_kind(5, hand):
		return 6
	if is_n_of_a_kind(4, hand):
		return 5
	if is_full_house(hand):
		return 4
	if is_n_of_a_kind(3, hand):
		return 3
	if is_two_pair(hand):
		return 2
	if is_n_of_a_kind(2, hand):
		return 1
	return 0

def evaluate_card(card):
	if card.isnumeric():
		return int(card)
	if card == "T":
		return 10
	if card == "J":
		return 11
	if card == "Q":
		return 12
	if card == "K":
		return 13
	if card == "A":
		return 14

def compare_by_card(hand1, hand2):
	for cards in zip(hand1, hand2):
		if evaluate_card(cards[0]) > evaluate_card(cards[1]):
			return 1
		elif evaluate_card(cards[0]) < evaluate_card(cards[1]):
			return -1
	print(hand1, hand2)
	return 0

def compare_rank(hand1, hand2):
	hand1_value = evaluate_hand(hand1)
	hand2_value = evaluate_hand(hand2)
	if hand1_value > hand2_value:
		return 1
	elif hand1_value < hand2_value:
		return -1
	else:
		return compare_by_card(hand1, hand2)

def compare(line1, line2):
	return compare_rank(line1[0], line2[0])

lines = [line.split() for line in open("input", "r").read().split('\n')]
sortedlines = sorted(lines, key=functools.cmp_to_key(compare))

winnings = 0

for idx, line in enumerate(sortedlines):
	winnings += (idx + 1) * int(line[1])

print(winnings)