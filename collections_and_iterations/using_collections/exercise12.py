# Write some code that determines and prints whether the number 3 appears inside each of these lists:

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']


# My response:

print(3 in numbers1)    # True
print(3 in numbers2)    # False
print(3 in numbers3)    # False
print('3' in numbers4)  # True
print(3 in numbers5)    # True

# Comments:

# '3' is a string, not a number. Question specifically asks whether the number 3 is in the code.


# Launch School's answer:

print(3 in numbers1)          # True
print(3 in numbers2)          # False
print(3 in numbers3)          # False
print(3 in numbers4)          # False (3 != '3')
print(3 in numbers5)          # True  (3 == 3.0)
