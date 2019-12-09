class Node:
	def __init__(self, pair):
		self.parent = pair[0]
		self.children = pair[1]

def make_tree(src: str) -> list:
	src = [line.strip().split(')') for line in src]
	return src

def count_orbits():
	pass


with open("input.txt") as f:
	src = make_tree(f)

	node_tab = []

	for idx, node in enumerate(src):
		if any(node[0] in conn for conn in src):
			print(f"{node[0]} is already in the nodetab")
		#if src[idx][0] not in node_tab[].parent:
	#		node_tab.append(Node(node))
#		else:
#			node_tab[idx].children.append(node[1])

	for i in node_tab:
		print(i.parent, i.children)
