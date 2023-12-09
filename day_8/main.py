import navigate
import parse_file
import math
def main():
	parsed_file = parse_file.parse_file("input")
	nodes = parse_file.get_nodes(parsed_file)
	instructions = parse_file.get_instructions(parsed_file)
	instructions_len = len(instructions)
	instructions_passed = 0
	steps = 0
	current_nodes = ["AAA", "NJA", "BHA", "HTA", "LJA", "XXA"]
	lcm_list = []
	for node in current_nodes:
		lcm_list.append(navigate.get_steps_loop(nodes, instructions, node))
	print(math.lcm(*lcm_list))
if __name__ == "__main__":
	main()