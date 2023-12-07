word_number_dict = {"one": 1,
					"two": 2,
					"three": 3,
					"four": 4,
					"five": 5,
					"six": 6,
					"seven": 7,
					"eight": 8,
					"nine": 9}

def get_number(string: str, lookup_dict: dict) -> int:
	number_list = []
	for i, char in enumerate(string):
		if char.isdigit():
			number_list.append(int(char))
		for key, value in lookup_dict.items():
			if (string[i:].startswith(key)):
				number_list.append(value)
	return (int(str(number_list[0]) + str(number_list[-1])))

def read_file(text_file: str, lookup_dict: dict[str, int]) -> int:
	sum_list = []
	read_file = open(text_file)
	for line in read_file:
		sum_list.append(get_number(line, lookup_dict))
	return(sum(sum_list))

print(read_file("input", word_number_dict))