def t_path(inp):

    inp_rows = [line.replace("\n", "") for line in open(inp, "r")]

    path_grid = [i for i in inp_rows]
    width = len(path_grid[0])
    pos_x = 0
    tree_cnt = 0

    for pos_y in range(0, len(path_grid)):
        if path_grid[pos_y][pos_x] == "#":
            tree_cnt += 1
        pos_x = (pos_x + 3) % width
    return tree_cnt


print(t_path("part_3/input.txt"))
