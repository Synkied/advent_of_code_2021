from data import day_2

def compute_submarine_depth(moves):
    horizontal_moves = 0
    vertical_moves = 0
    aim = 0
    depth = 0

    for move in moves:
        direction, value = move.split('_')
        value = int(value)

        if direction == 'forward':
            horizontal_moves += value
            depth += aim * value

        elif direction == 'up':
            vertical_moves -= value
            aim -= value

        elif direction == 'down':
            vertical_moves += value
            aim += value

    part_1 = horizontal_moves * vertical_moves
    part_2 = horizontal_moves * depth
    print('part_1', part_1)
    print('part_2', part_2)

    return {
        'part_1': part_1,
        'part_2': part_2,
    }


def test_depth_measure():
    moves = [
        "forward_5",
        "down_5",
        "forward_8",
        "up_3",
        "down_8",
        "forward_2",
    ]

    res = compute_submarine_depth(moves)

    assert res['part_1'] == 150
    assert res['part_2'] == 900

if __name__ == '__main__':
    test_depth_measure()
    compute_submarine_depth(day_2)
