from typing import List

"""
  find duplet for a given sum
  Given an array of unsorted numbers find two numbers within the array that when added 
  equals the target sum.
  EG. array = [1,2,-3,4,-2,-1, 0], target = 0, ANS: [[-2, 2]]
"""
# [1, 2, -3, 4, -2, -1, 0], 3
def find_duplex(numbers: List[int], target: int) -> List[int]:
    numbers.sort()
    duplicate: List[int] = []
    end_el = len(numbers) - 1
    for i in range(len(numbers)):
        if numbers[i] + numbers[end_el] == target:
            duplicate.append([numbers[i], numbers[end_el]])
        elif numbers[i] + numbers[end_el] > target:
            end_el -= 1
        elif numbers[i] + numbers[end_el] < target:
            i += 1
    return duplicate

# print(f"Find Duplexes: {find_duplexs([1, 2, -3, 4, -2, -1, 0], 3)}")


"""
Problem Statement: Given an unsorted array return list of a 
list of three numbers that sum up to the target
This problem is also related to 3 sum closest to zero 
1. sort the array in place and declare triplet list 
2. loop over the array with a len - 2
3. find the diff btn target and 1st index value
4. declare [start and end pointers ] 
    a 'start = i + 1'  and 'end = len of array -1 ' pointers 
5. perform a while loop while start is < end 
6. current_sum  = array value at start + array value at end 
7. do the checks and append when needed.
"""
def find_triplets(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()  # complexity is OlogN

    triplets = []
    for i in range(len(nums) - 2):
        diff = target - nums[i]
        start = i + 1
        end = len(nums) - 1
        while start < end:
            current_target_sum = nums[start] + nums[end]
            if current_target_sum == diff:
                triplets.append([nums[i], nums[start], nums[end]])
                start += 1
                end -= 1
            elif current_target_sum < diff:
                start += 1
            else:
                end -= 1
    return triplets


"""
Quadruple Sum to Target (medium) #
Given an array of unsorted numbers and a target number, 
find all unique quadruplets in it, 
whose sum is equal to the target number.
Example 1:

Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.
"""
# WRITE TEST FOR THIS FUNCTION
def quadruple_sum_target(arr: List[int], target: int):
    arr.sort()
    quadruplets = []

    for i in range(0, len(arr)-3):
        diff = target - arr[i]
        start = i + 1
        end = len(arr) - 1

        while start <= end:
            current_sum = arr[start] + arr[start + 1] + arr[end]
            if current_sum == diff:
                quadruplets.append([arr[i], arr[start], arr[start + 1], arr[end]])
                start += 1
                end -= 2
            elif current_sum < diff:
                start += 1
            else:
                end -= 1
    return [x for x in quadruplets]


def closest_to_zero(numbers: List[int]):
    closest_num = None
    closest_diff = float('inf')  # Set initial difference to infinity
    for num in numbers:
        if abs(num) < closest_diff:
            closest_num = num
            closest_diff = abs(num)
    return closest_num

"""
Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
This algorithms find the best 3 numbers thats closest to the given target.
Example Given: [1, 20, 1, 1] with target=100) == 22 is the sum of the best 3 numbers
thats closest to the target 100.
"""

def three_sum_closest_target(nums: List[int], target: int) -> int:
    best_sum = 100_000
    nums.sort()
    for i in range(len(nums) - 2):
        lower = i + 1
        upper = len(nums) - 1
        while lower < upper:
            current_sum = nums[i] + nums[lower] + nums[upper]
            if current_sum == target:
                return current_sum
            if abs(target - current_sum) < abs(target - best_sum):
                best_sum = current_sum
            if current_sum <= target:
                lower += 1
            else:
                upper -= 1
    return best_sum

"""
do inplace removal of duplicates without  
using additional data structures like sets or space.
"""
def remove_duplicates(numberArray: List[int]):
    start, nextIndex = 1, 1
    for start in range(len(numberArray)):
        if numberArray[nextIndex - 1] != numberArray[start]:
            numberArray[nextIndex] = numberArray[start]
            nextIndex += 1
    return nextIndex




def find_duplex_trial(numbers: List[int], target: int) -> List[List[int]]:
    numbers.sort()
    last_index: int = len(numbers) -1
    target_pairs: List[int] = []
    for i in range(len(numbers)):
        if numbers[i] + numbers[last_index] == target:
            target_pairs.append([numbers[i], numbers[last_index]])
        elif numbers[i] + numbers[last_index] > target:
            last_index -= 1
        else: 
            i += 1
    return target_pairs


"""
Problem Statement #
Given an array arr of unsorted numbers and a target sum, 
count all triplets in it such that 
arr[i] + arr[j] + arr[k] < target where i, j, 
and k are three different indices.
Write a function to return the count of such triplets.

Example 1:
Input: [-1, 0, 2, 3], target=3 
Output: 2

Explanation: There are two triplets 
whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
Example 2:

Input: [-1, 4, 2, 1, 3], target=5 
Output: 4
Explanation: There are four triplets whose sum is less than the target: 
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
"""
def count_triplet_with_smaller_sum(nums: List[int], target: int) -> int:
    result = 0
    nums.sort()
    for i in range(len(nums) - 2):
        lower = i + 1
        upper = len(nums) - 1
        while lower < upper:
            current_sum = nums[i] + nums[lower] + nums[upper]
            if current_sum < target:
                result += upper - lower
                lower += 1
            else:
                upper -= 1
    return result


"""
GIVEN AN ARRAY OF NUMBERS FIND THE SUM OF TWO NUMBERS THAT GIVES THE EXPECTED TARGET
RETURN THE THEIR POSITION IN THE ARRAY GIVEN 
EG ARRAY = [12,-10, -2, 7, 4], TARGET = 5 , OUTPUT = [ -2, 7 ] POSITIONS = [2,3]
"""

def advancedTwoSum(nums: List[int], target: int) -> List[int]:
    for index, value in enumerate(nums):
        diff = target - value
        if diff in nums:
            return [index, nums.index(diff)]


print(f"Two Sum: {advancedTwoSum([12,-10, -2, 7, 4], target=5)}")

def is_prime(num):
    for n in range(2,int(num**0.5)+1):
        if num % n == 0:
            return False
    return True


def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_num = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_num)
    return fib_sequence


def list_valid_parentheses(parentheses: List[str]) -> List[str]:
   return [ paren for paren in parentheses if is_valid_parenthesis(paren=paren) ]

def is_valid_parenthesis(paren: str) -> bool:
    return paren.count('(') ==  paren.count(')')


"""
Problem Statement #
Given an array containing 0s, 1s and 2s, sort the array in-place. 
You should treat numbers of the array as objects, 
hence, we can’t count 0s, 1s, and 2s to recreate the array.

The flag of the Netherlands consists of three colors: red, 
white and blue; and since our input array also consists of 
three different numbers that is why it is called Dutch National Flag problem.

Example 1:
Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]

Example 2:
Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]
"""
def dutch_national_flag(arr: List[int])-> List[int]: 
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[mid], arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


