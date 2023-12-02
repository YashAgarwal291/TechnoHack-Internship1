import tkinter as tk
from tkinter import messagebox
import numpy as np

board = np.array([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])
current_player = 'X'

def place(row, col, button):
    global current_player
    if board[row][col] == '-':
        board[row][col] = current_player
        button.config(text=current_player)
        if check_winner():
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            reset_board()
        elif '-' not in board:
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            reset_board()
        else:
            current_player = 'O' if current_player == 'X' else 'X'

def check_winner():
    for i in range(3):
        if all(board[i, :] == current_player) or all(board[:, i] == current_player):
            return True
    if all(np.diag(board) == current_player) or all(np.diag(np.fliplr(board)) == current_player):
        return True
    return False

def reset_board():
    global board, current_player
    board = np.array([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']])
    current_player = 'X'
    for button_row in buttons:
        for button in button_row:
            button.config(text='-')

root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = [[None, None, None] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text='-', font=('normal', 20), width=6, height=2,
                                   command=lambda row=i, col=j, button=buttons[i][j]: place(row, col, button))
        buttons[i][j].grid(row=i, column=j)

reset_button = tk.Button(root, text="Reset", font=('normal', 14), width=10, height=2, command=reset_board)
reset_button.grid(row=3, column=1)

root.mainloop()
