import time
start_time = time.time()
import re


def main_1(inp_str_1: str, words: list[str]) -> int:
    res = 0
    inp_str_1 = "".join(inp_str_1.split(" "))
    for word in words:
        res += inp_str_1.count(word)
    return res


def main_2(inp_str_2: list[str], words: list[str]):
    used_indices = set()
    inp_str_2 = " ".join(temp_str.strip() for temp_str in inp_str_2)
    rev_inp_str_2 = inp_str_2[::-1]

    used_indices = count_symbols(words, inp_str_2, used_indices, False)
    used_indices = count_symbols(words, rev_inp_str_2, used_indices, True)

    return len(used_indices)


def count_symbols(words: list[str], str: str, used_indices: set, rev: bool) -> set:
    for word in words:
        for i in re.finditer(word, str):
            for x in range(i.start(), i.end()):
                if rev:
                    x = len(str) - 1 - x
                if x not in used_indices:
                    used_indices.add(x)
    return used_indices


def main_3(inp_str_3: list[str], words: list[str]) -> int:
    used_indices = set()

    # Add reversed words for bidirectional matching
    words = words + [word[::-1] for word in words]
    grid = convert_to_grid(inp_str_3)

    # print("Words to search:", words)
    # print("Grid:")
    # print("\n".join(" ".join(row) for row in grid))

    # Check vertically and horizontally
    used_indices = check_vertical(grid, words, used_indices)
    used_indices = check_horizontal(grid, words, used_indices)

    # print("Matched indices:", sorted(used_indices))
    return len(used_indices)


def convert_to_grid(temp_str: list[str]) -> list[list[str]]:
    return [list(line.strip()) for line in temp_str]


def check_vertical(grid: list[list[str]], words: list[str], used_indices: set) -> set:
    for col in range(len(grid[0])):
        # Create a string for the current column
        column_str = ''.join(row[col] for row in grid)

        for word in words:
            # Search for the word manually
            start = 0
            while True:
                start = column_str.find(word, start)
                if start == -1:  # No more matches
                    break
                # Add all indices corresponding to the found word
                for x in range(len(word)):
                    used_indices.add((start + x, col))
                start += 1  # Move forward to look for the next occurrence

    return used_indices


def check_horizontal(grid: list[list[str]], words: list[str], used_indices: set) -> set:
    for row_index, row in enumerate(grid):
        # Create a string for the current row with wrap-around
        row_str = ''.join(row * 2)

        for word in words:
            # Search for the word manually
            start = 0
            while True:
                start = row_str.find(word, start)
                if start == -1:  # No more matches
                    break
                # Add all indices corresponding to the found word
                for y in range(len(word)):
                    used_indices.add((row_index, (start + y) % len(row)))
                start += 1  # Move forward to look for the next occurrence

    return used_indices


inp_1 = open('everybody_codes_e2024_q02_p1.txt').readlines()
inp_2 = open('everybody_codes_e2024_q02_p2.txt').readlines()
inp_3 = open('everybody_codes_e2024_q02_p3.txt').readlines()
# inp_3 = open('sample.txt').readlines()
print(f"The answer to part one is {main_1(inp_1[2], inp_1[0].split(":")[1].strip().split(','))}")
print(f"The answer to part two is {main_2(inp_2[2:], inp_2[0].split(":")[1].strip().split(','))}")
print(f"The answer to part three is {main_3(inp_3[2:], inp_3[0].split(":")[1].strip().split(','))}")
print(f"Time taken is {time.time() - start_time}s")
