nums = [1,2,2,3,2,4]
target = 2


#method 1 
freq = {}

for num in nums :
    freq[num] = freq.get(num, 0) +1

print(freq[target])


#method 2

count = 0

for num in nums:
    if num == target:
        count += 1

print(count)

