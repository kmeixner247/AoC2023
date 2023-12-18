heat_map = [[int(c) for c in line] for line in open("input", 'r').read().split('\n')]

def find_closest_unvisited(unvisited, data):
	closest_node = ()
	closest = 99999
	for node in unvisited:
		if data[node] < closest:
			closest = data[node]
			closest_node = node
	return closest_node

def get_left(dir):
	return (-dir[1], dir[0])

def get_right(dir):
	return(dir[1], -dir[0])

def get_node(pos, dir, dist):
	return ((pos[0] + dir[0] * dist, pos[1] + dir[1] * dist), dir)

def is_valid(heat_map, node):
	if node[0] < 0 or node[0] >= len(heat_map) or node[1] < 0 or node[1] >= len(heat_map[0]):
		return False
	return True

unvisited = set()
unvisited.add(((0,0), (0,0)))
visited = set()
data = dict()
data.update({((0,0),(0,0)): 0})

while len(unvisited) > 0:
	(pos, dir) = find_closest_unvisited(unvisited, data)

	dist = data[(pos, dir)]

	visited.add((pos, dir))
	unvisited.remove((pos, dir))
		
	left_dir = get_left(dir)
	right_dir = get_right(dir)
	if dir == (0,0):
		left_dir = (0,1)
		right_dir = (1,0)
	left_dist = dist
	right_dist = dist
	for i in range(1,4):
		node_left = get_node(pos, left_dir, i)
		if is_valid(heat_map, node_left[0]):
			left_dist += heat_map[node_left[0][0]][node_left[0][1]]
			if not node_left in visited:
				if not node_left in unvisited:
					unvisited.add(node_left)
				if not node_left in data or left_dist < data[node_left]:
					data.update({node_left : left_dist})

		node_right = get_node(pos, right_dir, i)
		if is_valid(heat_map, node_right[0]):
			right_dist += heat_map[node_right[0][0]][node_right[0][1]]
			if not node_right in visited:
				if not node_right in unvisited:
					unvisited.add(node_right)
				if not node_right in data or right_dist < data[node_right]:
					data.update({node_right : right_dist})

result_1 = (((len(heat_map) - 1), len(heat_map[0]) - 1), (0,1))
result_2 = (((len(heat_map) - 1), len(heat_map[0]) - 1), (1,0))
print(min(data[result_1], data[result_2]))
