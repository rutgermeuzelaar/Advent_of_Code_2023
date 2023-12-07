validation_dict = {"red": 12,
				   "green": 13,
				   "blue": 14}

def read_file(filename: str):
	file = open(filename)
	sum = 0
	for line in file:
		sum += power_min_num_cubes(get_min_num_cubes(get_game_records(line)))
	return (sum)

def power_min_num_cubes(min_num_cubes: dict) -> int:
	power = 0
	for value in min_num_cubes.values():
		if not power:
			power = value
		else:
			power *= value
	return (power)

def get_game_num(line: str) -> int:
	i = 0
	digit = []
	digit_joined = []
	digit_found = False
	while (i < len(line)):
		while (line[i].isdigit()):
			digit.append(line[i])
			digit_found = True
			i += 1
		if (digit_found):
			digit_joined = ''.join(digit)
			return (int(digit_joined))
		i += 1

def get_game_records(line: str) -> list:
	color_list = ["red", "green", "blue"]
	sum_dict = {color: 0 for color in color_list}
	digit_list = []
	list_of_record_dicts = []
	i = 0
	digit_position = 1
	while (i < len(line)):
		digit = []
		digit_switch = False
		while (line[i].isdigit()):
			digit_switch = True
			digit.append(line[i])
			i += 1
		if (digit_switch):
			digit_joined = ''.join(digit)
			digit_list.append(digit_joined)
			continue
		for key in sum_dict.keys():
			if (line[i:].startswith(key)):
				sum_dict[key] = int(digit_list[digit_position])
				digit_position += 1
		if (line[i] == ';'):
			list_of_record_dicts.append(sum_dict)
			sum_dict = sum_dict.fromkeys(sum_dict, 0)
		i += 1
	list_of_record_dicts.append(sum_dict)
	return (list_of_record_dicts)

def validate_game(game_record: dict, check_dict: dict) -> bool:
	for key, value in check_dict.items():
		get_result = game_record.get(key)
		if (get_result != None and get_result > value):
			return (False)
	return (True)

def get_min_num_cubes(game_records: list):
	color_list = ["red", "green", "blue"]
	sum_dict = {color: 0 for color in color_list}
	for dict in game_records:
		for key in sum_dict.keys():
			if dict[key] > sum_dict[key]:
				sum_dict[key] = dict[key]
	return (sum_dict)

# print(read_file("input"))
print(power_min_num_cubes(get_min_num_cubes(get_game_records("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"))))
print(get_game_num("Game 785176: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"))
print(read_file("input"))
# print(validate_game(test_dict, validation_dict))