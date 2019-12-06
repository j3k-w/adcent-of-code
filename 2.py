<<<<<<< HEAD
def computing(src: list, noun, verb) -> int:
    inp = src[:]
    inp[1] = noun
    inp[2] = verb

    for index in range(0, len(inp), 4):
        opcode = inp[index]
        fac1 = inp[inp[index + 1]]
        fac2 = inp[inp[index + 2]]
        target = inp[index + 3]

        if opcode == 99:
            return inp[0]
        elif opcode == 1:
            inp[target] = fac1 + fac2
        elif opcode == 2:
            inp[target] = fac1 * fac2


    return inp[0]

if __name__=="__main__":
    with open('2input.txt') as f:
        src = [int(x) for x in next(f).split(',')]

        # Part 1.
        print("First part:", computing(src, 12, 2))

        # # Part 2.
        for noun in range(100):
            for verb in range(100):
                if computing(src, noun, verb) == 19690720:
                    print("Second part:", 100 * noun + verb)
                    break
=======
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
>>>>>>> e0eb5f3229caf2ce54fef933894f7a1dda213854
