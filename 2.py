def intcode_parser(s: list) -> list:
    # s = source
    opcode = s[0]
    p1, p2 = s[1], s[2]
    target = s[3]

    if opcode not in (1, 2, 99):
        raise SyntaxError("Wrong opcode!")
    else:
        if opcode == 1:
            s[target] = p1 + p2
        elif opcode == 2:
            s[target] = p1 * p2
        elif opcode == 99:
            return s
        else:
            print("You did sth wrong")


source = [1, 4, 5, 3]

print(intcode_parser(source))
