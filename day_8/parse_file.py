def parse_file(filename: str) -> list:
	parsed_file = []
	file = open(filename)
	for line in file:
		if (line != '\n'):
			parsed_file.append(line)
	file.close()
	return (parsed_file)

def get_instructions(parsed_file) -> str:
	origin = parsed_file[0]
	instructions = []
	i = 0
	while origin[i] != '\n':
		instructions.append(origin[i])
		i += 1
	instructions = ''.join(instructions)
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
		while (node[i].isalnum()):
			key.append(node[i])
			i += 1
		while (not(node[i].isalnum())):
			i += 1
		while (node[i].isalnum()):
			value_1.append(node[i])
			i += 1
		while (not(node[i].isalnum())):
			i += 1
		while (node[i].isalnum()):
			value_2.append(node[i])
			i += 1
		key = ''.join(key)
		value_1 = ''.join(value_1)
		value_2 = ''.join(value_2)
		nodes[key] = [value_1, value_2]
	return nodes
