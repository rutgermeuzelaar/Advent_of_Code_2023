def scan_left(line: str, num_end: int, num_len: int) -> bool:
	position = num_end - num_len
	if (position < 0):
		return (False)
	for i in range(position - 1, num_end + 1):
		if line[i] != '.' and not line[i].isdigit():
			return (True)
	return (False)

def scan_right(line: str, num_start: int, num_len: int) -> bool:
	position = num_start + num_len
	if (position > len(line)):
		return (False)
	for i in range(num_start - 1, position + 1):
		if line[i] != '.' and not line[i].isdigit():
			return (True)
	return (False)

def get_num_lines(filename: str) -> int:
	num_lines = 0
	file = open(filename)
	for line in file:
		num_lines += 1
	return (num_lines)

def get_line_len(filename: str) -> int:
	line_len = 0
	file = open(filename)
	for line in file:
		for char in line:
			if (char == '\n'):
				break
			line_len += 1
		break
	return (line_len)

def scan_file(filename: str) -> list:
	list_of_lines = []
	line_len = get_line_len(filename)
	file = open(filename)
	for line in file:
		line = list(line)
		list_of_lines.append(line[:line_len])
	return (list_of_lines)

def scan_specific(num_start: int, num_end: int, num_len: int, current_line: str, upper_line=[], lower_line=[]) -> bool:
	validation_list = []
	if (upper_line):
		validation_list.append(scan_left(upper_line, num_end, num_len))
		validation_list.append(scan_right(upper_line, num_start, num_len))
	if (lower_line):
		validation_list.append(scan_left(lower_line, num_end, num_len))
		validation_list.append(scan_right(lower_line, num_start, num_len))
	if (current_line):
		validation_list.append(scan_left(current_line, num_end, num_len))
		validation_list.append(scan_right(current_line, num_start, num_len))
	return (any(validation_list))
	
def solve_file(filename: str) -> int:
	part_numbers = []
	num_lines = get_num_lines(filename)
	line_list = scan_file(filename)
	line_len = get_line_len(filename)
	index_line = 0
	index_char = 0
	while (index_line < num_lines):
		while (index_char < line_len):
			num = []
			is_part_number = False
			line = line_list[index_line]
			while (line[index_char].isdigit()):
				num.append(line[index_char])
				if (index_char == line_len - 1):
					break
				index_char += 1
			if (num):
				num_len = len(num)
				num_joined = ''.join(num)
				if (index_line == 0):
					is_part_number = scan_specific(index_char - num_len, index_char, num_len, line, [], line_list[index_line + 1])
				elif (index_line == num_lines - 1):
					is_part_number = scan_specific(index_char - num_len, index_char, num_len, line_list[index_line - 1])
				else:
					is_part_number = scan_specific(index_char - num_len,  index_char, num_len, line, line_list[index_line - 1], line_list[index_line + 1])
				if (is_part_number):
					part_numbers.append(int(num_joined))
			index_char += 1
		index_char = 0
		index_line += 1
	return (sum(part_numbers))

def solve_file_gear_ratio(filename: str) -> int:
	part_numbers = []
	num_lines = get_num_lines(filename)
	line_list = scan_file(filename)
	line_len = get_line_len(filename)
	index_line = 0
	index_char = 0
	while (index_line < num_lines):
		while (index_char < line_len):
			num = []
			is_part_number = False
			line = line_list[index_line]
			while (line[index_char].isdigit()):
				num.append(line[index_char])
				if (index_char == line_len - 1):
					break
				index_char += 1
			if (num):
				num_len = len(num)
				num_joined = ''.join(num)
				if (index_line == 0):
					is_part_number = scan_specific(index_char - num_len, index_char, num_len, line, [], line_list[index_line + 1])
				elif (index_line == num_lines - 1):
					is_part_number = scan_specific(index_char - num_len, index_char, num_len, line_list[index_line - 1])
				else:
					is_part_number = scan_specific(index_char - num_len,  index_char, num_len, line, line_list[index_line - 1], line_list[index_line + 1])
				if (is_part_number):
					part_numbers.append(int(num_joined))
			index_char += 1
		index_char = 0
		index_line += 1
	return (sum(part_numbers))
# print(solve_file("input"))