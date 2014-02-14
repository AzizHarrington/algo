

puzzle = ['159*6*7**',
          '**71**49*',
          '*84*9****',
          '**59***8*',
          '8*2*3*9*4',
          '*3***25**',
          '****5*14*',
          '*96**38**',
          '**8*4*632']


def rotate_puzzle(puzzle):
    result = []
    length = len(puzzle)
    for x in range(length):
        row = ''
        for y in range(length):
            row += puzzle[y][x]
        result.append(row)
    return result


rotated_puzzle = rotate_puzzle(puzzle)

assert len(rotated_puzzle) == 9