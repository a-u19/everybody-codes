import re


def main_1(inp_str_1:str, words:list[str]) -> int:
    res = 0
    inp_str_1 = "".join(inp_str_1.split(" "))
    for word in words:
        res += inp_str_1.count(word)
    return res


def main_2(inp_str_2:list[str], words:list[str]):
    used_indices = set()
    inp_str_2 = " ".join(temp_str.strip() for temp_str in inp_str_2)
    rev_inp_str_2 = inp_str_2[::-1]

    used_indices = count_symbols(words, inp_str_2, used_indices, False)
    used_indices = count_symbols(words, rev_inp_str_2, used_indices, True)


    return len(used_indices)


def count_symbols(words:list[str], str:str, used_indices:set, rev:bool) -> set:
    for word in words:
        for i in re.finditer(word, str):
            for x in range(i.start(), i.end()):
                if rev:
                    x = len(str) - 1 - x
                if x not in used_indices:
                    used_indices.add(x)
    return used_indices


def main_3(inp_str_3:list[str], words:list[str]) -> int:
    used_indices = set()

    grid = convert_to_grid(inp_str_3)
    # print(f"Print grid is:\n" + "\n".join(" ".join(row) for row in grid))
    # print(f"Print grid is:\n" + "\n".join(" ".join(row) for row in reversed(grid)))
    for rev in True, False:
        used_indices = check_vertical(grid, words, used_indices, rev)
        used_indices = check_horizontal(grid, words, used_indices, rev)

    return len(used_indices)


def convert_to_grid(temp_str:list[str]) -> list:
    for i, line in enumerate(temp_str):
        temp_str[i] = list(line.strip())

    return temp_str


def check_vertical(grid:list[str], words:list[str], used_indices:set, rev:bool):
    if not rev:
        for col in range(len(grid[0])):
            each_col = []
            for row in range(len(grid)):
                each_col.append(grid[row][col])
            each_col = ''.join(each_col)

            # print(each_col)

            for word in words:
                for i in re.finditer(word, each_col):
                    for x in range(i.start(), i.end()):
                        if tuple((x,col)) not in used_indices:
                            used_indices.add(tuple((x, col)))

    else:
        for col in range(len(grid[0]) - 1, -1, -1):
            each_col = []
            for row in range(len(grid) - 1, -1, -1):
                each_col.append(grid[row][col])
            each_col = ''.join(each_col)

            # print(each_col)

            for word in words:
                for i in re.finditer(word, each_col):
                    for x in range(i.start(), i.end()):
                        if tuple((x, col)) not in used_indices:
                            used_indices.add(tuple((x, col)))

    return used_indices

def check_horizontal(grid:list[str], words:list[str], used_indices:set, rev:bool) -> set:
    if not rev:
        for col, row in enumerate(grid):
            temp_row = row*2
            temp_row = ''.join(temp_row)

            for word in words:
                for i in re.finditer(word, temp_row):
                    for x in range(i.start(), i.end()):
                        x = x % len(row)
                        if tuple((col, x)) not in used_indices:
                            used_indices.add(tuple((col, x)))

    else:
        for col, row in enumerate(grid):
            row = row[::-1]
            temp_row = row*2
            temp_row = ''.join(temp_row)

            for word in words:
                for i in re.finditer(word, temp_row):
                    for x in range(i.start(), i.end()):
                        x = x % len(row)
                        x = len(row) - 1 - x
                        if tuple((col, x)) not in used_indices:
                            used_indices.add(tuple((col, x)))


    return used_indices


inp_1 = open('everybody_codes_e2024_q02_p1.txt').readlines()
inp_2 = open('everybody_codes_e2024_q02_p2.txt').readlines()
inp_3 = open('everybody_codes_e2024_q02_p3.txt').readlines()
# inp_3 = open('sample.txt').readlines()
print(f"The answer to part one is {main_1(inp_1[2], inp_1[0].split(":")[1].strip().split(','))}")
print(f"The answer to part two is {main_2(inp_2[2:], inp_2[0].split(":")[1].strip().split(','))}")
print(f"The answer to part three is {main_3(inp_3[2:], inp_3[0].split(":")[1].strip().split(','))}")