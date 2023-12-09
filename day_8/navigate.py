import parse_file

def get_steps_loop(nodes: dict, instructions: str, start_node: str):
	instructions_count = 0
	instructions_len = len(instructions)
	current_node = start_node
	steps = 0
	while (current_node[2] != 'Z'):
		if (steps % instructions_len == 0):
			instructions_count += 1
		current_instruction = instructions[steps - (instructions_count * instructions_len)]
		if current_instruction == 'L':
			current_node = nodes.get(current_node)[0]
		elif current_instruction == 'R':
			current_node = nodes.get(current_node)[1]
		steps += 1
	return steps

def increment_all_nodes(nodes: dict, single_instruction: str, nodes_to_increment: list) -> list:
	incremented_nodes = []
	for node in nodes_to_increment:
		if single_instruction == 'L':
			incremented_nodes.append(nodes.get(node)[0])
		if single_instruction == 'R':
			incremented_nodes.append(nodes.get(node)[1])
	return incremented_nodes

def is_end_node(node: str) -> bool:
	if node.endswith('Z'):
		return True
	return False