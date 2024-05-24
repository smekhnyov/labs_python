import random

def generate_maze(rows, cols, start_row, start_col, end_row, end_col):
    maze = [["#" for _ in range(cols)] for _ in range(rows)]

    def carve(row, col):
        maze[row][col] = " "
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(directions)
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 < r < rows and 0 < c < cols and maze[r][c] == "#":
                maze[row + dr // 2][col + dc // 2] = " "
                carve(r, c)

    carve(start_row, start_col + 1)
    maze[start_row][start_col] = "S"
    maze[end_row][end_col] = "E"
    return maze

def print_hash(maze):
    for row in maze:
        print("".join(row))

def print_maze(maze, rows, cols, start_row, start_col, end_row, end_col):
    maze[0][0] = "┌"
    maze[0][cols - 1] = "┐"
    maze[rows - 1][0] = "└"
    maze[rows - 1][cols - 1] = "┘"
    for i in range(1, rows - 1):
        maze[i][0] = "│"
        maze[i][cols - 1] = "│"
    for j in range(1, cols - 1):
        maze[0][j] = "─"
        maze[rows - 1][j] = "─"
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if maze[i][j] == "#":
                if maze[i - 1][j] in ["#", "│"] and maze[i + 1][j] in ["#", "│"] and maze[i][j - 1] in ["#", "─"] and maze[i][j + 1] in ["#", "─"]:
                    maze[i][j] = "┼"
                elif maze[i - 1][j] in ["#", "│"] and maze[i][j - 1] in ["#", "─"] and maze[i + 1][j] in ["#", "│"]:
                    maze[i][j] = "┤"
                elif maze[i - 1][j] in ["#", "│"] and maze[i][j + 1] in ["#", "─"] and maze[i + 1][j] in ["#", "│"]:
                    maze[i][j] = "├"
                elif maze[i][j - 1] in ["#", "─"] and maze[i][j + 1] in ["#", "─"] and maze[i - 1][j] in ["#", "│"]:
                    maze[i][j] = "┴"
                elif maze[i][j - 1] in ["#", "─"] and maze[i][j + 1] in ["#", "─"] and maze[i + 1][j] in ["#", "│"]:
                    maze[i][j] = "┬"
                elif maze[i - 1][j] in ["│", "#"] and maze[i][j + 1] in ["#", "─"] and maze[i][j - 1] == " " and maze[i + 1][j] == " ":
                    maze[i][j] = "└"
                elif maze[i - 1][j] in ["│", "#"] and maze[i][j - 1] in ["#", "─"] and maze[i][j + 1] == " " and maze[i + 1][j] == " ":
                    maze[i][j] = "┘"
                elif maze[i + 1][j] in ["│", "#"] and maze[i][j + 1] in ["#", "─"] and maze[i][j - 1] == " " and maze[i - 1][j] == " ":
                    maze[i][j] = "┌"
                elif maze[i + 1][j] in ["│", "#"] and maze[i][j - 1] in ["#", "─"] and maze[i][j + 1] == " " and maze[i - 1][j] == " ":
                    maze[i][j] = "┐"
                elif maze[i][j + 1] in ["#", "─", "┘", "┐", "┤", "┼", "┴", "┬"] or maze[i][j - 1] in ["#", "─", "┌", "└", "├", "┼", "┴", "┬"]:
                    maze[i][j] = "─"
                elif maze[i + 1][j] in ["#", "│", "┘", "└", "┤", "┼", "├", "┴"] or maze[i - 1][j] in ["#", "│", "┌", "┐", "┤", "┼", "├", "┬"]:
                    maze[i][j] = "│"
    for i in range(1, rows - 1):
        if maze[i][cols - 1] in ["#", "│"] and maze[i][cols - 2] in ["#", "─", "┌", "└"]:
            maze[i][cols - 1] = "┤"
        elif maze[i][0] in ["#", "│"] and maze[i][1] in ["#", "─", "┘", "┐"]:
            maze[i][0] = "├"
    for j in range(1, cols - 1):
        if maze[rows - 1][j] in ["#", "─"] and maze[rows - 2][j] in ["#", "│", "┌", "┐"]:
            maze[rows - 1][j] = "┴"
        elif maze[0][j] in ["#", "─"] and maze[1][j] in ["#", "│", "┘", "└"]:
            maze[0][j] = "┬"
    maze[start_row][start_col] = "S"
    maze[end_row][end_col] = "E"
    for row in maze:
        print("".join(row))

def main():
    rows = 19#int(input("Enter the number of rows: "))
    cols = 39#int(input("Enter the number of columns: "))
    start_row = 1
    start_col = 0
    end_row = rows - 2
    end_col = cols - 1
    maze = generate_maze(rows, cols, start_row, start_col, end_row, end_col)
    #print_hash(maze)
    print_maze(maze, rows, cols, start_row, start_col, end_row, end_col)

if __name__ == "__main__":
    main()
