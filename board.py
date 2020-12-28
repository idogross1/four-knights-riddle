class board:
    game_won = False
    
    chess_board = [
    [' ',' 1 ',' 2 ',' 3 '],
    ['a ','w1','|','  ','|','w2'],
    ['  ','--','|','--','|','--'],
    ['b ','  ','|','  ','|','  '],
    ['  ','--','|','--','|','--'],
    ['c ','b1','|','  ','|','b2']
    ]

    location = [0, 5, 6, 1, 8, 3, 2, 7]

    def black_turn(self):
        piece = 'b1'
        xy = self.find_piece_location(piece)
        index = self.xy_to_index(xy)
        next_spot = self.find_next_spot(piece, index)
        xy_new = self.spot_to_xy(next_spot)
        self.update_board(piece, xy_new)


    def find_piece_location(self, piece):
        for i, inner_list in enumerate(self.chess_board):
            for j, cell in enumerate(inner_list):
                if cell == piece:
                    return [i,j]


    def find_next_spot(self, piece, index):
        if piece == 'b1':
            for i in location:
                if location[i] == index:
                    if index == 0:
                        pass
                    else:
                        pass
        else:
            pass

    def white_turn(self, piece, spot):
        xy = self.spot_to_xy(spot) #convert spot to index
        if(self.is_spot_empty(xy)): #if the spot is empty
            self.update_board(piece, xy)
            
    def update_board(self, piece, xy):
        self.delete_from_old_spot(piece)
        self.chess_board[xy[0]] [xy[1]] = piece

    def delete_from_old_spot(self, piece):
        for i, inner_list in enumerate(self.chess_board):
            for j, cell in enumerate(inner_list):
                if cell == piece:
                    self.chess_board[i][j] = '  '
                    break

    def is_spot_empty(self, xy):
        if (self.chess_board[xy[0]][xy[1]] == '  '):
            return True
        return False
        
    def spot_to_index(self, spot): 
    	return { 
		'a1': 0, 
		'a2': 1, 
		'a3': 2,
        'b1': 3, 
		'b3': 5,
        'c1': 6, 
		'c2': 7, 
		'c3': 8 
	    }.get(spot) 

    def spot_to_xy(self, spot): 
    	return { 
		'a1': [1,1], 
		'a2': [1,3], 
		'a3': [1,5],
        'b1': [3,1], 
		'b3': [3,5],
        'c1': [5,1], 
		'c2': [5,3], 
		'c3': [5,5] 
	    }.get(spot)

    def xy_to_index(self, xy): 
    	return { 
		[1,1]: 0, 
		[1,3]: 1,
		[1,5]: 2,
        [3,1]: 3,
		[3,5]: 5,
        [5,1]: 6,
		[5,3]: 7,
		[5,5]: 8
	    }.get(xy)

    def print_board(self):
        for row in self.chess_board:
            print("".join(row))


    