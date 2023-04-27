# board layout
# dimensions: 8 x 8
# -------------------------
# | 0| 1| 2| 3| 4| 5| 6| 7|
# -------------------------
# | 8| 9|10|11|12|13|14|15|
# -------------------------
# |16|17|18|19|20|21|22|23|
# -------------------------
# |24|25|26|27|28|29|30|31|
# -------------------------
# |32|33|34|35|36|37|38|39|
# -------------------------
# |40|41|42|43|44|45|46|47|
# -------------------------
# |48|49|50|51|52|53|54|55|
# -------------------------
# |56|57|58|59|60|61|62|63|
# -------------------------

#grid is 8 x 8
grid_dimensions = 8

def is_valid_position(r, c):
    return r >= 0 and c >= 0 and r < grid_dimensions and c < grid_dimensions

# can move two squares in any direction and one square perpendicularly
def get_valid_moves(r, c):
    #knights have 8 possible moves, described by deltas below
    delta_r = [2, 2, -2, -2, 1, 1, -1, -1]
    delta_c = [1, -1, 1, -1, 2, -2, 2, -2]
    
    #get potential destinations of the knight from (r, c)
    destinations = []
    for i in range(grid_dimensions):
        dest_r = r+delta_r[i]
        dest_c = c+delta_c[i]
        #filter out invalid destinations
        if is_valid_position(dest_r, dest_c):
            destinations.append((dest_r, dest_c))
    return destinations

# count the number of moves needed to solve the 
# puzzle moving like a knight from chess
# BFS seems like a simple solution
def solution(src, dest):
    #translate src and dest to line up with grid coordinates
    src_r = src/grid_dimensions
    src_c = src%grid_dimensions
    
    dest_r = dest/grid_dimensions
    dest_c = dest%grid_dimensions
    
    #keep track of visited nodes so we don't repeat squares
    visited = [[False for c in range(grid_dimensions)]
               for r in range(grid_dimensions)]
    visited[src_r][src_c] = True
    
    # BFS Queue 
    queue = []
    queue.append((src_r, src_c, 0))
    
    while len(queue) > 0:
        #get current square from the queue
        cur_square = queue.pop(0)
        row = cur_square[0]
        col = cur_square[1]
        distance = cur_square[2]
        
        # visited[row][col] = True
        
        #check if we're at the destination
        if row == dest_r and col == dest_c:
            return distance
        
        #add valid moves to the queue
        moves = get_valid_moves(row, col)
        for i in range(len(moves)):
            move_row = moves[i][0]
            move_col = moves[i][1]
            if not visited[move_row][move_col]:
                #mark squares as visited so we don't add 
                #duplicates to the queue
                visited[move_row][move_col] = True
                queue.append((move_row, move_col, distance+1))