from typing import List

def average_contiguous_sub_arrays_with_target(arrays: List[int], target: int):
    window_sum = 0
    start = 0
    contiguous_averages = []

    for i in range(len(arrays)):
        window_sum += arrays[i]
        if i >= target-1: # i starts from zero hence the reduction of 1 from target
            contiguous_averages.append(window_sum/target)
            window_sum -= arrays[start]
            start += 1
    return contiguous_averages

def closest_to_zero(numbers: List[int]) -> int:
    closest_num = None
    closest_diff = float('inf')

    for num in numbers:
        if abs(num) < closest_diff:
            closest_num = num
            closest_diff = abs(num)
    return closest_num

def find_factorial(number: int) -> int:
    return 1 if number <= 1 else number * find_factorial(number - 1)

def find_number_negatives_in_target(numbers: List[int], target: int) -> List[int]:

    negative_numbers = []
    window_numbers = []
    start = 0
    for i in range(len(numbers)):
        window_numbers.append(numbers[i])
        if len(window_numbers) == target+1:
            count_negatives = count_negative_numbers(window_numbers)
            negative_numbers.append(count_negatives)
            window_numbers.pop(start)
            start += 1
    return negative_numbers

def count_negative_numbers(window_numbers: List[int]) -> int:
    return len(list(filter(lambda x: x < 0, window_numbers)))

def count_letter_sequence(word: str) -> str:
    sliding_window = ""
    generated_sequence = ""

    for i in range(len(word)):
        next_el = i + 1
        sliding_window += word[i]
        word += " "

        if word[i] != word[next_el]:
            generated_sequence += word[i]
            generated_sequence += str(len(sliding_window))
            sliding_window = ""
    return generated_sequence

# longest consonants 
def longest_string_no_vowel(word: str) -> str:

    result = ""
    max_result = ""
    if not word:
        return None 
    for i in range(len(word)):
        if word[i] not in get_vowels():
            result += word[i]
            if len(result) > len(max_result):
                max_result = result
        else:
            result = ""
    return max_result

def get_vowels() -> List[str]:
    return ['a', 'e', 'o', 'i', 'u']

# is duplicate number 
def find_duplicate(numbers: List[int], target: int) -> bool:
    return numbers.count(target) > 1


def find_max_sum(numbers: List[int], target: int) -> int:
    if numbers is None or target is None:
        return None
    max_value  = 0
    start = 0
    window_sum = 0
    for i in range(len(numbers)):
        window_sum += numbers[i]
        if i - start + 1 == target:
            max_value = max(max_value, window_sum)
            window_sum -= numbers[start]
            start += 1
    return max_value

import math
def smallest_sub_array_equal_target(numbers=None, target=None) -> int:
    start = 0
    window_sum = 0
    min_sum = math.inf

    if numbers is None or target is None:
        return None 

    for i in range(len(numbers)):
        window_sum += numbers[i]
        while window_sum >= target:
            min_sum = min(min_sum, i - start + 1)
            window_sum -= numbers[start]
            start += 1
    return 0 if min_sum == math.inf else min_sum


def find_min_max_diff(numbers, target) -> float:
    start = 0
    window_sum = 0
    min_value = math.inf
    max_value = 0
    for i in range(len(numbers)):
        window_sum += numbers[i]
        if i - start + 1 == target:
            min_value = min(min_value, window_sum)
            max_value = max(max_value, window_sum)
            window_sum -= numbers[start]
            start += 1
    return (max_value - min_value) / 2

def perfect_number(number: int) -> bool:
    return int(str(number)[::-1]) == number

def find_middle_number(numbers: List[int]) -> int:
    if len(numbers) % 2 != 0:
        return numbers[len(numbers)//2]
    return (numbers[len(numbers)//2] + numbers[len(numbers)//2 - 1]) / 2 


def get_last_digits(number: int, digit_size: int) -> List[int]:
    num_str = str(number)
    return [ int(x) for x in num_str[len(num_str)-digit_size: ]]



# number of pairs 
# two point techniques 
# fast slow pointers 
# merge intervals 
# python built in functions for mastering my grafts 


# TODAYS LESSON ON DATA STRUCTURES AND ALGORITHMS 1st August, 2023
def count_negatives(numbers: List[int], target: int) -> List[int]:
    window_el = []
    start = 0
    negatives = []

    for i in range(len(numbers)):
        window_el.append(numbers[i])
        if len(window_el) == target+1:
            nega = len(list(filter(lambda x: x < 0, window_el)))
            negatives.append(nega)
            window_el.pop(start)
            start += 1
    return negatives


print(count_negatives([-1, 2, -2, 3, 5, -7, -5], target=3))

 

