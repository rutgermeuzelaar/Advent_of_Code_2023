import re

search_pattern_start = r'[A-Z]|[0-9]){2}(A)+'
search_pattern_end = r'[A-Z]|[0-9]){2}(Z)+'

def get_start_nodes(nodes: dict) -> list:
	for key in nodes.keys():
		regex_search = re.search(search_pattern_start, key)
		print(regex_search)