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
                # meeting_points.append([[el_i, el_j], [ne_i, ne_j]])
                meeting_points.append([[el_i, ne_i], [el_j, ne_j]])

    return meeting_points


def parse_vectors(mpp):
    "Parses the vectors of crossing points"
    x, y = 0, 0
    # true_meets = []

    for change in mpp:
        for vector in change:
            print(max(set(vector), key=vector.count))

            # if vector[0][1] == vector[1][1]:
        #         x = vector[0][1]
        #         y = vector[1][0]
        #     elif vector[0][0] == vector[1][0]:
        #         x = vector[0][0]
        #         y = vector[0][1]
        # print([x, y])

    # for i, m in enumerate(mpp):
    #     if m[i][0][1] == m[i][0][1]:
    #         y = m[i][0][1]
    #         x = m[i][1][0]
    #     elif m[i][0][0] == m[i][1][0]:
    #         y = m[i][1][0]
    #         x = m[i][0][1]

    #     true_meets.append([x, y])

    # return true_meets


wire1 = ['R8', 'U5', 'L5', 'D3']
wire2 = ['U7', 'R6', 'D4', 'L4']

s1 = compute(wire1)
s2 = compute(wire2)
meeting_points = compare(s1, s2)
parse_vectors(meeting_points)
