
def two_sum(nums, target):
    empty_dictionary = {}
    for i , num in enumerate(nums):
        if target - num in empty_dictionary:
            return (empty_dictionary[target - num], i )
        empty_dictionary[num] = i

nums = [1,2,3,4,5,6,7,4,3]
target = 11
print(two_sum(nums, target))

