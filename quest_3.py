def main_1(grid_1:list[str]) -> int:
    grid_1, res = fill(grid_1, "#", "1")

def fill(grid:list[str], orig_char:str, new_char:str, res:int) -> tuple[list[str], int]:
    for y, line in enumerate(grid):
        line = line.strip()
        grid[y] = line
        for x, char in line:
            if char == orig_char and is_valid_block(grid, y, x):
                grid[y][x] = new_char

    return tuple((grid, res))

def is_valid_block(grid:list[str], y:int, x:int) -> bool:
    for y_offset in [-1, 0, 1]:
        for x_offset in [-1, 0, 1]:
            if grid[y+y_offset][x+x_offset] != grid[y][x]:
                return False
    return True

inp_1 = open('sample.txt').readlines()
main_1(inp_1)