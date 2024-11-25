def main_1(nums:list) -> int:
    return sum(nums) - (min(nums) * len(nums))


def main_3(nums:list) -> int:
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(median - num) for num in nums)

input_1 = list(int(num) for num in (open('everybody_codes_e2024_q04_p1.txt').readlines()))
input_2 = list(int(num) for num in (open('everybody_codes_e2024_q04_p2.txt').readlines()))
input_3 = list(int(num) for num in (open('everybody_codes_e2024_q04_p3.txt').readlines()))
# input_3 = list(int(num) for num in (open('sample.txt').readlines()))
print(f"The answer to part 1 is {main_1(input_1)}")
print(f"The answer to part 2 is {main_1(input_2)}")
print(f"The answer to part 3 is {main_3(input_3)}")