def mine_gold(arr, num_row, num_col):
    # Bottom up
    max_table = [[0 for _ in range(num_col)] for _ in range(num_row)]
    for row in range(num_row):
        max_table[row][num_col-1] = arr[row][num_col-1]
    for col in range(num_col - 2, -1, -1):
        for row in range(num_row):
            if (col == num_col-1):
                right = 0
            else:
                right = max_table[row][col+1]
            if (row == 0 or col == num_col-1):
                right_up = 0
            else:
                right_up = max_table[row-1][col+1]
            if (row == num_row-1 or col == num_col-1):
                right_down = 0
            else:
                right_down = max_table[row+1][col+1]
            max_table[row][col] = arr[row][col] + max(right, right_up, right_down)
    return max([row[0] for row in max_table])

arr = [[1, 3, 1, 5],
       [2, 2, 4, 1],
       [5, 0, 2, 3],
       [0, 6, 1, 2]]

print(mine_gold(arr, 4, 4))