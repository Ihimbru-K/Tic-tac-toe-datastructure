# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 00:13:04 2022

@author: mon pc
"""


theBoard = {"top-r": " ", "top-m": " ", "top-l": " ", "mid-l": " ", "mid-m": " ", "mid-r": " ", "low-l":" ", "low-m": " ", "low-r": " "}
def printBoard(board):
    print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
    print("-+-+-")
    print(board["mid-l"] + '|' + board['mid-m'] + '|' + board["mid-r"])
    print("-+-+-")
    print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])
turn = "X"

for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == "X":
        turn = "0"
    else:
        turn = "X"
    printBoard(theBoard)