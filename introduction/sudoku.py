import itertools, sys

sys.setrecursionlimit(5000)


def check_row(row, puzzle):
    digits = [n for n in puzzle[row] if n]
    return (len(digits) == len(set(digits))) and (sum(digits) <= 45)


def check_column(column, puzzle):
    digits = [n[column] for n in puzzle if n[column]]
    return (len(digits) == len(set(digits))) and (sum(digits) <= 45)


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


def check_all_squares(puzzle):
    """applies check square to whole puzzle"""
    for s in range(9):
        if not check_square(s, puzzle):
            return False
    return True


def find_next_blank(puzzle):
    """find the next blank cell and return row, col"""
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return(row, col)


def is_solved(puzzle):
    """check that whole puzzle passes all check tests"""
    for row in range(len(puzzle)):
        if not (check_row(row, puzzle) and sum(puzzle[row]) == 45):
            return False
        for col in range(len(puzzle)):
            if not (check_column(col, puzzle) and sum(puzzle[row]) == 45):
                return False

    for i in range(len(puzzle)):
        if not check_square(i, puzzle):
            return False
    return True


def solve(puzzle):
    if is_solved(puzzle):
        return puzzle
    else:
        row, col = find_next_blank(puzzle)
        for i in range(1, 10):
            puzzle[row][col] = i
            if check_row(row, puzzle) and check_column(col, puzzle) and check_all_squares(puzzle):
                if solve(puzzle):
                    return solve(puzzle)
                else:
                    puzzle[row][col] = 0
        else:
            puzzle[row][col] = 0
    return False


puzzle = [
    [0, 0, 8, 0, 0, 9, 0, 0, 0],
    [0, 0, 4, 1, 6, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 5],
    [1, 4, 0, 0, 0, 0, 0, 9, 0],
    [0, 2, 0, 0, 0, 0, 0, 5, 0],
    [0, 5, 0, 0, 0, 0, 0, 8, 6],
    [3, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 8, 1, 9, 0, 0],
    [0, 0, 0, 3, 0, 0, 4, 0, 0]
]

print(solve(puzzle))


def test():
    test_puzzle = [
        [1, 5, 9, 0, 6, 0, 7, 0, 0],
        [0, 7, 7, 1, 0, 0, 4, 9, 0],
        [0, 8, 4, 0, 9, 0, 0, 9, 0],
        [0, 0, 5, 9, 0, 0, 0, 8, 0],
        [8, 0, 2, 0, 3, 0, 9, 0, 4],
        [0, 3, 0, 0, 0, 2, 5, 0, 0],
        [0, 0, 0, 0, 5, 0, 1, 4, 0],
        [0, 9, 6, 0, 0, 3, 8, 0, 0],
        [0, 0, 8, 0, 4, 0, 6, 3, 2]
    ]

    assert check_row(0, test_puzzle) == True
    assert check_row(1, test_puzzle) == False
    assert check_column(8, test_puzzle) == True
    assert check_column(7, test_puzzle) == False
    assert check_square(6, test_puzzle) == True
    assert check_square(0, test_puzzle) == False

    print('tests passed')
