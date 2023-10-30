def twoSum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        if target - num in hashmap:
            return [hashmap[target - num], i]
        hashmap[num] = i

if __name__ == '__main__':
    target=10
    nums=[1,6,8,7,9]
    print(twoSum(nums, target))
