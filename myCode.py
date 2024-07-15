# the below method is using set, which increases the space and time complexity as compared to the next method
def removeDuplicates(nums):
    nums[:] = set(nums)

    return nums

nums = [1,1,2]
func_call = removeDuplicates(nums)
print(func_call)


#without using set method
def removeDuplicates(nums):
    #defining it to 1 cz the previous one i.e at nums[0] is the first value and will be unique, so we check from nums[1]
    pointer_to_unique_value_in_array = 1

    #the loops iterates from seond element i.e index 1 to last element of array 
    for index in range(1, len(nums)):
        #if nums[1] i.e the seocnd element is not equal to the first element, then the second element is unique
        if nums[index] != nums[index-1]:
            #since current/second element is unique, we assign this element to the position of pointer in the list and increments pointer by 1
            nums [pointer_to_unique_value_in_array] = nums[index]
            pointer_to_unique_value_in_array += 1
    return pointer_to_unique_value_in_array

nums = [1,1,2]
func_call = removeDuplicates(nums)
print(func_call)