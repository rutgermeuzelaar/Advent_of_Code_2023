# scan in 9 x 9 radius
# look for number, if number found return
# validate if it has two numbers

import day_3

def scan_for_ints(star_position: int, current_line=[], upper_line=[], lower_line=[]) -> int:
	line_len = len(current_line)
	coordinates = []
	num_list = []
	coordinate_before = star_position - 1
	coordinate_after = star_position + 1
	i = 0
	joined_list = current_line, upper_line, lower_line

	coordinates.append(star_position)
	if (coordinate_before > 0):
		coordinates.append(coordinate_before)
	if (coordinate_after < line_len):
		coordinates.append(coordinate_after)
	for line in joined_list:
		i = 0
		if (line):
			while (i < line_len):
				number_in_range = False
				num = []
				while (line[i].isdigit()):
					if (i in coordinates):
						number_in_range = True
					num.append(line[i])
					if (i == line_len - 1):
						break
					i += 1
				if (number_in_range):
					num_joined = ''.join(num)
					num_list.append(int(num_joined))
					continue
				i += 1
	if (len(num_list) == 2):
		return(num_list[0] * num_list[1])
	return (-1)

def solve_gear_ratio(filename: str) -> int:
	list_of_lists = day_3.scan_file(filename)
	num_lines = day_3.get_num_lines(filename)
	line_len = day_3.get_line_len(filename)
	index_line = 0
	index_char = 0
	num_list = []
	while (index_line < num_lines):
		while (index_char < line_len):
			if (list_of_lists[index_line][index_char] == '*'): 
				to_append = 0
				if (index_line == 0):
					to_append = scan_for_ints(index_char, list_of_lists[index_line], [],list_of_lists[index_line + 1])
				elif (index_line == num_lines - 1):
					to_append = scan_for_ints(index_char, list_of_lists[index_line], list_of_lists[index_line - 1])
				else:
					to_append = scan_for_ints(index_char, list_of_lists[index_line], list_of_lists[index_line - 1], list_of_lists[index_line + 1])
				if (to_append > 0):
					num_list.append(to_append)
			index_char += 1
		index_char = 0
		index_line += 1
	print(num_list)
	return (sum(num_list))

print(solve_gear_ratio("input"))
				
				


