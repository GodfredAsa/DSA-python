
"""
FREE STYLE CODING EXERCISE
"""

from typing import List

CONSTANT_ONE = 1

def reverse_number(num: int) -> int:
    return int(str(num)[::-1])


print(reverse_number(123))


def factorial_of_number(num: int) -> int:
    return CONSTANT_ONE if num <= 0 else num * factorial_of_number(num - CONSTANT_ONE)

print(factorial_of_number(5))


def get_last_digits_per_target(num: int, target=2) -> int:
    num_arr = [n for n in str(num)]
    n_of_el = len(num_arr)
    if target >= n_of_el:
       return 0
    last_digits_target = num_arr[n_of_el - target:]
    return int("".join(last_digits_target))


print(get_last_digits_per_target(123, target=1))


def isDuplicate(nums: List[int], target: int) -> bool:
   return nums.count(target) > 1



print(isDuplicate([1,2,3,4,5,2,6], 2))


def collect_duplicates(nums: List[int]) -> List[int]:
    return list({ n for n in nums if isDuplicate(nums, n) })


print(collect_duplicates([1,2,3,4,5,2,6, 5]))

"""
Palindrome is a number that when its reversed has the same numeric value.
Example 212 => 212, 11 => 11 
Non-Palindromes: 123 => 321. Since 123 != 321 not a palindrome
"""

def isPalindrome(num: int) -> int:
    return int(str(num)[::-CONSTANT_ONE]) == num


print(isPalindrome(23))


def getFactors(num: int) -> List[int]:
    return [n for n in range(CONSTANT_ONE, num + 1) if num % n == 0 ]


print(getFactors(8128))

# a perfect number is a number whose sum of factors equals the number itself.
# 6 = [1,2,3] => 1 + 2 + 3 = 6. Hence 6 is a perfect number.
# Example: 6=[1,2,3], 28, 496, 8128

def isPerfectNumber(num: int) -> bool:
    return sum(getFactors(num)) == num


print(isPerfectNumber(6))
print(isPerfectNumber(28))
print(isPerfectNumber(8128))


def fibonacciSeries(num) -> List[int]:
    a, b = 0, 1
    results = []
    for _ in range(num):
        results.append(a)
        a, b = b, a + b
    return results


print(fibonacciSeries(4))



def manual_reverse_str(word: str) -> str:
    word = "-" + word 
    result_word = ""
    for i in range(1, len(word)):
        result_word += word[-i]
    return result_word


print(manual_reverse_str("beautiful"))


def countTwos(num: int) -> int:
    result = 0
    for i in range(0, num+1):
        if i % 2 == 0:
            result += 1
    print(result)

countTwos(7)

# swap number in place dont use temp variables 

def swap_arithmetic(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


print(swap_arithmetic(4,1))



import math
print(math.factorial(5))


# SORT ODD NUMBERS IN PLACE
def sort_odd_in_place(nums: List[int]) -> List[int]:
    odd_nums = sorted([n for n in nums if n % 2 != 0])
    return [x if x % 2 == 0 else odd_nums.pop(0) for x in nums]

print('----------------vvvvvvvv------------------')
print(sort_odd_in_place([5, 8, 6, 3, 4] ))
print('----------------vvvvvvvv------------------')


""" 
Given n, take the sum of the digits of n. If that value has more than one digit, 
continue reducing in this way until a single-digit number is produced. 
The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""

def digit_root(n) -> int:
    return n if n <= 9 else n % 9

print(digit_root(493193))

def find_middle_number(nums: List[int]):
    nLength = len(nums)
    if nLength % 2 != 0:
        return nums[nLength // 2]
    return sum([ nums[nLength // 2] + nums[(nLength // 2) + 1] ]) / 2


""" 
Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
"""

def int_to_roman(num):
    roman_numerals = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
        50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D',
        900: 'CM', 1000: 'M'
    }

    result = ''
    for value, symbol in sorted(roman_numerals.items(), reverse=True):
        while num >= value:
            result += symbol
            num -= value
    return result

print(int_to_roman(3))

def closest_zero(nums: List[int]) -> int:
    closest_num = None
    closest_diff = float('inf')
    for num in nums:
        if abs(num) < closest_diff:
            closest_num = num
            closest_diff = abs(num)
    return closest_num


def is_prime(num: int) -> bool:
    factors = getFactors(num)[:-1]
    return True if len(factors) == 1 else False


def prime_factors(num: int) -> List[int]:
    nFactors = [ n for n in range(CONSTANT_ONE, num + 1) if num % n == 0]
    return [x for x in nFactors if is_prime(x) == True]


print("-----------------------------")
NUMBER = 15
print(is_prime(NUMBER))
print(getFactors(NUMBER))
print(prime_factors(NUMBER))


def difference_two(arr1: List[int], arr2: List[int]) -> List[tuple]:
    return [(x, y) for x in arr1 for y in arr2 if abs(x-y)==2 and x * y <= 15]


print(difference_two([x for x in range(0, 6)], [y for y in range(1, 20, 2)]))