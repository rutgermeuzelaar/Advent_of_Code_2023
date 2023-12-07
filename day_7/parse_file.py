import card_utilities

def parse_file(filename: str):
	file = open(filename)
	return_dict = {}
	for line in file:
		line_split = line.split(" ")
		key = str(line_split[0])
		value = int(line_split[1])
		return_dict[key] = value
	return return_dict

def get_type_lists(filename: str):
	file = open(filename)
	five_of_a_kind_list = []
	four_of_a_kind_list = []
	full_house_list = []
	three_of_a_kind_list = []
	two_pair_list = []
	one_pair_list = []
	high_card_list = []
	for line in file:
		line_split = line.split(" ")
		hand = str(line_split[0])
		if (card_utilities.is_five_of_a_kind(hand)):
			five_of_a_kind_list.append(hand)
		if (card_utilities.is_four_a_kind(hand)):
			four_of_a_kind_list.append(hand)
		if (card_utilities.is_full_house(hand)):
			full_house_list.append(hand)
		if (card_utilities.is_three_of_a_kind(hand)):
			three_of_a_kind_list.append(hand)
		if (card_utilities.is_two_pair(hand)):
			two_pair_list.append(hand)
		if (card_utilities.is_one_pair(hand)):
			one_pair_list.append(hand)
		if (card_utilities.is_high_card(hand)):
			high_card_list.append(hand)
	return [high_card_list, one_pair_list, two_pair_list, three_of_a_kind_list, full_house_list, four_of_a_kind_list, five_of_a_kind_list]
