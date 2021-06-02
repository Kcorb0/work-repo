def t_path(inp, step_x, step_y):

    path_grid = [i for i in [line.replace("\n", "") for line in open(inp, "r")]]
    width = len(path_grid[0])
    pos_x = 0
    tree_cnt = 0

    for pos_y in range(0, len(path_grid), step_y):
        if path_grid[pos_y][pos_x] == "#":
            tree_cnt += 1
        pos_x = (pos_x + step_x) % width
    return tree_cnt


inputs = "part_3/input.txt"

print(f"Part 1 answer: {t_path(inputs, 3, 1)}")
print(
    f"Part 2 answer: {t_path(inputs, 1, 1)*t_path(inputs, 3, 1)*t_path(inputs, 5, 1)*t_path(inputs, 7, 1)*t_path(inputs, 1, 2)}"
)
