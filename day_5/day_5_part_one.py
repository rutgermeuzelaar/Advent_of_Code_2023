import timeit

def get_map_line_list(line: str) -> dict:
	map_line = line.split(" ")
	range_dict = {"dest_range_start": int(map_line[0]), "source_range_start": int(map_line[1]), "range_length": int(map_line[2])}
	return (range_dict)

def number_in_range(number: int, range_dict: dict) -> int:
	source_range_start = range_dict.get("source_range_start")
	dest_range_start = range_dict.get("dest_range_start")
	range_length = range_dict.get("range_length")
	source_range_end = source_range_start + range_length
	dest_range_end = dest_range_start + range_length
	if (number >= source_range_start and number < source_range_end):
		offset = source_range_end - number
		return(dest_range_end - offset)
	return (-1)

def check_for_digit(line: str) -> bool:
	for i in range(len(line)):
		if (line[i].isdigit()):
			return (True)
	return (False)

def convert_file_to_list(filename: str) -> list:
	converted_file = []
	file = open(filename)
	for line in file:
		converted_file.append(line)
	return (converted_file)

def get_seeds(file_as_list: list) -> dict:
	seeds = file_as_list[0]
	seeds = str(seeds).split(" ")
	seeds = {int(seed): 0 for seed in seeds[1:]}
	return (seeds)

def seed_not_found(conversion_dict: dict, range_dict: dict) -> dict:
	for key, value in conversion_dict.items():
		if (value == 0):
			conversion_dict[key] = key
	return (conversion_dict)

def get_dicts_file(filename: str) -> list:
	file_as_list = convert_file_to_list(filename)
	initial_dict = get_seeds(file_as_list)
	file_as_list = file_as_list[2:]
	file_as_list.append("volatile")
	list_w_dicts = []
	num_maps_crossed = 0
	append_list = []
	list_w_dicts.append(initial_dict)
	for i in file_as_list:
		if (i == '\n'):
			continue
		elif (not(check_for_digit(i))):
			num_maps_crossed += 1
			if (num_maps_crossed == 1):
				continue
			if (num_maps_crossed == 2):
				new_dict = fill_dict(append_list, initial_dict, True)
				append_list = []
			else:
				new_dict = fill_dict(append_list, list_w_dicts[num_maps_crossed - 2], False)
				append_list = []
			list_w_dicts.append(new_dict)
		else:
			append_list.append(i)
	return(list_w_dicts)

def fill_dict(map_line: list, previous_dict: dict, switch: bool) -> dict:
	count_seed_dict = {}
	if (switch):
		count_seed_dict = {position: 0 for position in previous_dict.keys()}
	else:
		count_seed_dict = {position: 0 for position in previous_dict.values()}
	for line in map_line:
		map_line_range_dict = get_map_line_list(line)
		for key in count_seed_dict:
			number_found = number_in_range(key, map_line_range_dict)
			if (number_found != -1):
				count_seed_dict[key] = number_found
	count_seed_dict = seed_not_found(count_seed_dict)
	return (count_seed_dict)

def get_location(seed: int, list_with_dicts: list, index: int) -> int:
	max_len = len(list_with_dicts)
	if (index == max_len - 1):
		return (seed)
	if (index == 0):
		current_dict = list_with_dicts[index]
		next_value = seed
	else:
		current_dict = list_with_dicts[index]
		next_value = current_dict.get(seed)
	return (get_location(next_value, list_with_dicts, index + 1))

def get_location_dict(seed_list: list, list_with_dicts: list, file_as_list: list) -> dict:
	location_dict = get_seeds(file_as_list)
	for key in location_dict.keys():
		location_dict[key] = get_location(key, list_with_dicts, 0)
	return (location_dict)

def solve(filename: str):
	file_as_list = convert_file_to_list(filename)
	dicts_file = get_dicts_file(filename)
	seed_list = get_seeds(file_as_list)
	location_dict = get_location_dict(seed_list, dicts_file, file_as_list)
	is_lowest = 0
	is_first = True
	for value in location_dict.values():
		if (is_first):
			is_lowest = value
			is_first = False
		else:
			if (value < is_lowest):
				is_lowest = value
	return (is_lowest)

map_line = get_map_line_list("52 50 48")
tests = [[0, 1], [48, 49, 50, 51], [96, 97, 98, 99]]
for test in tests:
	for number in test:
		
print(number_in_range(98, map_line))
# start_time = timeit.default_timer()
# # print(solve("example_mutated"))
# end_time = timeit.default_timer()
# print(f"runtime: {end_time - start_time}")