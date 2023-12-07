import card_utilities

CARD_LIST = [
	'A',
	'K',
	'Q',
	'T',
	'9',
	'8',
	'7',
	'6',
	'5',
	'4',
	'3',
	'2',
	'J'
]

def compare_hands(hand_1: list, hand_2: list) -> int:
	for i in range(5):
		value_hand_1 = hand_1[i] 
		value_hand_2 = hand_2[i]
		if (CARD_LIST.index(value_hand_1) < CARD_LIST.index(value_hand_2)):
			return (1)
		if (CARD_LIST.index(value_hand_1) > CARD_LIST.index(value_hand_2)):
			return (-1)
	return (0)

def sort_list_of_hands(list_of_hands: list) -> list:
	list_of_hands_len = len(list_of_hands)
	for i in range(list_of_hands_len):
		swapped = False
		for j in range(0, list_of_hands_len - i - 1):
			if compare_hands(list_of_hands[j], list_of_hands[j + 1]) == 1:
				temp = list_of_hands[j]
				list_of_hands[j] = list_of_hands[j + 1]
				list_of_hands[j + 1] = temp
				swapped = True
		if not swapped:
			break
	return (list_of_hands)

def get_best_hand_wildcard(hand: str) -> str:
	base_hand = hand
	base_hand_stripped = base_hand.replace('J', '')
	wildcard_count = len(base_hand) - len(base_hand_stripped)
	set_no_wildcard = set(base_hand_stripped)
	char_count_dict = {char: base_hand.count(char) for char in list(set_no_wildcard)}
	len_char_count_dict = len(char_count_dict)
	# Five of a kind
	if (hand == "JJJJJ"):
		return "JJJJJ"
	if (len_char_count_dict == 1):
		return_hand = base_hand.replace('J', list(set_no_wildcard)[0])
		return return_hand
	else:
		if (len_char_count_dict == 2):
			for key, value in char_count_dict.items():
				# Four of a kind
				if (value == 1):
					set_no_wildcard.remove(key)
					return_hand = base_hand.replace('J', list(set_no_wildcard)[0])
					return return_hand
			# Full house
			return_hand = base_hand.replace('J', list(set_no_wildcard)[0])
			return return_hand
		if (len_char_count_dict == 3):
			for key, value in char_count_dict.items():
				# Three of a kind
				if (value == 2):
					return_hand = base_hand.replace('J', key)
					return return_hand
			if (wildcard_count == 2):
				return_hand = base_hand.replace('J', list(set_no_wildcard)[0])
				return return_hand
		if (len_char_count_dict == 4):
			return_hand = base_hand.replace('J', list(set_no_wildcard)[0])
			return return_hand

print(get_best_hand_wildcard("KA6J4"))
print(get_best_hand_wildcard("JT43J"))
print(get_best_hand_wildcard("JJJJJ"))