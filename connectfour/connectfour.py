def who_is_winner(pieces_position_list):
    coordinates = "ABCDEFG"
    board = [[] for _ in range(7)]
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

    def getRC(col, row):
        if 0 <= col < 7 and 0 <= row < len(board[col]):
            return board[col][row]
        return None

    def count_in_direction(col, row, dc, dr, color):
        count = 0
        while getRC(col, row) == color:
            count += 1
            col += dc
            row += dr
        return count

    # process moves sequentially
    for move in pieces_position_list:
        col = coordinates.index(move[0])
        color = "Yellow" if "Yellow" in move else "Red"
        board[col].append(color)
        row = len(board[col]) - 1  # just-placed piece

        # check all directions
        for dc, dr in directions:
            total = (
                count_in_direction(col, row, dc, dr, color)
                + count_in_direction(col, row, -dc, -dr, color)
                - 1  # subtract double-counted center
            )
            if total >= 4:
                return color  # winner found

    return "Draw"

# Community Solution
  
# COLUMNS, ROWS = 'ABCDEFG', range(6)
# LINES = [{(COLUMNS[i+k], ROWS[j]) for k in range(4)}
#            for i in range(len(COLUMNS) - 3) for j in range(len(ROWS))] \
#         + [{(COLUMNS[i], ROWS[j+k]) for k in range(4)}
#            for i in range(len(COLUMNS)) for j in range(len(ROWS) - 3)] \
#         + [{(COLUMNS[i+k], ROWS[j+k]) for k in range(4)}
#            for i in range(len(COLUMNS) - 3) for j in range(len(ROWS) - 3)] \
#         + [{(COLUMNS[i+k], ROWS[j-k]) for k in range(4)}
#            for i in range(len(COLUMNS) - 3) for j in range(3, len(ROWS))]

# def who_is_winner(pieces_positions):
#     players = {}
#     board = dict.fromkeys(COLUMNS, 0)
#     for position in pieces_positions:
#         column, player = position.split('_')
#         pos = (column, board[column])
#         board[column] += 1
#         players.setdefault(player, set()).add(pos)
#         if any(line <= players[player] for line in LINES):
#             return player
#     return "Draw"
