def main_part_1(inp_1:str) -> int:
    return inp_1.count('B') + inp_1.count('C') * 3

def main_part_2(inp_2:str) -> int:
    res = 0
    values = {'A':0, 'B':1, 'C':3, 'D':5}
    for i in range(0,len(inp_2),2):
        res += values[inp_2[i]] if inp_2[i] in values.keys() else 0
        res += values[inp_2[i+1]] if inp_2[i+1] in values.keys() else 0
        if inp_2[i] in values.keys() and inp_2[i+1] in values.keys():
            res += 2
    return res
    # return len(inp_2) + main_part_1(inp_2) + inp_2.count('D') * 5 - inp_2.count('x') * 2

inp_1 = open('everybody_codes_e2024_q01_p1.txt').read()
inp_2 = open('everybody_codes_e2024_q01_p2.txt').read()
print(f"The answer to part one is {main_part_1(inp_1)}")
print(f"The answer to part two is {main_part_2(inp_2)}")