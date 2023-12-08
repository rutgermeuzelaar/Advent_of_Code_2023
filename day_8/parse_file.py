def parse_file(filename: str) -> list:
	parsed_file = []
	file = open(filename)
	for line in file:
		if (line != '\n'):
			parsed_file.append(line)
	print(parsed_file)
	return (parsed_file)

def get_instructions(parsed_file) -> str:
	origin = parsed_file[0]
	instructions = []
	i = 0
	while origin[i] != '\n':
		instructions.append(origin[i])
		i += 1
	instructions = ''.join(instructions)
	print(instructions)
	return (instructions)

def get_nodes(parsed_file) -> list:
	nodes = {}
	for index, node in enumerate(parsed_file):
		if index == 0:
			continue
		i = 0
		element_count = 0
		key = []
		value_1 = []
		value_2 = []
		values = []
		while (node[i].isalpha()):
			key.append(node[i])
			i += 1
		while (not(node[i].isalpha())):
			i += 1
		while (node[i].isalpha()):
			value_1.append(node[i])
			i += 1
		while (not(node[i].isalpha())):
			i += 1
		while (node[i].isalpha()):
			value_2.append(node[i])
			i += 1
		key = ''.join(key)
		value_1 = ''.join(value_1)
		value_2 = ''.join(value_2)
		nodes[key] = [value_1, value_2]
	return nodes

print(get_nodes(parse_file("example_2")))