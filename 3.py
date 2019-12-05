def compute(path: list) -> list:
    """Computes the path by given instruction
       and returns vector of points where
       direction is being changed"""
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


def compare(s1: list, s2: list) -> list:
    "Compares two paths and returns list of crossing vectors"
    meeting_points = []

    for idx, el_i in enumerate(s1):
        ne_i = s1[(idx + 1) % len(s1)]
        for jdx, el_j in enumerate(s2):
            ne_j = s2[(jdx + 1) % len(s2)]
            if (((el_i[0] > el_j[0] and
                  el_i[1] < el_j[1]) and
                 (ne_i[0] < ne_j[0] and
                  ne_i[1] > ne_j[1])) or
                ((el_i[0] < el_j[0] and
                  el_i[1] > el_j[1]) and
                 (ne_i[0] > ne_j[0] and
                  ne_i[1] < ne_j[1]))):
                meeting_points.append([[el_i, ne_i], [el_j, ne_j]])

    return meeting_points


def parse_vectors(mpp):
    "Parses the vectors of crossing points"
    true_meets = []

    for change in mpp:
        for vector in change:
            if vector[0][1] == vector[1][1]:
                x = vector[0][1]
            elif vector[0][0] == vector[1][0]:
                x = vector[0][0]
            true_meets.append(abs(x))

    print(true_meets)
    true_meets = [true_meets[i:i+2] for i in range(0, len(true_meets), 2)]

    print(true_meets)

    result = sum(min(true_meets, key=sum))
    print(result)

    return result


# wire1 = ['R8', 'U5', 'L5', 'D3']
# wire2 = ['U7', 'R6', 'D4', 'L4']

# wire1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
# wire2 = ['U62','R66','U55','R34','D71','R55','D58','R38']

wire1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
wire2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

s1 = compute(wire1)
s2 = compute(wire2)
meeting_points = compare(s1, s2)
parse_vectors(meeting_points)
