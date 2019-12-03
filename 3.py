def compare(s1, s2):
    meeting_points = []

    for idx, elem_i in enumerate(s1):
        ne_i = s1[(idx + 1) % len(s1)]
        for jdx, elem_j in enumerate(s2):
            ne_j = s2[(jdx + 1) % len(s2)]
            if (elem_i[0] > elem_j[0] and elem_i[1] < elem_j[1]) and (ne_i[0] < ne_j[0] and ne_i[1] > ne_j[1]):
                meeting_points.append([elem_i, elem_j])

    return meeting_points


def compute(path):
    pos = [0, 0]
    s = []

    for instr in path:
        direction = instr[0]
        steps = int(instr[1:])

        if direction == 'R':
            pos[0] += steps
        elif direction == 'L':
            pos[0] -= steps
        elif direction == 'U':
            pos[1] += steps
        elif direction == 'D':
            pos[1] -= steps

        s.append(pos[:])

    return s


wire1 = ['R8', 'U5', 'L5', 'D3']
wire2 = ['U7', 'R6', 'D4', 'L4']
# print(compute(wire1))
# print(compute(wire2))

s1 = compute(wire1)
s2 = compute(wire2)
print(compare(s1, s2))
