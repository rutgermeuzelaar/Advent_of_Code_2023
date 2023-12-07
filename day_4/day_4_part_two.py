import day_4
# def solve_recursive(index: int, sub_indices: int, file: list, card_total_dict: dict) -> int:
# 	if (index == last):
# 		return (card_total_dict)
# 	if (sub_indices):
# 		for i in sub_indices:
# 			card_total_dict[i] = 
# 	else:
# 		num_copies = calculate_points(file[index])
# 		sub_indices = [i + index for i in range(1, num_copies)]
# 	solve_recursive()

def calculate_points(scores: list) -> int:
	found_counter = 0
	current_score = 0
	for score in scores[1]:
		if score in scores[0]:
			found_counter += 1
	return (found_counter)

def solve(index: int, sum_copies: dict, file: list, len: int):
	if (index == len):
		return (sum_copies)
	num_points = calculate_points(file[index])
	if (num_points):
		for i in range(sum_copies.get(index)):
			for j in range(index + 1, index+num_points+1):
				sum_copies[j] += 1
	return (solve(index + 1, sum_copies, file, len))

def file_to_lists(filename: str) -> list:
	file = open(filename)
	file_in_list = []
	for line in file:
		file_in_list.append(day_4.convert_string(line))
	return(file_in_list)

test_dict = {0: 1, 1: 1, 2: 1}
def solve_file(filename: str) -> int:
	file_list = file_to_lists(filename)
	len_file_list = len(file_list) - 1
	sum_dict = {i: 1 for i in range(len(file_list))}
	sum_dict = solve(0, sum_dict, file_list, len_file_list)
	return (sum(sum_dict.values()))

print(solve_file("input"))
# tuple with,: number of copies, updated since last call
# Loop once to get all the number of points per card
# Loop again to increment the copies of each card
# Loop once to get all the number of points per card
# etc etc until all the number