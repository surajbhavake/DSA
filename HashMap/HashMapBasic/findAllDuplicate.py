nums = [1,2,2,3,3,4]

freq = {}

for num in nums :
    freq[num] = freq.get(num,0)+1

duplicate = []

for key,value in freq.items():
    if value > 1:
        duplicate.append(key)

print(freq,duplicate)