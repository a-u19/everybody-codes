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

inp_1 = open('everybody_codes_e2024_q02_p1.txt').readlines()
inp_2 = open('everybody_codes_e2024_q02_p2.txt').readlines()
print(f"The answer to part one is {main_1(inp_1[2], inp_1[0].split(":")[1].strip().split(','))}")
print(f"The answer to part two is {main_2(inp_2[2:], inp_2[0].split(":")[1].strip().split(','))}")