import tkinter as tk
import time

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True

    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            update_ui(board)
            root.update()
            time.sleep(0.01)

            if solve_sudoku(board):
                return True

            board[row][col] = 0
            update_ui(board)
            root.update()
            time.sleep(0.01)

    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def update_ui(board):
    for i in range(9):
        for j in range(9):
            entry = entry_grid[i][j]
            entry.delete(0, tk.END)
            entry.insert(0, str(board[i][j]))
            entry.update()

def set_predefined_inputs(puzzle):
    for i in range(9):
        for j in range(9):
            entry = entry_grid[i][j]
            value = puzzle[i][j]
            if value != 0:
                entry.insert(0, str(value))

# Initialize the UI
root = tk.Tk()
root.title("Sudoku Solver")

font = ("Arial", 14)
bg_color = "#F2F2F2"
button_color = "#4CAF50"

heading_label = tk.Label(root, text="SUDOKU Solver", font=("Helvetica", 20), padx=10, pady=10, bg=bg_color)
heading_label.grid(row=0, column=0, columnspan=9)

sudoku_board = [[0] * 9 for _ in range(9)]
entry_grid = []

for i in range(9):
    row_entries = []
    for j in range(9):
        entry = tk.Entry(root, font=font, width=6)
        entry.grid(row=i + 1, column=j, padx=2, pady=2)
        row_entries.append(entry)
    entry_grid.append(row_entries)

predefined_puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

set_predefined_inputs(predefined_puzzle)

solve_button = tk.Button(root, text="Solve Sudoku", font=("Helvetica", 16), bg=button_color, fg="white", command=lambda: solve_sudoku(sudoku_board))
solve_button.grid(row=11, columnspan=9, padx=10, pady=10)

root.configure(bg=bg_color)

root.mainloop()
