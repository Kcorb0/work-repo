from random import randint


def create_grid(size):

    empty_grid = [[0 for i in range(1, size + 1)] for x in range(1, size + 1)]
    grid = [[0 for i in range(1, size + 1)] for x in range(1, size + 1)]

    row = 0
    col = 0

    while row < size:
        while col < size:
            mine = randint(0, 10)
            if mine <= 1:
                grid[row][col] = 1
            col += 1
        col = 0
        row += 1

    for i in empty_grid:
        print(i)
    print("\n")
    for i in grid:
        print(i)


grid1 = create_grid(10)