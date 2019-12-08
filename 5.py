def compute(src: list):
    ID = input("Provide an ID of the system to test: ")
    if int(ID) != 1:
        return "-- wrong ID -- system halted!"
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
                if len(instr) >= 2 and instr[2] == "1":
                    fac1 = command[1]
                    print(f"fac1 mode: {instr[2]}, fac1 value: {fac1}")
                else:
                    fac1 = inp[command[1]]
                    print(f"fac1 mode: {instr[2]}, fac1 value: {fac1}")

                # SECOND PARAMETER; FAC2
                if len(instr) >= 4 and instr[3] == "1":
                    fac2 = command[2]
                    print(f"fac2 mode: {instr[3]}, fac2 value: {fac2}")
                else:
                    fac2 = inp[command[2]]
                    print(f"fac2 mode: {instr[3]}, fac2 value: {fac2}")

                # THIRD PARAMETER; TARGET
                if len(instr) == 5 and instr[4] == "1":
                    target = inp[command[3]]
                    print(f"target mode: {instr[4]}, target value: {target}")
                else:
                    target = command[3]
                    print(f"target mode: 0, target value: {target}")

                if opcode == 1:
                    inp[target] = fac1 + fac2
                    print(f"element {target} is now {inp[target]}")
                elif opcode == 2:
                    inp[target] = fac1 * fac2
                    print(f"element {target} is now {inp[target]}")
                pos += 4

            elif opcode in (3, 4):
                print(opcode)
                if opcode == 3:
                    inn = inp[inp[pos+1]]
                    print("opcode 3; value:", inn)
                elif opcode == 4:
                    print(inp[pos+1])

                pos += 2

    return inp


if __name__=="__main__":
    # with open('5input.txt') as f:
    #     src = [int(x) for x in next(f).split(',')]
    src = [1002, 4, 3, 4, 33]
    srv = [1101, 100, -1, 4, 0]
    srb = [3, 0, 4, 0, 99]
    print("before:", srb)
    print("after:", compute(srb))
