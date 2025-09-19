def check_duplicate(num):
    if len(nums) == len(set(nums)):
        return "Number are not Duplicate. "
    else:
        return "Number are Duplicate"
nums = [5,6,7,8,3,5]
print(check_duplicate(nums))

