from data import day_5_data


def determine_min_max(i, j):
    the_max = max(i, j)
    the_min = min(i, j)

    return the_min, the_max


def vents_overlap(data):
    max_x = int(
        max([x for d in data for xy in d.split(' -> ') for x in xy.split(',')])
    )
    max_y = int(
        max([y for d in data for xy in d.split(' -> ') for y in xy.split(',')])
    )
    diagram = []
    total_overlaps = 0

    for _ in range(max_y + 1):
        diagram.append([0] * (max_x + 1))

    for d in data:
        xy1, xy2 = d.split(' -> ')
        x1, y1 = map(int, xy1.split(','))
        x2, y2 = map(int, xy2.split(','))

        if x1 == x2:
            the_min, the_max = determine_min_max(y1, y2)
            the_min = min(y1, y2)
            for i in range(the_min, the_max + 1):
                diagram[i][x1] += 1
        elif y1 == y2:
            the_min, the_max = determine_min_max(x1, x2)
            for i in range(the_min, the_max + 1):
                diagram[y1][i] += 1

        else:
            min_couple = min((x1, y1), (x2, y2))

            the_min_x, the_max_x = determine_min_max(x1, x2)
            the_min_y, the_max_y = determine_min_max(y1, y2)
            new_max_y = the_max_y
            new_min_y = the_min_y

            for i in range(the_min_x, the_max_x + 1):
                if the_max_y == min_couple[1]:
                    diagram[new_max_y][i] += 1
                    new_max_y -= 1

                else:
                    diagram[new_min_y][i] += 1
                    new_min_y += 1

    for i in range(max_y + 1):
        for j in range(max_x + 1):
            if diagram[i][j] >= 2:
                total_overlaps += 1

    return total_overlaps


def test_vents_overlap():
    data = [
        '0,9 -> 5,9',
        '8,0 -> 0,8',
        '9,4 -> 3,4',
        '2,2 -> 2,1',
        '7,0 -> 7,4',
        '6,4 -> 2,0',
        '0,9 -> 2,9',
        '3,4 -> 1,4',
        '0,0 -> 8,8',
        '5,5 -> 8,2',
    ]

    res = vents_overlap(data)
    print('res test', res)

    assert res == 12


if __name__ == '__main__':
    test_vents_overlap()
    res = vents_overlap(day_5_data)
    print(res)
