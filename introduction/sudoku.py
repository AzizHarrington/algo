puzzle = [
	'159*6*7**',
    '**71**49*',
    '*84*9****',
	'**59***8*',
	'8*2*3*9*4',
	'*3***25**',
	'****5*14*',
	'*96**38**',
	'**8*4*632'
]


def check_row(row, puzzle):
	digits = [n for n in puzzle[row] if n.isdigit()]
	return len(digits) == len(set(digits))


def check_column(column, puzzle):
	digits = [n[column] for n in puzzle if n[column].isdigit()]
	return len(digits) == len(set(digits))


import itertools
def check_square(square, puzzle):
	if square in [0, 1, 2]:
		select_rows = puzzle[:3]
	if square in [3, 4, 5]:
		select_rows = puzzle[3:6]
	if square in [6, 7, 8]:
		select_rows = puzzle[6:]
	index = square%3
	gen = [(n for n in row[index*3:(index+1)*3] if n.isdigit())
			for row in select_rows]
	digits = list(itertools.chain(*[list(n) for n in gen]))
	return len(digits) == len(set(digits))



def test():
	test_puzzle = [
		'159*6*7**',
	    '*771**49*',
	    '*84*9**9*',
		'**59***8*',
		'8*2*3*9*4',
		'*3***25**',
		'****5*14*',
		'*96**38**',
		'**8*4*632'
	]
	assert check_row(0, test_puzzle) == True
	assert check_row(1, test_puzzle) == False
	assert check_column(8, test_puzzle) == True
	assert check_column(7, test_puzzle) == False
	assert check_square(6, test_puzzle) == True
	assert check_square(0, test_puzzle) == False
	print('tests passed')


print(test())