import parse_file
import re

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

def get_steps_loop(nodes: dict, instructions: str, start_node: str, end_node: str):
	steps = 0
	instructions_count = 0
	instructions_len = len(instructions)
	current_node = start_node
	while (current_node != end_node):
		if (steps % instructions_len == 0):
			instructions_count += 1
		current_instruction = instructions[steps - (instructions_count * instructions_len)]
		if (current_instruction == 'L'):
			current_node = nodes.get(current_node)[0]
		else:
			current_node = nodes.get(current_node)[1]
		steps += 1
		if (steps == 100):
			pass
	return (steps)

def wrapper_the_quickness(nodes: dict, instructions: list, start_nodes: list, end_nodes: list):
	nodes_position_dict = {start_node: None for start_node in start_nodes}
	steps = 0
	is_unsolved = True
	end_nodes_len = len(end_nodes)
	while is_unsolved:
		end_node_count = 0
		nodes_position_dict = the_quickness(nodes, nodes_position_dict, instructions, steps, end_nodes)
		for count, end_node in enumerate(nodes_position_dict.values()):
			if end_node in end_nodes:
				end_node_count += 1
		if (end_nodes_len == end_node_count):
			is_unsolved = False
		nodes_position_dict = {value: key for key, value in nodes_position_dict.items()}
		steps += 1
	return (steps)
		
def the_quickness(nodes: dict, nodes_position: dict, instructions: list, steps: int, end_nodes: list) -> dict:
	instructions_len = len(instructions)
	steps = steps % instructions_len
	for key in nodes_position.keys():
		current_instruction = instructions[steps]
		if (current_instruction == 'L'):
			current_node = nodes.get(key)[0]
		else:
			current_node = nodes.get(key)[1]
		nodes_position[key] = current_node
	return (nodes_position)

def get_start_nodes(nodes: dict) -> list:
	start_list = []
	search_pattern_start = r'([A-Z]|[0-9]){2}(A)+'
	for key in nodes.keys():
		regex_search = re.search(search_pattern_start, key)
		if (regex_search):
			append_value = regex_search.group()
			start_list.append(append_value)
	return (start_list)

def get_end_nodes(nodes: dict) -> list:
	start_list = []
	search_pattern_end = r'([A-Z]|[0-9]){2}(Z)+'
	for key in nodes.keys():
		regex_search = re.search(search_pattern_end, key)
		if (regex_search):
			append_value = regex_search.group()
			start_list.append(append_value)
	return (start_list)
	
parsed_file = parse_file.parse_file("input")
nodes = parse_file.get_nodes(parsed_file)
instructions = parse_file.get_instructions(parsed_file)
start_nodes = get_start_nodes(nodes)
end_nodes = get_end_nodes(nodes)
print(wrapper_the_quickness(nodes, instructions, start_nodes, end_nodes))