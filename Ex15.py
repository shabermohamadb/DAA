# N-Queens - Print One Possible Solution
n = int(input("Enter N: "))
board = [-1] * n

def solve(row):
    if row == n:
        return True

    for col in range(n):
        safe = True
        for r in range(row):
            if board[r] == col or abs(board[r] - col) == row - r:
                safe = False
                break
        if safe:
            board[row] = col
            if solve(row + 1):
                return True
    return False

if solve(0):
    print("Solution:", board)
else:
    print("No Solution")
