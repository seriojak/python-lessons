import datetime

# Tuple
print('---------------Tuple-------------')

tuples = ("Norway", 4.953, 3)

print(tuples[0])
print(len(tuples))

print(tuples + (338186.0, 265e9))

single_tuple = (391,)
print(single_tuple)

empty_tuple = ()
print(type(empty_tuple))

many_tuples = 1, 2, 3, 1, 7
print(type(many_tuples))


def min_max(items):
    return min(items), max(items)


print(min_max([83, 33, 34, 84, 32, 85, 61]))
print(tuple([1, 55, 3, 10, 55]))

lower, upper = min_max([83, 33, 34, 84, 32, 85, 61])

a = 'jelly'
b = 'bean'

a, b = b, a

print(5 in (3, 5, 17, 257))

# Strings
print('---------------Strings-------------')

print(len('llanfairpwllgwaynfullg'))

colors = ';'.join(['#45ff23', '#1234fa', '45ff23'])
print(colors)

print(colors.split())

print('unforgettable'.partition('forget'))

print("The age of {0} is {1}".format('Jim', 32))

value = 4 * 20
print(f'The value is {value}')
print(f'The current time is {datetime.datetime.now().isoformat()}')

# Ranges
print('---------------Ranges-------------')

print(range(5))

for i in range(5):
    print(i)

print(list(range(5, 10)))

t = [6, 372, 8862, 14800, 20846]

for p in enumerate(t):
    print(p)

# List
print('---------------List-------------')

arr = [1, -4, 10, -16, 15]

print(arr[-1])

print(arr[1:3])

print(arr[:])

refArr = arr

print(refArr is arr)

cloneArr = arr[:]

print(cloneArr is arr)
print(cloneArr == arr)

arr2 = arr.copy()

print(arr2 is arr)

arr3 = list(arr)

print(arr3 is arr)

del arr[2]

print(arr)

arr.remove(-16)

print(arr)

arr.insert(2, 10)

print(arr)

arr.reverse()
arr.sort()

# Dictionaries
print('---------------Dictionaries-------------')

dic = {'kay': 'value', 'otherKey': 'otherValue'}

print(type(dic))

# Sets
print('---------------Sets-------------')

sets = {0, 12, 'string', 10, 10}

print(sets)
print(type(sets))

