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
