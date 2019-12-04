def find(start: int, stop: int) -> int:
    cnt = 0

    for num in range(start, stop + 1):
        if len(str(num)) == 6:
            # make a list out of number and
            # delete repeating values
            num_ = list(dict.fromkeys(str(num)))

            # if there is a repeating value
            if len(num_) < 6:
                print(num_)
                for i, s in enumerate(num_):
                    if s <= num_[i+1]:
                        print(num_)
            # if str(num) in '1234567890'
            # num_ = list(dict.fromkeys(num))

        # cnt += 1
    return cnt


start = 111111
stop  = 111114
# print(find(start, stop))
find(start, stop)
