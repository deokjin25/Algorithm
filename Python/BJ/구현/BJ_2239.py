import sys
input = sys.stdin.readline

sudoku = []
for i in range(9):
    line = input().strip()
    sudoku.append([int(x) for x in line])

row_used = [set() for _ in range(9)]
col_used = [set() for _ in range(9)]
box_used = [set() for _ in range(9)]

for i in range(9):
    for j in range(9):
        if sudoku[i][j] != 0:
            n = sudoku[i][j]
            row_used[i].add(n)
            col_used[j].add(n)
            box_used[(i//3)*3 + (j//3)].add(n)

empty = [(i,j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def solve(idx):
    if idx == len(empty):
        for row in sudoku:
            print(''.join(map(str, row)))
        return True

    i, j = empty[idx]
    b = (i//3)*3 + (j//3)

    possible = {1,2,3,4,5,6,7,8,9} - row_used[i] - col_used[j] - box_used[b]

    for num in sorted(possible):
        sudoku[i][j] = num
        row_used[i].add(num)
        col_used[j].add(num)
        box_used[b].add(num)

        if solve(idx+1):
            return True

        sudoku[i][j] = 0
        row_used[i].remove(num)
        col_used[j].remove(num)
        box_used[b].remove(num)

    return False

solve(0)