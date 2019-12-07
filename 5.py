def compute(src: list) -> int:
    inp = src[:]
    pos = 0

    while pos < len(inp):
        try:
            command = inp[pos:pos+4]
        except:
            command = inp[pos:]
        finally:
            instr = str(inp[pos])[::-1]
            opcode = int(instr[:2].replace('0', ''))
            print("opcode:", opcode)
            if opcode == 99:
                return inp
            elif opcode in (1, 2):
                # FIRST PARAMETER; FAC1
                if instr[2]:
                    fac1 = command[1]
                    print(f"fac1 mode: {instr[1]}, fac1 value: {fac1}")
                else:
                    fac1 = inp[command[1]]
                    print(f"fac1 mode: {instr[1]}, fac1 value: {fac1}")

                # SECOND PARAMETER; FAC2
                if instr[3]:
                    fac2 = command[2]
                    print(f"fac2 mode: {instr[2]}, fac2 value: {fac2}")
                else:
                    fac2 = inp[command[2]]
                    print(f"fac2 mode: {instr[2]}, fac2 value: {fac2}")

                # THIRD PARAMETER; TARGET
                if instr[4]:
                    target = inp[command[3]]
                    print(f"target mode: {instr[3]}, target value: {target}")
                else:
                    target = command[3]
                    print(f"target mode: {instr[3]}, target value: {target}")

                if opcode == 1:
                    inp[target] = fac1 + fac2
                    print(f"element {target} is now {inp[target]}")
                elif opcode == 2:
                    inp[target] = fac1 * fac2
                    print(f"element {target} is now {inp[target]}")
            pos += 4

    return inp


if __name__=="__main__":
    # with open('5input.txt') as f:
    #     src = [int(x) for x in next(f).split(',')]
    src = [1002, 4, 3, 4, 33]
    print("before:", src)
    print("after:", compute(src))



def c2():
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
        elif opcode == 3:
            inp[target] = fac1 * fac2


    return inp[0]
