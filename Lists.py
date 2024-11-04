lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
print(lst)

print(lst[0])
print(lst[4:6])

print(len(lst))

lst.append(99)
print(lst)

lst.remove(62)
print(lst)

lst.pop()
print(lst)

lst.pop(0)
print(lst)


#lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
#print(lst[2]) # prints abc
#print(lst[4:6]) # prints [62, ['g', 'h', 'i']]

#lst1 = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
#lst2 = [0, 1, 2, 3, 4]
#lst3 = ['I love sushi so much!', 'I also love curry!']

#print(len(lst1))  # prints 6
#print(len(lst2))  # prints 5
#print(len(lst3))  # prints 2

#lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
#lst.append(99) # appends 99 at the end of the list

#lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
#lst.remove(62) # removes 62 from the list

#lst = ['abc', 123, 'def', 10.5, 62, ['g', 'h', 'i']]
#lst.pop() # removes ['g', 'h', 'i']
#lst.pop(0) # removes 'abc'