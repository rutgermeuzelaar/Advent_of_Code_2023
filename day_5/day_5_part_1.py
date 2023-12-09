import re

def parse_file(filename: str) -> list:
	file_list = []
	file = open(filename)
	for line in file:
		file_list.append(line)
	file.close()
	return file_list

def file_list_to_dict(file_list: list) -> dict:
	seeds_search = r'(seeds)'
	map_search_pattern = r'(\w)+-(\w)+-(\w)+'
	return_dict = {}
	max_maps = 7
	map_counter = 0
	len_file_list = len(file_list)
	index = 0
	while index < len_file_list - 1:
		line = file_list[index]
		seeds_search = re.search(r'(seeds)', line)
		map_search = re.search(r'(\w)+-(\w)+-(\w)+', line)
		if index == 30:
			pass
		if seeds_search != None:
			key = seeds_search.group()
			value = get_digits(line)
			return_dict.setdefault(key, value)
		if map_search != None:
			map_counter += 1
			key = map_search.group()
			value = []
			if map_counter == max_maps:
				while index < len_file_list:
					digits = get_digits(file_list[index])
					if digits:
						value.append(digits)
					index += 1
			else:
				index += 1
				while re.search(map_search_pattern, file_list[index]) == None:
					digits = get_digits(file_list[index])
					if digits:
						value.append(digits)
					index += 1
			return_dict.setdefault(key, value)
			continue
		index += 1
	return return_dict

def get_digits(line: str) -> list:
	digits = []
	digit_update = False
	i = 0
	line_len = len(line)
	while i < line_len:
		digit_arr = []
		digit_update = False
		while line[i].isdigit() and i < line_len:
			digit_arr.append(line[i])
			digit_update = True
			i += 1
		if digit_update:
			digit_arr_joined = ''.join(digit_arr)
			digits.append(int(digit_arr_joined))
			continue
		i += 1
	return digits

def convert_num_in_range(number: int, range_values: list) -> int:
	for single_range in range_values:
		dest_range_start = single_range[0]
		source_range_start = single_range[1]
		range_len = single_range[2]
		if number >= source_range_start and number < source_range_start + range_len:
			offset = number - source_range_start
			converted_number = dest_range_start + offset
			return converted_number
	return number

def solve_file(filename: str):
	parsed_file = parse_file(filename)
	map_dict = file_list_to_dict(parsed_file)
	seeds = map_dict.get('seeds')
	for i, (key, value) in enumerate(map_dict.items()):
		if i == 0:
			lookup_numbers = seeds
		else:
			lookup_numbers = [convert_num_in_range(num, value) for num in lookup_numbers]
	return min(lookup_numbers)

print(solve_file("input"))
