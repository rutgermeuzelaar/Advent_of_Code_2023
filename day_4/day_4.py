def convert_string(line: str) -> list:
	winning_numbers = []
	current_numbers = []
	split_list = line.split('|')
	line_index = 0
	char_index = 0
	split_list_len = len(split_list)
	while (line_index < split_list_len):
		line_len = len(split_list[line_index])
		while (char_index < line_len):
			num = []
			while (split_list[line_index][char_index].isdigit()):
				num.append(split_list[line_index][char_index])
				if (char_index == line_len - 1):
					break
				char_index += 1
			if (num):
				num_joined = ''.join(num)
				if (line_index == 0):
					winning_numbers.append(int(num_joined))
				if (line_index == 1):
					current_numbers.append(int(num_joined))
			char_index += 1
		char_index = 0
		line_index += 1
	winning_numbers = winning_numbers[1:]
	return ([winning_numbers, current_numbers])

def calculate_points(scores: list) -> int:
	found_counter = 0
	current_score = 0
	for score in scores[1]:
		if score in scores[0]:
			found_counter += 1
	while (found_counter):
		if (current_score == 0):
			current_score = 1
		else:
			current_score *= 2
		found_counter -= 1
	return (current_score)

def solve_file(filename: str) -> int:
	file = open(filename)
	num_list = []
	for line in file:
		num_list.append(calculate_points(convert_string(line)))
	return (sum(num_list))

# recursive?
# print(convert_string("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"))
# print(calculate_points(convert_string("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")))
# print(solve_file("input"))