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

def get_seed_pairs(seeds_range: list) -> list:
	all_seeds = []
	len_seeds_range = len(seeds_range)
	i = 0
	while i < len_seeds_range:
		range_start = seeds_range[i]
		range_len = seeds_range[i + 1]
		range_end = range_start + range_len - 1
		all_seeds.append([range_start, range_end])
		i += 2
	return all_seeds

def solve_file(filename: str):
	parsed_file = parse_file(filename)
	map_dict = file_list_to_dict(parsed_file)
	seeds_range = map_dict.get('seeds')
	seeds = get_seeds(seeds_range)
	for i, (key, value) in enumerate(map_dict.items()):
		if i == 0:
			lookup_numbers = seeds
		else:
			lookup_numbers = [convert_num_in_range(num, value) for num in lookup_numbers]
	return min(lookup_numbers)

def sort_map_lines(map_lines: list) -> list:
	len_map_lines = len(map_lines)
	i = 0
	while i < len_map_lines - 1:
		swapped = False
		j = 0
		while j < len_map_lines - i - 1:
			if map_lines[j][1] > map_lines[j+1][1]:
				temp_line = map_lines[j+1]
				map_lines[j+1] = map_lines[j]
				map_lines[j] = temp_line
				swapped = True
			j += 1
		if not swapped:
			break
		i += 1
	return map_lines

parsed_file = parse_file("example")
map_dict = file_list_to_dict(parsed_file)
seeds_range = map_dict.get('seeds')
test_lines = [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]]
print(sort_map_lines(test_lines))
# Set border for lower than lowest value | lower than zero not possible
# If lowest value is zero or lowest value is set sort from lowest to highest
# Do this for all entries to decide if a seed pair is in the shortest location