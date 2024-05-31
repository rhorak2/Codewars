
# Write a function which calculates the average of the numbers in a given list
# Note: Empty arrays should return 0.

def find_average(numbers):
    if numbers == []:
        return 0
    else:
        return (sum(x for x in numbers)/len(numbers))

print(find_average([]))

"""
def find_average(array):
    return sum(array) / len(array) if array else 0
"""