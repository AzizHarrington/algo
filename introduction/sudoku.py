import itertools


puzzle = [
    [1, 5, 9, 0, 6, 0, 7, 0, 0, 0],
    [0, 0, 7, 1, 0, 0, 4, 9, 0, 0],
    [0, 8, 4, 0, 9, 0, 0, 0, 0, 0],
    [0, 0, 5, 9, 0, 0, 0, 8, 0, 0],
    [8, 0, 2, 0, 3, 0, 9, 0, 4, 0],
    [0, 3, 0, 0, 0, 2, 5, 0, 0, 0],
    [0, 0, 0, 0, 5, 0, 1, 4, 0, 0],
    [0, 9, 6, 0, 0, 3, 8, 0, 0, 0],
    [0, 0, 8, 0, 4, 0, 6, 3, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


def check_row(row, puzzle):
    digits = [n for n in puzzle[row] if n]
    return len(digits) == len(set(digits))


def check_column(column, puzzle):
    digits = [n[column] for n in puzzle if n[column]]
    return len(digits) == len(set(digits))


def check_square(square, puzzle):
    if square in [0, 1, 2]:
        select_rows = puzzle[:3]
    if square in [3, 4, 5]:
        select_rows = puzzle[3:6]
    if square in [6, 7, 8]:
        select_rows = puzzle[6:]
    index = square%3
    gen = [(n for n in row[index*3:(index+1)*3] if n)
            for row in select_rows]
    digits = list(itertools.chain(*[list(n) for n in gen]))
    return len(digits) == len(set(digits))


def solve_row(puzzle):
    """simple version of solve. one row only"""
    col = 0
    while col < 10:    
        if not puzzle[0][col]:
            for val in range(1, 10):
                puzzle[0][col] = val
                if check_row(0, puzzle):
                    break
            else:
                pass
        col += 1
    return puzzle[0]


def test():
    test_puzzle = [
        [1, 5, 9, 0, 6, 0, 7, 0, 0, 0],
        [0, 7, 7, 1, 0, 0, 4, 9, 0, 0],
        [0, 8, 4, 0, 9, 0, 0, 9, 0, 0],
        [0, 0, 5, 9, 0, 0, 0, 8, 0, 0],
        [8, 0, 2, 0, 3, 0, 9, 0, 4, 0],
        [0, 3, 0, 0, 0, 2, 5, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 1, 4, 0, 0],
        [0, 9, 6, 0, 0, 3, 8, 0, 0, 0],
        [0, 0, 8, 0, 4, 0, 6, 3, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    assert check_row(0, test_puzzle) == True
    assert check_row(1, test_puzzle) == False
    assert check_column(8, test_puzzle) == True
    assert check_column(7, test_puzzle) == False
    assert check_square(6, test_puzzle) == True
    assert check_square(0, test_puzzle) == False

    print('tests passed')

