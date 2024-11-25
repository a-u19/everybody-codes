def main_1(inp_grid:list[str], rounds:int) -> list[int]:
    grid = [list(map(int, line.strip().split())) for line in inp_grid]
    print(f"Starting grid is: {grid}")
    for round in range(rounds):
        res = []
        grid = place_num(grid, round)
        for row in grid:
            res.append(row[0])
        print(f"After round {round + 1}, the res is {res}")

    return res

def place_num(grid:list[list[int]], orig_index:int) -> (list[list[int]],bool):
    orig_index = orig_index % 4
    num = grid[orig_index].pop(0)
    temp_num = num
    line_lens = [len(line) for line in grid]
    line_lens = [item for item in line_lens for _ in range(2)]
    orig_index = (orig_index + 1) % 4
    left_side = False
    print(temp_num, line_lens[orig_index*2 % len(grid)])
    while temp_num >= line_lens[orig_index*2 % len(grid)]:
        temp_num -= line_lens[orig_index*2 % len(grid)]
        left_side = not left_side
        orig_index = (orig_index + 1) % 4
    if not left_side:
        temp_num += 1
        print("doesn't end on left")
    # print(f"Grid before is: {grid}")
    grid[orig_index] = grid[orig_index][:temp_num-1] + [num] + grid[orig_index][temp_num-1:]
    # print(f"Grid after is: {grid}")

    return grid


inp_1 = open('sample.txt').readlines()
print(f"The answer to part 1 is {main_1(inp_1,5)}")
