""" 
Implement the function unique_in_order which takes as argument a sequence and 
returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
"""


from itertools import groupby

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]

print(unique_in_order("AAAABBBCCDAABBB"))



""" 
You will be given an array of numbers. 
You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
ChatGPT
You can achieve this by first extracting the odd numbers from the array,
 sorting them, and then placing them back into their original positions in the array. 
 Here's how you can do it in Python:
"""


def sort_array(source_array):
    # Extract odd numbers from the array and sort them
    odd_numbers = sorted([num for num in source_array if num % 2 != 0])
    # Replace odd numbers in the original array with sorted odd numbers
    index = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = odd_numbers[index]
            index += 1

    return source_array


def sort_array(nums):
    odd_numbers = sorted([x for x in nums if x % 2 != 0]) # sorted odd numbers 
    return [x if x % 2 == 0 else odd_numbers.pop(0) for x in nums]

""" 
Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types.
"""
def find_short(s):
   return len(min(s.split(' '), key=len))

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

# def digital_root(n):
#     if n < 10:
#         return n
    
#     # Calculate the sum of digits
#     sum_of_digits = sum(int(digit) for digit in str(n))
    
#     # Recursive call to calculate digital root of the sum of digits
#     return digital_root(sum_of_digits)

def digital_root(n):
	return n % 9 or n and 9 

print(digital_root(19))


""" 
Write a function, persistence, 
that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.

For example (Input --> Output):

39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
"""

def persistence(n):
    return 0 if n < 10 else persistence(eval('*'.join(str(n)))) + 1


# import requests 

# response = requests.get('http://127.0.0.1:5001//api/items')

# if response.status_code == 200: 
#     print(response.json())

data =  [
   {
      "itemId":"0608235f-cb38-4ce2-8c53-9090fc087ab4",
      "name":"leaf",
      "desc":"organic",
      "imageUrl":"image",
      "quantity":10,
      "price":30.5,
      "createdAt":"27-11-2023"
   },
   {
      "itemId":"fce5f548-54ca-4a8b-b2c1-3931a5b3c53e",
      "name":"orange",
      "desc":"organic",
      "imageUrl":"image",
      "quantity":10,
      "price":30.5,
      "createdAt":"10-4-2024"
   },
   {
      "itemId":"99be41ad-cd86-42a8-947b-3064acce2fab",
      "name":"tea",
      "desc":"organic",
      "imageUrl":"image",
      "quantity":10,
      "price":30.5,
      "createdAt":"10-4-2024"
   }
]


total_cost = sum([ x['price'] * x['quantity'] for x in data  ])

print(total_cost)

import requests 

def fetch_data_calculate_total_costs(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        total_cost = sum([ x['price'] * x['quantity'] for x in data  ])
        return {'total_cost': total_cost}
    else:
        return 'Could not fetch the requested url '

