import tkinter as tk
from tkinter import messagebox

# Check if a number can be placed
def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num:
            return False

    for x in range(9):
        if board[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

# Solve Sudoku using backtracking
def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num

                        if solve(board):
                            return True

                        board[row][col] = 0
                return False
    return True

# Get values from GUI
def solve_sudoku():
    board = []

    try:
        for i in range(9):
            row = []
            for j in range(9):
                value = entries[i][j].get()
                row.append(int(value) if value else 0)
            board.append(row)

        if solve(board):
            for i in range(9):
                for j in range(9):
                    entries[i][j].delete(0, tk.END)
                    entries[i][j].insert(0, str(board[i][j]))
        else:
            messagebox.showinfo("Result", "No solution exists!")

    except ValueError:
        messagebox.showerror("Error", "Enter only numbers!")

# Clear board
def clear_board():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)

# GUI Window
root = tk.Tk()
root.title("Sudoku Solver")
root.geometry("450x550")

entries = []

for i in range(9):
    row = []
    for j in range(9):
        e = tk.Entry(root, width=3, font=("Arial", 18), justify="center")
        e.grid(row=i, column=j, padx=2, pady=2)
        row.append(e)
    entries.append(row)

solve_btn = tk.Button(
    root,
    text="Solve Sudoku",
    command=solve_sudoku,
    font=("Arial", 14)
)
solve_btn.grid(row=10, column=0, columnspan=4, pady=20)

clear_btn = tk.Button(
    root,
    text="Clear",
    command=clear_board,
    font=("Arial", 14)
)
clear_btn.grid(row=10, column=5, columnspan=4, pady=20)

root.mainloop()