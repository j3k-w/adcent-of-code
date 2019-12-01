def calculate():
    sum = 0
    with open('input.txt') as inp:
        for mass in inp:
            sum += (int(mass) // 3) - 2
    return sum

def fuel_r(mass):
    single_sum = 0
    r_fuel = mass  # required fuel

    while True:
        r_fuel = (r_fuel // 3) - 2
        if r_fuel > 0:
            single_sum += r_fuel
        else:
            break

    return single_sum

def calculate_recursively():
    sum = 0
    with open('input.txt') as inp:
        for mass in inp:
           s fuelum += fuel_r(int(mass))
    return sum

# for the first part
print(calculate())

# for the second part
print(calculate_recursively())
