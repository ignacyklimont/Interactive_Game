# FIELD COORDINATES

# (1, 3) (2, 3) (3, 3)
# (1, 2) (2, 2) (3, 2)
# (1, 1) (2, 1) (3, 1)

def game_state(cells):
	cells_full = ' ' not in cells
	win_comb = [cells[0:3], cells[3:6], cells[6:9], cells[0:7:3], cells[1:8:3], cells[2:9:3], cells[0:9:4], cells[2:7:2]]
	o_win_count = win_comb.count('OOO')
	x_win_count = win_comb.count('XXX')
	if o_win_count == 1:
		return 'O wins the game'
	if x_win_count == 1:
		return 'X wins the game'
	else:
		if cells_full:
			return 'Draw'
cells = '         '
cells_matrix = [[cells[0], cells[1], cells[2]], [cells[3], cells[4], cells[5]], [cells[6], cells[7], cells[8]]]

def print_board():
	print("-" * 9)
	print('|', cells_matrix[0][0], cells_matrix[0][1], cells_matrix[0][2], '|')
	print('|', cells_matrix[1][0], cells_matrix[1][1], cells_matrix[1][2], '|')
	print('|', cells_matrix[2][0], cells_matrix[2][1], cells_matrix[2][2], '|')
	print("-" * 9)

print_board()
counter = 0
while counter <= 9:
	if counter == 9:
		print('Draw')
		break
	try:
		x,y = input("Enter the coordinates: ").split()
		if not x.isdigit() or not y.isdigit():
			print("You should enter numbers!")
		elif x.isdigit() and y.isdigit():
			x = int(x) - 1
			y = int(y) - 1
			if not ((x >= 0 and x <= 2) and (y >= 0 and y <= 2)):
				print("Coordinates should be from 1 to 3!")
			else:
				if cells_matrix[x][y] == ' ':
					if counter % 2 == 0:
						cells_matrix[x][y] = 'X'
					else:
						cells_matrix[x][y] = 'O'
					print_board()
					counter += 1
				else:
					print('This cell is occupied! Choose another one!')
	except:
		print('You should enter two numbers!')
	cells = ''.join([''.join([str(ele) for ele in sub]) for sub in cells_matrix])
	if game_state(cells) == None:
		continue
	else:
		print(game_state(cells))
		break
