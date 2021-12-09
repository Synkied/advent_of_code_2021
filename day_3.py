from data import day_3_input

def gamma_epsilon_compute(binaries):
    counter = {}
    power_consumption = 0
    gamma_rate = ''

    for binary in binaries:
        for idx, bit in enumerate(binary):
            counter.setdefault(idx, {})

            if bit == '0':
                counter[idx].setdefault('0', 0)
                counter[idx]['0'] += 1
            else:
                counter[idx].setdefault('1', 0)
                counter[idx]['1'] += 1

    for key, compar in counter.items():
        if compar['0'] > compar['1']:
            gamma_rate += '0'
        if compar['1'] > compar['0']:
            gamma_rate += '1'

    print(counter)

    epsilon = inverse_binary(gamma_rate)
    power_consumption = int(gamma_rate, 2) * int(epsilon, 2)
    print(power_consumption)

    return power_consumption

def inverse_binary(binary):
    temp = int(binary, 2)

    # applying Ex-or operator
    # b/w 10 and 31
    inverse_s = temp ^ (2 ** (len(binary) + 1) - 1)

    # convert the integer result
    # into binary result and then
    # slicing of the '0b1'
    # binary indicator
    res = bin(inverse_s)[3 : ]

    return res

def test_gamma_epsilon_compute():
    binaries = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
    ]

    res = gamma_epsilon_compute(binaries)

    assert res == 198


if __name__ == '__main__':
    test_gamma_epsilon_compute()
    gamma_epsilon_compute(day_3_input)
