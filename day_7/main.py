import parse_file
import sort_utilities

def main():
	filename = "input"
	file = parse_file.get_type_lists(filename)
	sorted_joined_list = []
	return_dict = parse_file.parse_file(filename)
	for i in file:
		len_of_list = len(i)
		if (len_of_list > 1):
			to_append = sort_utilities.sort_list_of_hands(i)
			for value in to_append:
				sorted_joined_list.append(value)
		elif (i):
			to_append = i
			for value in to_append:
				sorted_joined_list.append(value)
	total_winnings_list = []
	for rank, hand in enumerate(sorted_joined_list):
		total_winnings_list.append(return_dict.get(hand) * (rank + 1))
	print(sum(total_winnings_list))

if __name__ == "__main__":
	main()