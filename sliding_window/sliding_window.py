from typing import List, Set
import math

"""
The concept of a sliding window is a technique commonly used in computer science and algorithms to process or analyze elements in a sequence, such as an array or a string. It involves selecting a fixed-size subset or window of elements from the sequence and moving that window through the sequence one step at a time, often in a sequential manner.

Here's a more detailed breakdown of how the sliding window works:

1. **Window Initialization:**
   - Define the size of the window. This is typically a fixed number, and it determines how many elements are included in each window.

2. **Initial Position:**
   - Place the window at the beginning of the sequence. The window starts with the first set of elements from the sequence.

3. **Processing:**
   - Perform a specific operation or analysis on the elements within the current window.
   - This operation could involve calculations, comparisons, or any other relevant processing depending on the problem you are trying to solve.

4. **Window Movement:**
   - Slide the window to the next position in the sequence.
   - The window moves forward by one element at a time.

5. **Repeat:**
   - Repeat the processing step on the new set of elements within the updated window.
   - Continue moving the window until it reaches the end of the sequence.

The sliding window technique is often used to efficiently solve problems that involve analyzing or processing subarrays or substrings. It is particularly useful in situations where a brute-force approach would be inefficient due to redundant calculations.

Common applications of sliding window technique include:

- **String Matching:** Finding a substring or pattern within a larger string efficiently.
- **Maximum/Minimum Subarray:** Finding the maximum or minimum sum or product of a contiguous subarray.
- **Substring Problems:** Solving problems that involve finding a substring satisfying certain conditions.

The sliding window technique is valued for its simplicity, efficiency, and the ability to optimize algorithms for specific types of problems.
"""


"""
Given an array, find the average of all contiguous sub-arrays of size ‘target’ in it.
Here, we are asked to find the average of all contiguous sub-arrays of size ‘5’ in the given array. Let’s solve this:
For the first 5 numbers (subarray from index 0-4), the average is: 
For the next 5 numbers (subarray from index 2-6), the average is: 

Here is the final output containing the averages of all contiguous sub-arrays of size 5:
Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], target=5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]
"""


# def average_contiguous_sub_arrays_with_target(arrays: List[int], target: int):
#     window_sum = 0
#     start = 0
#     contiguous_averages = []

#     for i in range(len(arrays)):
#         window_sum += arrays[i]
#         if i >= target - 1:  # i starts from zero hence the reduction of 1 from target
#             contiguous_averages.append(window_sum / target)
#             window_sum -= arrays[start]
#             start += 1
#     return contiguous_averages

def average_contiguous_sub_arrays_with_target(arrays: List[int], target: int):
    start, window_sum = 0, 0
    contiguous_averages = []

    for i, num in enumerate(arrays):
        window_sum += num

        if i >= target - 1:
            contiguous_averages.append(window_sum / target)
            window_sum -= arrays[start]
            start += 1

    return contiguous_averages


def closest_to_zero(numbers: List[int]) -> int:
    closest_num = None
    closest_diff = float("inf")

    for num in numbers:
        if abs(num) < closest_diff:
            closest_num = num
            closest_diff = abs(num)
    return closest_num


def find_factorial(number: int) -> int:
    return 1 if number <= 1 else number * find_factorial(number - 1)


"""
Given an array, find the number of negative values in a target array of size ‘target’.
Here we are asked to find the number of negative values in an array of target size 

Here is the final output containing the averages of all contiguous sub-arrays of size 5:
Array: [-1, 2, -2, 3, 5, -7, -5], target=3
NB: The size of each array is 3, so for the first iteration thats [-1,2,-2] has 2 negative numbers,
the second is [2,-2,3] and number of negatives is 1, and so on.
Output: [2, 1, 1, 1, 2]
"""


def get_counted_negatives_per_target(numbers: List[int], target: int) -> List[int]:
    negative_numbers = []
    window_numbers = []
    start = 0
    for index, num in enumerate(numbers):
        window_numbers.append(num)
        if len(window_numbers) == target + 1:
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
    return ["a", "e", "o", "i", "u"]


# is duplicate number


def find_duplicate(numbers: List[int], target: int) -> bool:
    return numbers.count(target) > 1


def find_max_sum(numbers: List[int], target: int) -> int:
    if numbers is None or target is None:
        return None
    max_value = 0
    start = 0
    window_sum = 0
    for i in range(len(numbers)):
        window_sum += numbers[i]
        if i - start + 1 == target:
            max_value = max(max_value, window_sum)
            window_sum -= numbers[start]
            start += 1
    return max_value


"""
Given an array of positive numbers and a positive number target, 
find the length of the smallest contiguous sub-array 
whose sum is greater than or equal to target. Return 0, 
if no such sub-array exists.
"""


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


"""
Difference between the maximum and minimum average of all k-length continuous subarrays
Input: arr[ ] = {3, 8, 9, 15}, K = 2
Output: 6.5
Explanation: All sub arrays of length 2 are {3, 8}, {8, 9}, {9, 15} 
and their averages are (3+8)/2 = 5.5, (8+9)/2 = 8.5, and (9+15)/2 = 12.0 respectively.

Therefore, the difference between the maximum(=12.0) and minimum(=5.5) is 12.0 -5.5 = 6.5.

THE FUNCTION BENEATH FINDS DIFFERENCE BETWEEN 
THE SUM OF MAXIMUM AND MINMAX VALUES
"""


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

    """
    A perfect number is one when reversed, its numeric value remain the same 
    Example: 1) 131 ==> 131 [√]   2) 34  ==> 43 [x]
    """


def perfect_number(number: int) -> bool:
    if len(str(number)) <= 1:
        return False
    return int(str(number)[::-1]) == number


def find_middle_number(numbers: List[int]) -> int:
    if len(numbers) % 2 != 0:
        return numbers[len(numbers) // 2]
    return (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2


def get_last_digits(number: int, digit_size: int) -> List[int]:
    num_str = str(number)
    return [int(x) for x in num_str[len(num_str) - digit_size :]]


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
        if len(window_el) == target + 1:
            nega = len(list(filter(lambda x: x < 0, window_el)))
            negatives.append(nega)
            window_el.pop(start)
            start += 1
    return negatives


print(count_negatives([-1, 2, -2, 3, 5, -7, -5], target=3))


def collectDuplicates(numbers: List[int]) -> List[int]:
    my_duplicates: Set[int] = {
        numbers[i] for i in range(len(numbers)) if numbers.count(numbers[i]) > 1
    }
    return list(my_duplicates)


"""[3, 8, 9, 15], 2
Given an array of characters where each character represents a 
fruit tree, you are given two baskets and your goal is to put 
maximum number of fruits in each basket. The only restriction 
is that each basket can have only one type of fruit.

You can start with any tree, but once you have started you can’t skip a tree. 
You will pick one fruit from each tree until you cannot, i.e., you will stop 
when you have to pick from a third fruit type.

This problem follows the Sliding Window pattern and is quite 
similar to Longest Substring with K Distinct Characters. 
In this problem, we need to find the length of the longest 
subarray with no more than two distinct characters (or fruit types!). 
This transforms the current problem into Longest Substring with
K Distinct Characters where K=2.
========  SAMPLE ======

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""


def fruits_into_basket(fruits: list):
    start, max_length = 0, 0
    fruit_freq = {}

    for i in range(len(fruits)):
        right_fruit = fruits[i]
        if right_fruit not in fruit_freq:
            fruit_freq[right_fruit] = 0
        fruit_freq[right_fruit] += 1

        while len(fruit_freq) > 2:
            left_fruit = fruits[start]
            fruit_freq[left_fruit] -= 1
            if fruit_freq[left_fruit] == 0:
                del fruit_freq[left_fruit]
            start += 1
        max_length = max(max_length, i - start + 1)
    return max_length