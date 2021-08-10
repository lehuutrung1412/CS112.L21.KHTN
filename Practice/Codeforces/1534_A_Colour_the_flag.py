def check_valid(row, col, value):
    flag = True
    if row != n-1:
        flag = flag and value != table[row+1][col]
    if col != m-1:
        flag = flag and value != table[row][col+1]
    if row != 0:
        flag = flag and value != table[row-1][col]
    if col != 0:
        flag = flag and value != table[row][col-1]
    return flag        

def isSolved(table):
    for row in range(n):
        if '.' in table[row]:
            return False
    return True

def solve(row, col):
    if isSolved(table):
        return True
    if col == m:
        return solve(row+1, 0)
    if table[row][col] == '.':
        for val in ['W', 'R']:
            if check_valid(row, col, val):
                table[row][col] = val
                if solve(row, col+1):
                    return True
            table[row][col] = '.'
    else:
        return solve(row, col+1)
    return False   

def printTable(table):
    for i in range(n):
        for j in range(m):
            print(table[i][j], end="")
        print()         

if __name__ == "__main__":    
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        table = []
        for r in range(n):
            temp = []
            temp[:0] = input()
            table.append(temp)
        if solve(0, 0):
            print('YES')
            printTable(table)
        else:
            print('NO')