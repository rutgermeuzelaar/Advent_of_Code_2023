def is_five_of_a_kind(hand: list) -> bool:
	get_set = set(hand)
	len_set = len(get_set)
	if (len_set == 1):
		return (True)
	return (False)

def is_four_a_kind(hand: list) -> bool:
	get_set = set(hand)
	for char in get_set:
		char_count = hand.count(char)
		if (char_count == 4):
			return (True)
	return (False)

def is_full_house(hand: list) -> bool:
	get_set = set(hand)
	len_set = len(get_set)
	count_list = []
	if (len_set != 2):
		return (False)
	for char in get_set:
		char_count = hand.count(char)
		count_list.append(char_count)
	if (3 in count_list and 2 in count_list):
		return (True)
	return (False)

def is_three_of_a_kind(hand: list) -> bool:
	get_set = set(hand)
	len_set = len(get_set)
	count_list = []
	if (len_set != 3):
		return (False)
	for char in get_set:
		char_count = hand.count(char)
		count_list.append(char_count)
	if (3 in count_list):
		return (True)
	return (False)

def is_two_pair(hand: list) -> bool:
	get_set = set(hand)
	len_set = len(get_set)
	count_list = []
	if (len_set != 3):
		return (False)
	for char in get_set:
		char_count = hand.count(char)
		count_list.append(char_count)
	pair_count = count_list.count(2)
	if (pair_count == 2):
		return (True)
	return (False)

def is_one_pair(hand: list) -> bool:
	get_set = set(hand)
	len_set = len(get_set)
	count_list = []
	if (len_set != 4):
		return (False)
	for char in get_set:
		char_count = hand.count(char)
		count_list.append(char_count)
	pair_count = count_list.count(2)
	if (pair_count == 1):
		return (True)
	return (False)

def is_high_card(hand: list) -> bool:
	get_set = set(hand)
	len_set = len(get_set)
	if (len_set == 5):
		return (True)
	return (False)

def get_card_type(hand: list) -> dict:
	card_types = [
		"five_of_a_kind", 
		"four_of_a_kind", 
		"full_house", 
		"three_of_a_kind", 
		"two_pair", 
		"one_pair",
		"high_card"
	]
	card_type_dict = {card_type: False for card_type in card_types}
	if (is_five_of_a_kind(hand)):
		card_type_dict["five_of_a_kind"] = True
	if (is_four_a_kind(hand)):
		card_type_dict["four_of_a_kind"] = True
	if (is_full_house(hand)):
		card_type_dict["full_house"] = True
	if (is_three_of_a_kind(hand)):
		card_type_dict["three_of_a_kind"] = True
	if (is_two_pair(hand)):
		card_type_dict["two_pair"] = True
	if (is_one_pair(hand)):
		card_type_dict["one_pair"] = True
	if (is_high_card(hand)):
		card_type_dict["high_card"] = True
	value_list = list(card_type_dict.values())
	if (value_list.count(True) > 1):
		print("Illegal operator")
	return card_type_dict

