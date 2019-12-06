import math


def repetition(number: str) -> bool:
    result = False
    for i in range(len(number) - 1):
        if number[i] == number[i+1]:
            result = True
            return result

    return result


def repetition2(num: str) -> bool:
    new_num = []
    for i in range(math.floor(len(num)/2)):
        new_num.append([num[i*2], num[i*2+1]])

    for i in new_num:
        if i[0] != i[1]:
            return False

    return True


def non_decreasing(number: str) -> bool:
    result = True
    for i in range(len(number) - 1):
        if number[i] > number[i + 1]:
            result = False
            break

    return result


def find(start: int, stop: int) -> int:
    cnt = 0

    for num in range(start, stop + 1):
        num = str(num)
        if non_decreasing(num):
            if repetition(num) or repetition2(num):
                cnt += 1
    return cnt


start = 264793
stop = 803935
# for i in range(start, stop)
print(find(start, stop))
