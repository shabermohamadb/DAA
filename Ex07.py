# N-Queens - All Possible Solutions
n = int(input("Enter N: "))
board = [-1] * n
count = 0

def solve(row):
    global count
    if row == n:
        count += 1
        print(board)
        return

    for col in range(n):
        safe = True
        for r in range(row):
            if board[r] == col or abs(board[r] - col) == row - r:
                safe = False
                break
        if safe:
            board[row] = col
            solve(row + 1)

solve(0)
print("Total solutions:", count)
