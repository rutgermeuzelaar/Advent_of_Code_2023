import parse_file

def get_start_node(nodes: dict) -> str:
	return (list(nodes)[0])

def get_end_node(nodes: dict) -> str:
	return (list(nodes)[-1])

def get_steps_recursive(steps: int, nodes: list, instructions: str, current_node: str, instructions_count: int):
	if (current_node == "ZZZ"):
		return (steps)
	instruction_len = len(instructions)
	if (steps % instruction_len == 0):
		instructions_count += 1
	current_instruction = instructions[steps - (instructions_count * instruction_len)]
	if (current_instruction == 'L'):
		current_node = nodes.get(current_node)[0]
	else:
		current_node = nodes.get(current_node)[1]
	return (get_steps_recursive(steps + 1, nodes, instructions, current_node, instructions_count))

def get_steps_loop(nodes: list, instructions: str):
	steps = 0
	instructions_count = 0
	instructions_len = len(instructions)
	current_node = "AAA"
	while (current_node != "ZZZ"):
		if (steps % instructions_len == 0):
			instructions_count += 1
		current_instruction = instructions[steps - (instructions_count * instructions_len)]
		if (current_instruction == 'L'):
			current_node = nodes.get(current_node)[0]
		else:
			current_node = nodes.get(current_node)[1]
		steps += 1
		# print(steps)
		if (steps == 100):
			pass
	return (steps)

parsed_file = parse_file.parse_file("input")
nodes = parse_file.get_nodes(parsed_file)
instructions = parse_file.get_instructions(parsed_file)
print(instructions)
print(get_start_node(nodes))
print(get_end_node(nodes))
print(get_steps_loop(nodes, instructions))