def main_1(grid_1:list[str]) -> int:
    grid_1 = convert_to_grid(grid_1)
    # print(grid_1)
    grid_1, res = initial_fill(grid_1, 0)
    # print(f"Print grid is:\n" + "\n".join(" ".join(row) for row in grid_1))
    temp_res = -1
    for orig_char in range(10):
        new_char = orig_char + 1
        grid_1, res = fill(grid_1, str(orig_char), str(new_char), res)
        # print(f"Print grid is:\n" + "\n".join(" ".join(row) for row in grid_1))
    return res


def convert_to_grid(temp_str:list[str]) -> list:
    for i, line in enumerate(temp_str):
        temp_str[i] = list(line.strip())

    return temp_str


def initial_fill(grid:list[str], res:int) -> [list[str], int]:
    for y, line in enumerate(grid):
        grid[y] = line
        for x, char in enumerate(line):
            if char == "#":
                grid[y][x] = "1"
                res += 1

    return grid, res



def fill(grid:list[str], orig_char:str, new_char:str, res:int) -> [list[str], int]:
    for y, line in enumerate(grid):
        grid[y] = line
        for x, char in enumerate(line):
            if char == orig_char and is_valid_block(grid, y, x, orig_char, new_char):
                grid[y][x] = new_char
                res += 1

    return grid, res


def main_3(grid_1:list[str]) -> int:
    grid_1 = convert_to_grid(grid_1)
    # print(grid_1)
    grid_1, res = initial_fill(grid_1, 0)
    # print(f"Print grid is:\n" + "\n".join(" ".join(row) for row in grid_1))
    # print(res)
    for orig_char in range(11):
        new_char = orig_char + 1
        grid_1, res = fill_part_3(grid_1, str(orig_char), str(new_char), res)
        print(f"After Layer {orig_char + 1}, Total Removed: {res}")
        # print(f"Print grid is:\n" + "\n".join(" ".join(row) for row in grid_1))
    return res


def is_valid_block(grid:list[str], y:int, x:int, orig_char:str, new_char:str) -> bool:
    for y_offset, x_offset in [[-1,0], [1,0], [0, -1], [0, 1]]:
        try:
            if grid[y+y_offset][x+x_offset] != orig_char and grid[y+y_offset][x+x_offset] != new_char:
                return False
        except IndexError:
            pass
    return True


def fill_part_3(grid:list[str], orig_char:str, new_char:str, res:int) -> [list[str], int]:
    for y, line in enumerate(grid):
        grid[y] = line
        for x, char in enumerate(line):
            if char == orig_char and is_valid_block_part_3(grid, y, x, orig_char, new_char):
                grid[y][x] = new_char
                res += 1

    return grid, res


def is_valid_block_part_3(grid:list[str], y:int, x:int, orig_char:str, new_char:str) -> bool:
    for y_offset in [-1,0,1]:
        for x_offset in [-1,0,1]:
            # print(y_offset,x_offset)
            try:
                if grid[y+y_offset][x+x_offset] != orig_char and grid[y+y_offset][x+x_offset] != new_char:
                    return False
            except IndexError:
                pass
    return True


inp_1 = open('everybody_codes_e2024_q03_p1.txt').readlines()
inp_2 = open('everybody_codes_e2024_q03_p2.txt').readlines()
inp_3 = open('everybody_codes_e2024_q03_p3.txt').readlines()
# inp_3 = open('sample.txt').readlines()
print(f"The answer to part one is {main_1(inp_1)}")
print(f"The answer to part two is {main_1(inp_2)}")
print(f"The answer to part three is {main_3(inp_3)}")