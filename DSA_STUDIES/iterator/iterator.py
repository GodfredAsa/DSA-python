"""
docs_url = "https://docs.python.org/3.10/howto/functional.html"
    
"""

from ast import Set


L = [('Italy', 'Rome'), ('France', 'Paris'), ('US', 'Washington DC')]

countries = dict(iter(L))

print(countries)

# Generator expressions and list comprehensions

import itertools, functools, operator

permut = itertools.permutations("ABC", 3)

print(list(permut))

items = [
    {"name": "Jollof", "price": 100},
    {"name": "Jollof", "price": 203}

]
cost  = functools.reduce(operator.add, [item['price'] for item in items], 0)

print(cost)
