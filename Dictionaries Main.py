groceries = {
'fruits': ['mangoes', 'bananas', 'kiwis'],
'protein': ['beef', 'pork', 'salmon'],
'carbs': ['rice', 'pasta', 'bread'],
'veggies': ['lettuce', 'cabbage', 'onions']
}

print(groceries['veggies'])

second_list = {'desserts': ['mochi', 'ice cream', 'gulab jamun']}
groceries.update(second_list)
print(groceries)

print(groceries.keys())
print(groceries.values())

