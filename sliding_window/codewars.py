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

# import requests 

# def fetch_data_calculate_total_costs(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         total_cost = sum([ x['price'] * x['quantity'] for x in data  ])
#         return {'total_cost': total_cost}
#     else:
#         return 'Could not fetch the requested url '


USER_ROLES = [
            {
                "id": 10,
                "name": "borga_create_employee",
                "description": "",
                "created": "2023-08-15T10:10:13.584407",
                "updated": "2023-08-15T10:10:13.584416"
            },
            {
                "id": 13,
                "name": "borga_update_delivery_account",
                "description": "",
                "created": "2023-08-15T10:10:13.587084",
                "updated": "2023-08-15T10:10:13.587094"
            },
            {
                "id": 8,
                "name": "borga_update_employee",
                "description": "",
                "created": "2023-08-15T10:10:13.582775",
                "updated": "2023-08-15T10:10:13.582785"
            },
            {
                "id": 6,
                "name": "borga_manage_deliveries",
                "description": "",
                "created": "2023-08-15T10:10:13.581038",
                "updated": "2023-08-15T10:10:13.581048"
            },
            {
                "id": 14,
                "name": "borga_update_merchant",
                "description": "",
                "created": "2023-08-15T10:10:13.588192",
                "updated": "2023-08-15T10:10:13.588201"
            },
            {
                "id": 9,
                "name": "borga_manage_orders",
                "description": "",
                "created": "2023-08-15T10:10:13.583591",
                "updated": "2023-08-15T10:10:13.5836"
            },
            {
                "id": 12,
                "name": "borga_dispute_resolution",
                "description": "",
                "created": "2023-08-15T10:10:13.586229",
                "updated": "2023-08-15T10:10:13.586239"
            },
            {
                "id": 1,
                "name": "borga_create_merchant",
                "description": "",
                "created": "2023-08-15T10:10:13.576729",
                "updated": "2023-08-15T10:10:13.576747"
            },
            {
                "id": 4,
                "name": "borga_view_audit_trail",
                "description": "",
                "created": "2023-08-15T10:10:13.579521",
                "updated": "2023-08-15T10:10:13.579531"
            },
            {
                "id": 5,
                "name": "borga_view_transactions",
                "description": "",
                "created": "2023-08-15T10:10:13.580296",
                "updated": "2023-08-15T10:10:13.580307"
            },
            {
                "id": 3,
                "name": "borga_update_admin",
                "description": "",
                "created": "2023-08-15T10:10:13.578811",
                "updated": "2023-08-15T10:10:13.57882"
            },
            {
                "id": 11,
                "name": "default-roles-borga-dev",
                "description": "${role_default-roles}",
                "created": "2023-08-15T10:10:13.585219",
                "updated": "2023-08-15T10:10:13.585228"
            },
            {
                "id": 7,
                "name": "borga_set_forex_rate",
                "description": "",
                "created": "2023-08-15T10:10:13.581944",
                "updated": "2023-08-15T10:10:13.581954"
            },
            {
                "id": 15,
                "name": "borga_create_delivery_account",
                "description": "",
                "created": "2023-08-15T10:10:13.589391",
                "updated": "2023-08-15T10:10:13.5894"
            },
            {
                "id": 2,
                "name": "borga_reporting",
                "description": "",
                "created": "2023-08-15T10:10:13.577884",
                "updated": "2023-08-15T10:10:13.577896"
            }
        ]

from typing import List
def is_user_authorize_by_role(roles: List[str], role: str) -> bool:
    return True if role == "SUPERADMIN" else role in roles


roles = [role['name'] for role in USER_ROLES]

print("User has role: " + str(is_user_authorize_by_role(roles, "SUPERADMIN")))


#  ==========    USER ROLES SIMPLIFIED IN KOTLIN    ==========
""" 
IMPLEMENTATION STRATEGY
1. Get the user by Id and extract his roles into an array of role names
2. make comparison if the explicit role in question is in the user's roles
3. Also checks if the user has the superior role then return True and and enable access to all resources 
4. If True enable access to the resource or collection in question else restrict and throw appropriate response.


SUMMARY OR SIMPLIFICATION STRATEGY 
1. Get roles of user 
"""




# import java.time.LocalDateTime

# data class UserRole(
#     val id: Int,
#     val name: String,
#     val description: String,
#     val created: LocalDateTime,
#     val updated: LocalDateTime
# )

# fun isUserAuthorizedByRole(roles: List<String>, role: String): Boolean {
#     return when (role) {
#         "SUPERADMIN" -> true
#         else -> role in roles
#     }
# }

# fun main() {
#     val userRoles = listOf(
#         UserRole(10, "borga_create_employee", "", LocalDateTime.parse("2023-08-15T10:10:13.584407"), LocalDateTime.parse("2023-08-15T10:10:13.584416")),
#         UserRole(13, "borga_update_delivery_account", "", LocalDateTime.parse("2023-08-15T10:10:13.587084"), LocalDateTime.parse("2023-08-15T10:10:13.587094")),
#         UserRole(8, "borga_update_employee", "", LocalDateTime.parse("2023-08-15T10:10:13.582775"), LocalDateTime.parse("2023-08-15T10:10:13.582785")),
#         UserRole(6, "borga_manage_deliveries", "", LocalDateTime.parse("2023-08-15T10:10:13.581038"), LocalDateTime.parse("2023-08-15T10:10:13.581048")),
#         UserRole(14, "borga_update_merchant", "", LocalDateTime.parse("2023-08-15T10:10:13.588192"), LocalDateTime.parse("2023-08-15T10:10:13.588201")),
#         UserRole(9, "borga_manage_orders", "", LocalDateTime.parse("2023-08-15T10:10:13.583591"), LocalDateTime.parse("2023-08-15T10:10:13.5836")),
#         UserRole(12, "borga_dispute_resolution", "", LocalDateTime.parse("2023-08-15T10:10:13.586229"), LocalDateTime.parse("2023-08-15T10:10:13.586239")),
#         UserRole(1, "borga_create_merchant", "", LocalDateTime.parse("2023-08-15T10:10:13.576729"), LocalDateTime.parse("2023-08-15T10:10:13.576747")),
#         UserRole(4, "borga_view_audit_trail", "", LocalDateTime.parse("2023-08-15T10:10:13.579521"), LocalDateTime.parse("2023-08-15T10:10:13.579531")),
#         UserRole(5, "borga_view_transactions", "", LocalDateTime.parse("2023-08-15T10:10:13.580296"), LocalDateTime.parse("2023-08-15T10:10:13.580307")),
#         UserRole(3, "borga_update_admin", "", LocalDateTime.parse("2023-08-15T10:10:13.578811"), LocalDateTime.parse("2023-08-15T10:10:13.57882")),
#         UserRole(11, "default-roles-borga-dev", "\${role_default-roles}", LocalDateTime.parse("2023-08-15T10:10:13.585219"), LocalDateTime.parse("2023-08-15T10:10:13.585228")),
#         UserRole(7, "borga_set_forex_rate", "", LocalDateTime.parse("2023-08-15T10:10:13.581944"), LocalDateTime.parse("2023-08-15T10:10:13.581954")),
#         UserRole(15, "borga_create_delivery_account", "", LocalDateTime.parse("2023-08-15T10:10:13.589391"), LocalDateTime.parse("2023-08-15T10:10:13.5894")),
#         UserRole(2, "borga_reporting", "", LocalDateTime.parse("2023-08-15T10:10:13.577884"), LocalDateTime.parse("2023-08-15T10:10:13.577896"))
#     )

#     val roles = userRoles.map { it.name }

#     println("User has role: ${isUserAuthorizedByRole(roles, "SUPERADMIN")}")
# }
