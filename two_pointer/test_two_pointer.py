from two_pointer.two_pointer import dutch_national_flag, find_duplex, generate_fibonacci, is_prime, list_valid_parentheses, three_sum_closest_target, is_valid_parenthesis, advancedTwoSum, generate_fibonacci

def test_find_duplex():
    assert find_duplex([1,2,-3,4,-2,-1, 0], 0) == [[-2, 2]]

def test_three_sum_closest_target():
    assert three_sum_closest_target([-3, -1, 1, 2], target=1) == 0
    assert three_sum_closest_target([1, 20, 1, 1], target=100) == 22

def test_is_prime() -> None:
    assert is_prime(2) == True
    assert is_prime(11) == True
    assert is_prime(4) == False

def test_generate_fibonacci() -> None:
    assert generate_fibonacci(7) == [0,1,1,2,3,5,8]
    
def test_is_valid_parenthesis() -> None:
    assert is_valid_parenthesis('(())') == True
    assert is_valid_parenthesis('(()') == False

def test_list_valid_parentheses()-> None:
    assert list_valid_parentheses(['(', '(())', '(()']) == ['(())']

def test_dutch_national_flag() -> None:
     assert dutch_national_flag([1, 0, 2, 1, 0]) == [0, 0, 1, 1, 2]

def test_advancedTwoSum() -> None:
     assert advancedTwoSum([12,-10, -2, 7, 4], target=5) == [2, 3]

def test_generate_fibonacci() -> None:
     assert generate_fibonacci(1) == [0, 1]
     assert generate_fibonacci(3) == [0, 1, 1]
     assert generate_fibonacci(4) == [0, 1, 1, 2]
     assert generate_fibonacci(5) == [0, 1, 1, 2, 3]




from typing import List

# def find_duplex(numbers: List[int], target: int) -> List[int]:
#     numbers.sort()
#     number_pairs: List[int] = []
#     for i in range(len(numbers)):
#         next_index = len(numbers) - 1
#         if numbers[i] + numbers[next_index] == target:
#             number_pairs.append([numbers[i], numbers[next_index]])
#         elif numbers[i] + numbers[next_index] < target:
#             i += 1
#         else:
#             next_index -= 1
#     return number_pairs

# def find_triplets(numbers: List[int], target: int) -> List[int]:
#     numbers.sort()
#     number_pairs: List[int] = []
#     for i in range(len(numbers) - 2):
#         next_index = i + 1
#         end_index = len(numbers) - 1
#         diff = target - numbers[i]
#         if numbers[next_index] + numbers[end_index] == diff:
#             number_pairs.append([numbers[i], numbers[next_index], numbers[end_index]])
#             next_index += 1
#             end_index -= 1
#         elif numbers[i] + numbers[next_index] < target:
#             i += 1
#         else:
#             next_index -= 1
#     return number_pairs

# def closest_zero(numbers: List[int]) -> int:
#     closest_num = None
#     closest_diff = float('inf')
#     for num in numbers:
#         if abs(num) < closest_diff:
#             closest_num = num
#             closest_diff = abs(num)
#     return closest_diff

# def count_triplets_smaller_sum(numbers: List[int], target: int) -> int:
#     number_triplets: int = 0
#     numbers,sorted()
#     for i in range(len(numbers)- 2):
#         lower = i + 1
#         upper = len(numbers) - 1
#         while lower < upper:
#             current_sum = numbers[i] + numbers[lower] + numbers[upper]
#             if current_sum < target:
#                 number_triplets += 1
#                 lower += 1
#             else:
#                 upper -= 1
#     return number_triplets

# def two_sum(numbers: List[int], target: int) -> List[int]:
#     for i in range(len(numbers)):
#         diff = target - numbers[i]
#         if diff in numbers:
#             return [i, numbers.index(diff)]
#         return None 

# def is_prime(number: int) -> bool:
#     for n in range(2, int(number ** 0.5) + 1):
#         if number % n == 0:
#             return False
#         return True
    
# def get_prime_numbers(numbers: List[int]) -> List[int]:
#     return [n for n in numbers if is_prime(n)]

# def generate_fibonacci_series(number: int) -> List[int]:
#     fib_series = [0, 1]
#     while len(fib_series) < number:
#         next_series = fib_series[-1] + fib_series[-2]
#         fib_series.append(next_series)
#     return fib_series