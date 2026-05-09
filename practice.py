# Reverse a list
a = [1, 2, 3, 4, 5]
a.reverse()
print(a)

# Find max number in list

b = [1, 5, 3, 4, 2]

max_value = b[0]

for num in b:
    if num > max_value:
        max_value = num

print("Max value:", max_value)

# Count frequency of elements

c = [1, 2, 2, 3, 3, 3, 4]

frequency = {}

for num in c:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequency:", frequency)

# Check if a list is sorted

list_1 = [1, 2, 3]

is_sorted = True

for i in range(len(list_1) - 1):
    if list_1[i] > list_1[i + 1]:
        is_sorted = False
        break

print("Is list_1 sorted:", is_sorted)

# Remove duplicates from list

list_2 = [1, 2, 2, 3, 4, 4]

unique = []

for num in list_2:
    if num not in unique:
        unique.append(num)

print("Sorted:", unique)

# Sum of list

# My Version

nums = [3, 5, 7, 2]
sum = nums[0] + nums[1] + nums[2] + nums[3]
print("Sum:", sum)

# Better Version

nums = [3, 5, 7, 2]

total = 0
for num in nums:
    total += num

print("Sum:", total)

# Find smallest number

smallest = [3, 1, 4, 2, 0]

smallest_value = smallest[0]

for num in smallest:
    if num < smallest_value:
        smallest_value = num

print("Smallest value:", smallest_value)

# Reverse list using loop


reverse_list = [1, 2, 3, 4, 5]
reversed_list = []
for i in range(len(reverse_list) - 1, -1, -1):
    reversed_list.append(reverse_list[i])

print("Reversed list:", reversed_list)


my_list = [1, 2, 3, 4, 5]

value = 10

if value in my_list:
    print("Value is in the list.")
else:
    print("Value is not in the list.")
