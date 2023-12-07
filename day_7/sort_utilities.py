CARD_LIST = [
	'A',
	'K',
	'Q',
	'J',
	'T',
	'9',
	'8',
	'7',
	'6',
	'5',
	'4',
	'3',
	'2'
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