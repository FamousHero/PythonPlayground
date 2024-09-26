# TBH quick little program to visualize pascals triangle for arbitrary n
# inspired by:
#   1 - https://www.youtube.com/watch?v=cUzklzVXJwo&ab_channel=Veritasium
#   2 - https://www.youtube.com/watch?v=gMlf1ELvRzc&ab_channel=Veritasium
#
# Idk man, Newtons a genius and vid 2 was cool, (vid 1 had math battles tho)
# Kinda hard not to get inspired
import sys


def pascalsTriangle(rows: int, current_row: int) -> None:

    padding = " " * current_row

    if current_row == rows-1: # at the top row
        print(padding+"1")
        return [1]
    elif current_row == rows - 2: # at the 2nd top row
        print(padding+" 1") # Extra padding since its 1 row above
        print(padding+"1 1")
        return [1,1]
    
    else:
        row_above = pascalsTriangle(rows, current_row+1) # print the row above
        row = ""
        row_array = []
        row_size = rows-current_row
        for i in range(row_size):
            if i == 0 or i == row_size-1:
                row += "1 "
                row_array.append(1)
            else:
                val = row_above[i-1] + row_above[i]
                row += str(val) + " "
                row_array.append(val)
        print(padding+row)
        return row_array
        
    

# might make it take the input from cli
if __name__ == "__main__":
    lines = input("How many rows would you like: ")
    try:
        lines = int(lines)
    except Exception as e:
        print("Invalid argument, expected a number")
        print(str(e))
        sys.exit(1)
    
    pascalsTriangle(lines, 0)        